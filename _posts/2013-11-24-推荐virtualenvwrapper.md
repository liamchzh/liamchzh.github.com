---
date: 2013-11-24
layout: post
title: 推荐virtualenvwrapper
description: "推荐virtualenvwrapper"
categories: [python]
---

### 什么是virtualenvwrapper

用Python搞Web开发的应该都用过virtualenv，这是用来建立隔离的python环境的工具。  
而**virtualenvwrapper**就是[virtualenv](http://pypi.python.org/pypi/virtualenv)的扩展。  

### 安装及使用
安装：`pip install virtualenvwrapper`

安装成功后记得把`source /usr/local/bin/virtualenvwrapper.sh`加入到`.bashrc`才会开机运行

创建虚拟环境：`mkvirtualenv env1` 

创建好的虚拟环境会在`/home/usr/.virtualenvs`文件夹中

切换环境：`workon [env_name]`

设置当前环境的默认工作路径(下次执行 workon 命令会自动切换路径)：`(env_name) $ setvirtualenvproject`

删除环境：`rmvirtualenv <env_name>`

- - - - 
更多请参考：[http://virtualenvwrapper.readthedocs.org/en/latest/](http://virtualenvwrapper.readthedocs.org/en/latest/)
