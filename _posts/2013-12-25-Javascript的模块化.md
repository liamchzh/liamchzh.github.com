---
date: 2013-12-25
layout: post
title: Javascript的模块化
description: "如何使用多个js文件"
categories: [js, web]
---
我写chrome extension的时候，需要用到JQuery.js和jQuery.md5.js，以及其他自己写的JS文件。后来查资料，知道了require.js这样一个库，能够让你把JS文件组织到一起。

    <script src="js/require.js" data-main="js/main"></script>
    
    // main.js
    require(['moduleA', 'moduleB', 'moduleC'], function (moduleA, moduleB, moduleC){
    // some code here
    });
 

- - - -
顺便说说browserify

官方的介绍：

>>> Use a node-style `require()` to organize your browser code and load modules installed by npm.

>>> browserify will recursively analyze all the `require()` calls in your app in order to build a bundle you can serve up to the browser in a single `<script>` tag.

简单来说就是让你写的js文件能够在浏览器里运行而不仅仅运行在后端。

不久前试着给公司网站写一个简单的功能，从最底层的数据库操作到前端页面全都自己完成。底层的API很快写好，中间的controller也很简单，唯独前端的页面对于我来说是个不小的挑战。

关于JS，我没有写过，只知道一些传统的使用，例如`onclick`等。藉这个机会我了解了一些前端的技术，其中就包括Browserify、jQuery等。
