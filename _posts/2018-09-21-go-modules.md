---
date: 2018-09-21
layout: post
title: Go Modules
description: "2018 年初，Russ Cox 发出了 vgo 的提案，Golang 官方博客也发表了文章，介绍了这个关于 package versioning 的提案。"
categories: [Golang]
---

## 前言
2018 年初，Russ Cox 发出了 vgo 的[提案](https://github.com/golang/proposal/blob/master/design/24301-versioned-go.md)，Golang 官方博客也发表了[文章](https://blog.golang.org/versioning-proposal)，介绍了这个关于 package versioning 的提案。Go team 最开始关于包版本管理的工作都是围绕 vgo 来做，在开始的阶段， vgo 一直在 Go 主仓库外，直到 2018 年 6 月，vgo 被 merge 到主干（[cmd/go: merge module support from x/vgo repo · golang/go@f7248f0 · GitHub](https://github.com/golang/go/commit/f7248f05946c1804b5519d0b3eb0db054dc9c5d6)），并改名为 `go moduels` 。截止目前，Go Modules 是 Go 1.11 中一项实验性功能。

## Go 包管理历史
Version < 1.5: 使用 Go Path

1.5 <= Version：配合 Vendor 目录

## Go Modules 是什么
Go modules 是 Go 1.11 的一项实验性功能，为了解决 Go 的包依赖管理问题。官方希望能在 1.11 中收集反馈和改进，接着在 Go 1.12 中确定这项功能。

Russ 连发[ 7 篇文章](https://research.swtch.com/vgo)，讲述了 vgo 的技术方案，在提案里，提出了使用 Semantic Import Versioning 和 Minimal Version Selection，引入 Go Modules 等。

Go Modules 在 proposal 里提出了几个新的概念。

### Modules

Module 是一些有特定版本的 Go package 的集合，非常重要的一点是，它们是统一的整体，并且是使用语义化版本的。

### go.mod

每个 module 都是在 `go.mod` 文件中定义的源代码树。Module 的源代码可以不在 Go Path 下。

在 go.mod 中你会看到  4 个命令，分别是：`module`, `require`, `exclude`, `replace`。

* exclude: 可以拒绝使用某个版本
* replace: 把 import path 替换成另一个，可以是在 VCS（例如 GitHub），也可以是本地某个路径

exclude 和 replace 都只对当前的 module 有效。`replace` 有个特殊的用途就是替换掉 golang.org/x 上的包，换成 GitHub 的路径。

```
module github.com/my/module/v3

require (
    github.com/some/dependency v1.2.3
    github.com/another/dependency v0.1.0
    github.com/additional/dependency/v4 v4.0.0
)

replace (
    golang.org/x/net v0.0.0-20180821023952-922f4815f713 => github.com/golang/net v0.0.0-20180826012351-8a410e7b638d
)
```

### [Semantic Import Versioning](https://research.swtch.com/vgo-import)

不兼容的升级应该怎么做？Semantic Import Versioning 的第一条规则就是：如果新的 package 和旧的 package，是同样的 import 路径，那么新的包就必须向后兼容。

通常来说，`my/thing` 这样的 module 版本是 v0，是允许不兼容的，等到了稳定版本，即 v1，如果这是出现不兼容，就需要重新命名：`my/thing/v2`。

![](/images/gomodules01.jpg)

### Minimal Version Selection

当安装或者升级依赖的时候，MVS 选择能满足依赖需求的版本中最老的（版本号最小的）。

在第一次构建整体依赖的时候，有两种方法，一个是递归；另一个是图的遍历。

递归就遍历所有依赖的包，已经依赖的包所依赖的包，得到一个所有包的版本列表，然后选择最新的。这种方法不是特别高效。

![](/images/gomodules02.jpg)

 另一种方法就是利用图的思想来遍历。

![](/images/gomodules03.jpg)

## 如何定义 Module 并升级（降级）依赖

### 如何使用 go.mod

确认已经安装 Go 1.11，需要先打开 module 开关

```
export GO111MODULE=on
```

然后执行
```
go mod init
```

目录下会新建一个 go.mod 文件。再执行 `go build` 命令，依赖的包的版本就会写到 go.mod 中。

示例：main.go
```
package main

import (
    "fmt"

    _ "go.uber.org/zap"
)

func main() {
    fmt.Println("hello")
}
```

执行 `go build main.go` 之后，自动下载 zap 并编译成二进制文件。这个过程中，下载完成后的 zap 并没有出现在 $GOPATH/src 下，这是 Go modules 的另外一个特性，也就是代码不需要再放在 GOPATH 或者 vendor 下。

go.mod
```
module mod

require (
	go.uber.org/atomic v1.3.2 // indirect
	go.uber.org/multierr v1.1.0 // indirect
	go.uber.org/zap v1.9.1 // indirect
)
```

### 从现有的包管理迁移

`go mod init` 能自动从 `Gopkg.lock` 等配置中，找到匹配的包版本，支持目前主流包管理工具，例如 dep, glide, govendor 等。

### 同时使用不兼容版本
Go modules 允许在 import path 中出现 v2 这样的带有主版本号的路径，所以甚至可以同时使用一个 package 的 v1 和 v2 两个版本的实现。

### 升级依赖
升级所有的依赖，依然可以使用 `go get -u`。如果用升级单独的包， `go get` 可以通过增加 @version 来指定，例如 `go get github.com/gorilla/mux@v1.6.2`。

### 准备发布

按照官方的[指引](https://github.com/golang/go/wiki/Modules#how-to-prepare-for-a-release)，发布前有几个检查项 ：

1. `go mod tidy` 确认所有包都引入进来或者删除无用的 module
2. `go test all` 确认测试已经通过
3. 检查 go.sum

Go 用 git tag 来表示版本，所以发布前需要给你的代码打上 tag，然后就可以发布了。

```
$ git tag v1.0.0
$ git push --tags
```

## 答疑

1.没有 GOPATH 和 Vendor，那编译的时候怎么找到依赖？

如果 GO111MODULE 设置了打开，那么编译的时候会忽略 vendor 目录。

2.编译的时候，下载的包放在哪里？

`$GOPATH/pkg/mod` 目录下

3.在 GOPATH 之外，报错 `outside GOPATH, no import comments`

需要指定导入的包名，例如`package main // import "github.com/you/hello"`

4.go.sum 文件是干嘛用的？

用来记录每个依赖包的版本和哈希值

