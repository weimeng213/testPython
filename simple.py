#! /usr/bin/python
from fabric.api import *
env.user='root'
env.hosts=['137.0.30.130','137.0.24.0']
env.password='vmware'
env.roledefs={
'bridge':['137.0.30.130']
'test':['10.1.10.155','10.1.10.156']
}
#env.parallel=True
env.colorize_errors=True
env.command_timeout=120

@runs_once
def local_task():
	local("uname -a")
@runs_once
def remote_path():
	path=raw_input("please input your path:\n")
@runs_once
def remote_order():
	order=raw_input("please input your order:\n")
def remote_task(path='.',order='who'):
	with settings(warn_only=True):
		with hide('running','stdout'):
			with cd(path):
				print("Executing on {} as {}".format(env.host, env.user))
				run(order)
"""def test():
	path=raw_input("please input your path:\n")
	order=raw_input("please input your order:\n")
	remote_task(path,order)
"""
