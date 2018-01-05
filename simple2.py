#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from fabric.api import *

env.user = 'root'
env.hosts = ['137.0.30.130','137.0.24.0']
env.password = 'vmware'

@runs_once   #主机遍历过程中，只有第一台触发此函数
def input_raw():
    return prompt('please input directoryname:',default='/root')

def worktask(dirname=''):
    run('ls -l '+dirname)

@task    #限定只有go函数对fab命令可见,其他没有使用@task标记的函数fab命令不可用
def go():
	prompt('please input directoryname:',key='ath',default='/')
	worktask(dirname=env.ath)
