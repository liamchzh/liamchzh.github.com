---
date: 2019-03-02
layout: post
title: All You Need to Know about System Design Interview - 1
description: "最近看完了《Grokking the System Design Interview》，这个一个专门为 System Design 面试而准备的教程，里面对于面试中常见的场景，按照既定的模板，进行了分析和解答，同时还有一些后端的基本知识点。"
categories: [Tech]
---

最近看完了《Grokking the System Design Interview》，这个一个专门为 System Design 面试而准备的教程，里面对于面试中常见的场景，按照既定的模板，进行了分析和解答，同时还有一些后端的基本知识点。

跟考试一样，系统设计也是有套路的。

## Step 1: Requirements clarifications

首先要搞明白的是要你要解决什么问题，具体场景、用户数量、需要哪些功能、有没有别的要求，等等。

例如要设计一个 Twitter，在开始之前，你可以需要知道：

1. 用户能不能发表 tweets 和关注别人？
2. 要不要设计用户的 timeline？
3. Tweets 能不能包含图片和视频？
4. Tweets 能不能被搜索到？
5. 要不要展示「热门/热搜」？
6. 要不要做「消息通知」？

## Step 2: System interface definition

设计系统需要的 API，保证我们理解的需求是正确的。例如：

1. `postTweet(user_id, tweet_data, tweet_location, user_location, timestamp, …)  `
2. `generateTimeline(user_id, current_time, user_location, …)  `
3. `markTweetFavorite(user_id, tweet_id, timestamp, …)  `

## Step 3: Back-of-the-envelope estimation

为了后续的扩容、对数据进行分区、负载均衡、缓存数据，我们需要对系统的各方面进行预估。

* 系统的规模（用户数、Tweets 总数、浏览量，等等）
* 需要多少存储（是否包含图片和视频可能会使存储量大大不同）
* 流量（QPS 等决定了你需要多大的带宽，以及对后端存储的压力，如何进行负载均衡，等等）

## Step 4: Defining data model
数据需要在不同系统内的流转，如何设计一个好的 data model 至关重要，因为关系着后续数据的管理和分区。再细节一点，如何选择数据库，用 NoSQL 还是关系型数据库？如何是关系型，又该如何设计 schema？

## Step 5: High-level design

从前到后，画出系统的必要组件。对于 Twitter，我们需要不同的服务器来处理各种读写请求，再往下，我们需要数据库和缓存来保证数据能被快速写入和读取。如果需要存储图片和视频，我们还需要额外的 file system 甚至 CDN。

## Step 6: Detailed design

选择其中一两个系统进行详细分析和设计。对于这样的详细设计，一般都会有不同的方案，我们需要列出其中的优劣之处，并进行取舍。

* 数据如何进行 sharding？
* 如何处理热门的用户和数据？
* 为了 timeline 要不要专门为了拉取最新的数据进行优化？
* 在哪一层加缓存？

## Step 7: Identifying and resolving bottlenecks

尝试找出系统的瓶颈或单点。

* 怎么解决单点问题？
* 数据是否有冗余，避免丢失。
* 服务器节点的高可用怎么做？
* 如何监控程序的指标？

## Designing a URL Shortening service like TinyURL

分析完套路之后，可以看一个例子，如何设计一个短连接服务：[Designing a URL Shortening service like TinyURL](https://www.educative.io/collection/page/5668639101419520/5649050225344512/5668600916475904)

