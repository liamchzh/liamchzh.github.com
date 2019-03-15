---
date: 2019-03-15
layout: post
title: 知乎匿名系统设计 (About System Design - 3)
description: "知乎的匿名功能，是在非常早期就已经加入的功能，至今问答业务历经各种迭代，匿名架构基本没有大改，从现在往回看，可以说当初的匿名系统设计，已经很好满足了产品的发展。但是如果我们能从现在的视角重新匿名系统，也许能做到更好。"
categories: [Tech]
---

声明：本文的设计与知乎现有的实际设计，并不一样，请勿对号入座。

知乎的匿名功能，是在非常早期就已经加入的功能，至今问答业务历经各种迭代，匿名架构基本没有大改 ~~改不动~~ ，从现在往回看，可以说当初的匿名系统设计，已经很好满足了产品的发展。但是如果我们能从现在的视角重新匿名系统，也许能做到更好。

## 系统要求

**功能要求**
* 用户可以在问题下使用匿名身份，开启之后用户在该问题的行为（投票、回答、关注问题、点赞）都是匿名
* 启用匿名身份后可以撤销
* 匿名回答之后可以正常收到点赞、评论消息
* 不能邀请别人回答问题
* 即使匿名，每个问题最多回答一次

**非功能要求**
* 不能明文存储匿名信息（即用户 ID）
* 加密的信息，最好是使用单向加密
* 支持多机房，出现网络故障能够降级

**其他要求**
* 已关注页面显示匿名关注的问题（目前知乎没有这个功能）
* 个人的回答页面显示自己的匿名回答（目前知乎也没有这个功能）

## 制约因素
匿名跟问答其实是强绑定关系，由于产品功能的某些限制，例如每个用户在每个问题下最多回答一次、一个回答最多赞同一次。在不直接存储回答用户信息的情况下，实现这样的限制就需要额外的工作了，不过这就属于问答业务这边该考虑的事情。

## 设计
根据功能需求，匿名涉及的实体主要是问题、回答、评论、点赞，凡是开启匿名身份的用户，在涉及这 4 个实体的行为都应该显示为匿名。为了支持撤销，每条记录肯定需要记录 member_id，那么最容易想到的方案就是增加一个字段用于标记是否为匿名，如果是，那么则需要在对外返回信息的时候，把用户信息隐藏掉。这个方案最容易出现的问题是匿名泄露，因为凡是暴露了用户信息的地方，都需要靠代码来保证不会泄露。另外，用户信息没有隐藏或者被加密，数据库一旦泄露，后果非常严重。稍微改进一下这个方案，就是把匿名用户信息进行（对称）加密，在取消匿名的时候，再解密为真实的用户的信息。这个方案依然没有解决数据库泄露的话会暴露匿名用户的问题。

匿名系统，应该抽象出来单独成为一个系统。所有的匿名信息，收拢到匿名系统内部，用户信息应该被单向加密，对数据库等权限进一步收紧，接口调用权限也需要收紧，设置白名单，只提供给有需要的其他系统（例如问答、评论服务）。匿名系统应提供设置、取消和查询匿名等接口，供问答服务调用。

以下是流程概述：
* 当用户启用匿名身份，匿名系统记录下用户及问题 ID，并提供查询接口；
* 当用户使用匿名身份回答问题时，问答服务请求匿名系统，新增加一条用户匿名回答的记录；
* 当用户取消匿名身份的时候，匿名根据用户的匿名记录，再请求问答服务，恢复相应回答的用户信息

为了保证匿名信息始终在匿名系统内部，不提供类似查询某个问题下所有匿名用户的接口。用户信息，在系统内部应该先加密再存到数据库，为了防止被逆向，应该采用单向加密。

## 接口设计
根据设计，匿名系统会暴露以下接口：
1. `set_anonymous(user_id, question_id)`
2. `remove_anonymous(user_id, question_id)`
3. `is_anonymous(user_id, question_id)`
4. `add_anonymous_answer(user_id, question_id, answer_id)`
5. `has_anonymous_answer(user_id, question_id)`

## 数据库设计

**用户在哪些问题下启用匿名身份**
```
CREATE TABLE `anonymous` (
  `id` bigint(20) unsigned NOT NULL,
  `user_hash` varchar(64) unsigned NOT NULL COMMENT '用户哈希串',
  `question_id` bigint(20) unsigned NOT NULL COMMENT '问题 ID',
  `is_deleted` tinyint(1) DEFAULT '0',
  `created` int(11) NOT NULL DEFAULT '0',
  `updated` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `idx_user_id_question_id` (`user_id`, `question_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

