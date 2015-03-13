---
date: 2012-11-05 04:07:21+00:00
layout: post
title: 使用git提交到github
categories:
- Git
---

本文属于入门级，并假设你已经安装了git，注册了github，知道git的add和commit命令，知道用于切换目录的cd命令。

1. git的初始设置

这一步中设置跟github的用户名和邮箱完全没有关系。

    git config --global user.name YourName
    git config --global user.email you@email.address 

2. 在github中建立仓库

在右上角点击"Create a New Repo"  
然后填写Repository name & Description,可以暂时先不初始化一个readme文档。  

3. 在本地建立仓库并初始化

    cd /home/... //进入你要建立仓库的目录
    mkdir Repo_name //名字为刚刚在github创建的仓库名称
    cd Repo_name //进入刚刚建立的仓库
    git init //初始化
    touch README.md //初始化一个readme文件

4. 创建SSH密钥

ssh-keygen -C you@email.address -t rsa
选择路径save the key,直接按Enter使用默认路径，然后输入密码（这密码不是github的密码，而是用于提交时对提交者的验证，可以为空，这样就任何人都可以向你的仓库提交）。
找到默认路径中的id_rsa.pub文件，用文本编辑器打开，复制全部内容。
然后进入github，找到个人设置里面的SSH Keys,把刚才复制的字符串添加到Key，title可以随便写
保存，如果key没问题，需要确定github密码，如果错误，则提醒ssh key语法错误。

5. 连接github（第一次）

    git add README.md
    git commit -m 'first commit'
    git remote add origin git@github.com:github_username/Repo_name #你在github的用户名和仓库名
    git push -u origin master #要输入你在创建SSH密钥时输入的密码 提交成功后可以去github看看了

至此，最麻烦的步骤已经结束。当以后需要提交新的代码或者文件时，就可以这样提交了：

    cd Repo_name //进入已经创建的仓库目录
    git add . //添加全部文件
    git commit -m 'new commit' //commit
    git push -u origin master // push到github

一开始使用github，我也是糊里糊涂的瞎整。当时思路很乱，搞不清本地git和github的关系，然后我把它放一边。一直到现在想备份我的代码，才重新琢磨，发现原来其实没有那么复杂。

参考：

[Git/Github使用方法小记](http://artori.us/git-github-usage/)

[git/github初级运用自如](http://www.cnblogs.com/fnng/archive/2012/01/07/2315685.html)

--------------------------------------------------------------------------------------
2012.11.19更新-如何把github的代码下载到本地
前几天电脑数据丢失（痛失两年以来的代码），想要把github上的代码下载下来。
重新安装完git后 配置好SSH密钥
接着使用克隆命令
git clone git@github.com:github_username/Repo_name.git
仓库里面的全部代码就会自动下载到当前目录
然后重新连接本地目录和云端仓库
git remote add upstream git@github.com:github_username/Repo_name
然后就可以像往常那样push了

----------------------------------------------------------------------------------------

2013.1.9 发现形象生动 通俗易懂的git简易指南

请戳[这里](http://rogerdudler.github.com/git-guide/index.zh.html)
