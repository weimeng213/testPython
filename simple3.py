#! /usr/bin/python
from fabric.api import *
from fabric.colors import *
env.user='root'
env.hosts=['137.0.30.130','10.1.10.156']
env.passwords={'root@137.0.30.130:22':'vmware','root@10.1.10.156:22':'cloud123456','root@10.1.10.155:22':'cloud123456'}
env.roledefs={
'bridge':['137.0.30.130'],
'test':['10.1.10.155','10.1.10.156']
}
#env.parallel=True
env.colorize_errors=True
env.command_timeout=120
env.gateway='137.0.30.130'

@runs_once
def local_task():
	local("uname -a")
@runs_once
def remote_path():
	path=raw_input("please input your path:\n")
@runs_once
def remote_order():
	order=raw_input("please input your order:\n")
@roles('test')
#@parallel(pool_size=5)
def remote_task(path='.',order='who'):
	with settings(warn_only=True):
		with cd(path):
			print(red("Executing on {} as {}").format(env.host, env.user))
			run(order)
@roles('bridge')
def getfile():
	get('/tmp/zabbix_server.log.old','.')
"""def test():
	path=raw_input("please input your path:\n")
	order=raw_input("please input your order:\n")
	remote_task(path,order)
"""
