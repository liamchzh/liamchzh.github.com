---
date: 2023-01-13
layout: post
title: "Plaid - Open Banking 的领先者"
description: "过去三年里，我一直使用 beancount 记账。在每个月底，把每个银行账号（包括信用卡）的交易记录导出，通过脚本进行分类整理，最后提交到 GitHub 进行托管。beancount 有很多的好处，例如复式记账方便校验、纯文本纪录方便用 git 管理等等。最近在想有没有方法能够进一步把记账自动..."
categories: [Newsletter]
---

过去三年里，我一直使用 beancount 记账。在每个月底，把每个银行账号（包括信用卡）的交易记录导出，通过脚本进行分类整理，最后提交到 GitHub 进行托管。beancount 有很多的好处，例如复式记账方便校验、纯文本纪录方便用 git 管理等等。最近在想有没有方法能够进一步把记账自动化，结果有朋友提到了 Plaid 这个公司。Plaid 给开发者提供了接口，在用户授权后，开发者可以获取用户的银行存款和交易等记录。这是金融领域一种称为 Open Banking - 开放银行的新兴趋势，该趋势要求银行允许消费者与第三方公司共享其帐户数据。

# Open Banking

> Open banking is a banking practice that provides third-party financial service providers open access to consumer banking, transaction, and other financial data from banks and non-bank financial institutions through the use of application programming interfaces (APIs).

> Open banking is becoming a major source of innovation that is poised to reshape the banking industry. [1]

简单来说，Open Banking（开放银行）就是银行把你的账户数据，例如余额和交易记录，通过 API 的方式提供给第三方平台。开放银行目前在美国、欧洲和拉丁美洲都有成熟的实践，在未来将对银行及其他传统金融服务企业产生深远的影响。

# 商业模式

Plaid 的商业模式很简单，就是通过 API 挣钱。开发者很方便就能注册 Plaid 账号，申请到调用权限然后调用 API 进行测试，但是当开发者基于 API 打造完产品想要服务更多（100+）用户时，那么就要付费才能调用 API。

企业（开发者）并不能通过 Plaid 进行扣款（在银行之间的转账也还在内测），那企业为什么需要用户的银行账户信息？这主要还是因为美国的银行交易太过「落后」，不能实时交易（储蓄账户，非信用卡账户），有时交易往往要等几个工作日，万一记账时用户余额不足，导致交易不成功，那就麻烦了，如果能实时查询用户的余额，则能够避免很多麻烦和风险。Cat Chen 写过一篇博客介绍美国金融机构之间的转账系统 - ACH Transfer 机制，来解释清楚为什么美国的网银转账这么慢。

借助 Plaid 的 API 接口，开发者和金融公司可以更直接地了解用户的账户情况，并帮助用户执行预算或费用管理等操作。因此，美国的转账软件 Venmo、加密货币交易所 Coinbase、以及 Robinhood 等等金融科技公司都是 Plaid 的客户，甚至基于 Plaid 还能做自动记账，例如 YNAB(You Need a Budget)。

# 前景

Venmo、Coinbase 和 Robinhood 等应用程序在疫情期间都出现了惊人的增长，而 Plaid 则可以将这些金融科技的应用程序联系起来，Plaid 称客户数量在 2020 年增长了 60%。

早在 2020 年初 Visa 就宣布有意收购 Plaid，但是收购由于反垄断原因等没有被批准。而在 2021 年四月，Plaid 宣布了 $425 million 的 D 轮融资，目前估值为 $13.4 billion。

围绕银行数据，Plaid 可以做的事情很多，除了上面提到的记账，Plaid 做预算管理和收入证明甚至是信用评估等。