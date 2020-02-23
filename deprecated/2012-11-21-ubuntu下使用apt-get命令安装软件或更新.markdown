---
date: 2012-11-21 08:20:19+00:00
layout: post
title: ubuntu下使用apt-get命令安装软件或更新
categories:
- Linux
description: "如果刚接触ubuntu，那么肯定对软件的安装特别困惑。面对.deb和.tar.gz，又出现各种命令，甚至还需要自己编译，安装起来会觉得还不如windows下的.exe方便。其实ubuntu下有一种很方便的安装软件方法，就是使用apt-get命令。"
---

如果刚接触ubuntu，那么肯定对软件的安装特别困惑。面对.deb和.tar.gz，又出现各种命令，甚至还需要自己编译，安装起来会觉得还不如windows下的.exe方便。  
其实ubuntu下有一种很方便的安装软件方法，就是使用apt-get命令。apt-get通过sources.list文件中设置的更新源来获取软件或更新。

1.编辑sources.list

sudo gedit /etc/apt/sources.list

2.打开以后，选择国内的更新源替换掉原来的国外的源

以下是北京理工大学的源(版本：12.10)，也可以使用其他例如网易或者教育网的源，具体请戳[这里](http://www.maybe520.net/blog/1647/)

    deb http://mirror.bit6.edu.cn/ubuntu/ quantal main restricted universe multiverse
    deb http://mirror.bit6.edu.cn/ubuntu/ quantal-security main restricted universe multiverse
    deb http://mirror.bit6.edu.cn/ubuntu/ quantal-updates main restricted universe multiverse
    deb http://mirror.bit6.edu.cn/ubuntu/ quantal-backports main restricted universe multiverse
    deb http://mirror.bit6.edu.cn/ubuntu/ quantal-proposed main restricted universe multiverse
    deb-src http://mirror.bit6.edu.cn/ubuntu/ quantal main restricted universe multiverse
    deb-src http://mirror.bit6.edu.cn/ubuntu/ quantal-security main restricted universe multiverse
    deb-src http://mirror.bit6.edu.cn/ubuntu/ quantal-updates main restricted universe multiverse
    deb-src http://mirror.bit6.edu.cn/ubuntu/ quantal-backports main restricted universe multiverse
    deb-src http://mirror.bit6.edu.cn/ubuntu/ quantal-proposed main restricted universe multiverse


3.保存后就可以安装或者更新。首先，更新软件包列表 sudo apt-get update

apt-get常用命令  
* 安装包 apt-get install package_name  
* 删除包 apt-get remove package_name  
* 升级系统 apt-get dist-upgrade  
* 下载源代码 apt-get source package_name  
* 查询软件包 apt-cache search package_name  
* 更详细的apt命令用法请戳[这里](http://blog.csdn.net/toddmi/article/details/7721198)

4.可以尝试安装一些软件软件

* chrome:    sudo apt-get install chromium-browser
* filezilla:      sudo apt-get install filezilla
* vim:           sudo apt-get install vim-gnome
* php:           sudo apt-get install php5
* py idle:       sudo apt-get install idle
