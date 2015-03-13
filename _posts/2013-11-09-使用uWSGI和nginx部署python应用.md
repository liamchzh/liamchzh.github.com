---
date: 2013-11-09 
layout: post
title: 使用uWSGI和nginx部署Python应用
description: "使用uWSGI和nginx部署Python应用"
categories: [python, web]
---

### 什么是uWSGI
部署过Python Web应用，应该都听说过[WSGI](http://zh.wikipedia.org/wiki/Web%E6%9C%8D%E5%8A%A1%E5%99%A8%E7%BD%91%E5%85%B3%E6%8E%A5%E5%8F%A3)，它的全称是：Web Server Gateway Interface，是为Python语言定义的Web服务器和Web应用程序或框架之间的一种简单而通用的接口。而uwsgi同样是一种通信协议，而uWSGI是实现了uwsgi、WSGI、http协议等协议的Web Server。

### uWSGI干什么用的
既然uWSGI已经是http server，那为什么还要nginx？我也不知道，查了一会，看到[一篇博文](http://ieqi.net/2012/08/06/ubuntu-12-04-%E4%B8%8B%E9%83%A8%E7%BD%B2-nginxuwsgiflask/)说：

>>>从现在已有的实践来看，对于Flask，比较好的部署方式是使用uWSGI做WSGI容器，Nginx做前端服务器。这样做的好处在于：
>>>1. uWSGI性能好，提供的功能也很多，运维方便。
>>>2. Nginx对于静态文件处理较好，而且默认支持uWSGI协议，在负载均衡和压力控制上都可以很方便的实现。

### uWSGI安装和配置
安装过程非常简单：

    pip install uwsgi
    
至于配置，方法有很多，我在网上找到的方法基本都是使用xml来配置，其实个人认为最方便的配置方法是使用命令行参数，也可以写成一个bash脚本。

参数的选项非常多，这里列出几个常用的：

* `--socket 127.0.0.1:3031`  
* `--processes 8`  8个工作进程
* `--master` 启动主进程
* `--vhost` 开启虚拟主机模式
* `--callable` 指定加载的模块中将被调用的变量名，即`app=Falsk(__name__)`中的`app`


### 配置nginx
我系统是ubuntu，配置文件在/etc/nginx/site-availalbe/里。你也可以不用default，例如新建一个mysite，不过要记得链接到site-enabled：`ln -s /etc/nginx/site-availabe/mysite /etc/nginx/site-enabled`

nginx的配置文件里，需要告诉nginx跟uWSGI通信的socket端口。

    location / {
        include uwsgi_params;
        uwsgi_pass 127.0.0.1:3031;
    }

具体配置可以参考以下：  


    server {
    	listen   80;
    	server_name xxx.com;
    
    	try_files $uri @uwsgi;
    	location @uwsgi  {
    		uwsgi_pass 127.0.0.1:3031;
    		include uwsgi_params;
    		uwsgi_param UWSGI_SCHEME $scheme;
    		uwsgi_param SERVER_SOFTWARE nginx/$nginx_version;
    	}
    
    	location / {
    		include uwsgi_params;
    		uwsgi_pass 127.0.0.1:3031;
    	}
    }

我也找了很多nginx的配置文件，不断修改才运行成功。

### 参考资料
* [Quickstart for python/WSGI applications](http://uwsgi-docs.readthedocs.org/en/latest/WSGIquickstart.html)  
* [uWSGI配置文档翻译](http://www.cnblogs.com/zhouej/archive/2012/03/25/2379646.html)  
* [Nginx + uWSGI + Flask + Vhost](http://my.oschina.net/lanybass/blog/61896)  