**用户在匿名身份下关注了问题**
```
CREATE TABLE `anonymous_follow` (
  `id` bigint(20) unsigned NOT NULL,
  `user_hash` bigint(64) unsigned NOT NULL COMMENT '用户哈希串',
  `question_id` bigint(20) unsigned NOT NULL COMMENT '问题 ID',
  `is_deleted` tinyint(1) DEFAULT '0',
  `created` int(11) NOT NULL DEFAULT '0',
  `updated` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `idx_user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

**用户在匿名身份下回答了问题**
```
CREATE TABLE `anonymous_answer` (
  `id` bigint(20) unsigned NOT NULL,
  `user_hash` bigint(64) unsigned NOT NULL COMMENT '用户哈希串',
  `question_id` bigint(20) unsigned NOT NULL COMMENT '问题 ID',
  `answer_id` bigint(20) unsigned NOT NULL COMMENT '回答 ID',
  `is_deleted` tinyint(1) DEFAULT '0',
  `created` int(11) NOT NULL DEFAULT '0',
  `updated` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `idx_user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

## High Level design
### 如何加密
我们该如何选择加密方法。

首先，加密是单向的，意味着不能反推出 user_id。单向加密的算法有不少，例如最常见的是 MD5 或者 SHA。但是这样还不行，如果数据库和代码（哈希方法）同时泄露，那么攻击者只需要算一遍所有的组合，就知道对应的用户是谁。我们还可以对 user_id 加盐，以及多次哈希，虽然 salt 值也可能会泄露。

为了应对暴力破解，还使用类似 bcrypt 这样慢哈希。假设有 10 亿用户，每个用户需要花 0.1 秒计算，只要 1160 台机器就能在 1 天时间全部计算出来。没有人随便就能有一千台机器，只要愿意花点时间，还是可以破解出来，另外如果每个请求都需要额外 100ms 计算用户哈希，其实很难接受。

### 一致性
在取消匿名的时候，需要请求问答服务，恢复回答、投票等记录的用户信息，然后再把用户在问题下匿名（anonymous_question 表）的记录标记为删除。

这一步需要对多个服务的多张表数据（如果要考虑评论等，会涉及更多）进行修改，为了保证一致性，需要考虑使用分布式事务。实现分布式事务的一个常见协议就是*两阶段提交协议*（2PC），2PC 引入一个协调者的角色，负责统一掌控全部的节点并执行真正的提交，分布式系统中实现一致性的其他协议都是在两阶段提交的基础上做的改进。

另外需要考虑目前知乎有多个机房（一主多从的架构），那么机房之间的数据同步，也是有可能随时中断的。那么中断之后，如何保证机房之间的数据一致性呢？

虽然 CAP 定理听起来是三取其二，可是分区容错性是没有办法选择，那么问题变成了，我们该选择一致性还是可用性呢？大部分业务场景下是可以接受短暂的不一致的，但是匿名这个功能必须保证数据的一致性，所以当系统之间无法通信时，舍弃可用性，选择一致性，这时将不能启用和取消匿名身份，而已经是匿名的数据，则继续显示匿名。

### 产品需求完成度
按照以上的设计，功能性和非功能性要求都能满足，对于其他要求里提到的匿名关注和匿名回答列表，也可以查询到。

在系统可扩展性方面，个人觉得一般，除非产品已经比较稳定，不然每次新的模块接入，匿名系统的改造工作量都不少。

## 容量预估和数据分区
假设有 1 亿活跃用户，平均每个用户每天在 1 个问题下匿名，然后回答了该问题，并且还在匿名的问题下回复了 10 条评论，赞同（或反对） 10 个回答。

按照容量预估，每天将产生 1 亿条数据，如此规模的数据，应该在系统上线前，就规划好如果对数据进行分区存放。我们如何对数据进行分区（sharding）呢？

### 存储
方案一：MySQL + 分库分表
分区的方式选择使用一致性哈希，方便以后扩容。

方案二：TiDB
TiDB 是 PingCAP 公司的开源数据库，兼容 MySQL，支持无限的水平扩展，具备强一致性和高可用性。对于业务，可以透明切换。

### 缓存
略。

## 总结
本文纯粹是在看完《Grokking the System Design Interview》后练手的设计。知乎实际的匿名设计，受到的约束、产品的需求和开发难度要更多更难。

## 参考

* [即使被拖库，也可以保证密码不泄露 - CoderZh Blog](https://blog.coderzh.com/2016/01/10/a-password-security-design-example/)
* [分布式事务的实现原理](https://draveness.me/distributed-transaction-principle)
