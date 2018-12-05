---
date: 2018-12-02
layout: post
title: Debugging Go Code with Delve
description: "Delve 是专门针对 Go 的 debugger"
categories: [Golang]
---

## Delve 是什么
Delve 是专门针对 Go 的 debugger。

在工作中，因为没有类似 iPython 之类的 shell 环境，加上目前也没有办法在开发环境进行调试，所以 Go 项目 debug 变得非常不方便。

## 比 GDB 好在哪里
Go 语言支持 GDB、LLDB 和 Delve 几种调试器。其中 GDB 是最早支持的调试工具，LLDB 是 macOS 系统推荐的标准调试工具。但是 GDB 和 LLDB 对 Go 语言的专有特性都缺乏很大支持，而只有 Delve 是专门为 Go 语言设计开发的调试工具，而且 Delve 本身也是采用 Go 语言开发（以及少部分 C 语言）。

Delve 专门为 Go 而开发，所以它需要更了解 Go 的特性：

* Execution Model
* Stack Management
* Compiler Optimizations

除了 CLI ，还提供了 JSON-RPC API，能配合 IDE 工作；另外还有一个 [GUI frontend for Delve](https://github.com/aarzilli/gdlv)。

## 安装
可以通过 go get 来安装，其他安装方法见 [Installation](https://github.com/derekparker/delve/tree/master/Documentation/installation)

`$go get -u github.com/derekparker/delve/cmd/dlv`

## 使用
### debug 命令
编译并开始 debug，可以指定具体的 package  
`$dlv debug ./your-project/main.go`

*args*  
打印当前函数参数的名字和值

*break*  
设置断点，`break [name] <linespec>`，缩写 `b`  
用法：

* `b main.main`
* `b /GOPATH/your-project/pkg/dir/file.go:26`
* `b +5`

*clear*  
删除断点，`clear <breakpoint name or id>`  

*continue*  
直到下一个断点，缩写 `c` 

*goroutine*  
显示或切换 goroutine

*goroutine*  
列出所有 goroutines

*next*  
下一行，缩写 `n`

*print*  
执行一个表达式，缩写 `p`

*step & step out*  
进入和退出函数

*set*  
给变量重新赋值

*restart*  
杀掉当前进程，然后重启

*stack*  
打印 stack trace，缩写 `bt`（特别好用）

### attach 命令

Delve 还允许直接 attach 到具体的进程，然后就像 debug 命令一样进行调试。这里不展开。

用法：`dlv attach pid`
