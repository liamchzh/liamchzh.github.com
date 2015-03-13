---
date: 2013-03-26 03:39:10+00:00
layout: post
title: 微信校园助手——微信公众平台+Django+SAE
categories:
- Python
description: "写一个自动回复的微信公众平台"
---

上一篇介绍了[微信公众平台API](http://liamchzh.com/%E5%BE%AE%E4%BF%A1%E5%85%AC%E4%BC%97%E5%B9%B3%E5%8F%B0api/)，知道了调用的流程之后就可以自己写一个自动回复的小玩意。





## 「人在北理」——校园助手





我需要的功能是让同学快速查询或分享一些校园内有用的信息。经过几天的开发，目前有的功能是：







  * 查询校车和环一公交的发车时刻。


  * 查询天气和空气质量。


  * 英文翻译。


  * 通过微信给人人主页发状态。





## 具体实现





先看views.py中的一段代码




    
    def handleRequest(request):
        if request.method == 'GET':
            response = HttpResponse(checkSignature(request),content_type="text/plain")
            return response
        elif request.method == 'POST':
            response = HttpResponse(responseMsg(request),content_type="application/xml")
            return response
        else:
            return None
    #校验
    def checkSignature(request):
    
    #处理request中的content     
    def responseMsg(request):





填写接口配置信息的url和token之后后，微信服务器将发送GET请求到填写的URL上，并且带上四个参数，你要做的就是校验，如果正确则返回echoStr。这一步只需要验证一次。通过验证之后，微信用户发到公众平台的消息都会被POST到这个url上，这时，你要做的就是提取用户的消息，处理之后返回相应的结果。注意返回的消息也要按照规定的xml结构才能发回给用户。





详细代码请见：  
[views.py](https://github.com/liamchzh/python/blob/master/views.py)  
[renren.py](https://github.com/liamchzh/python/blob/master/renren.py)  
[weather.py](https://github.com/liamchzh/python/blob/master/weather.py)





## 其他





### 参考资料：





[微信机器人：小蜗牛有道翻译小助手](http://blog.csdn.net/liushuaikobe/article/details/8453716)  

[微信公众平台API调用的方法](http://www.shahuwang.com/?p=1552)  

[使用python登录人人网并发表状态](http://www.oschina.net/code/snippet_946076_17870)





### 感谢：





[PM25.in](http://pm25.in/)提供了查询空气质量（AQI，PM2.5，PM10）的API





### 欢迎关注「人在北理」——校园助手





[![getqrcode](http://liamchzh.com/wp-content/uploads/2013/03/getqrcode.jpg)](http://liamchzh.com/wp-content/uploads/2013/03/getqrcode.jpg)



