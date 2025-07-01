---
date: 2023-01-07
layout: post
title: "StaffEng - 如何写设计文档（并以 Google 为例）"
description: "在项目开始前，设计文档往往必不可少。设计文档（Design Docs，有的公司也叫 RFC）描述了我们在一个项目中所做的决策和权衡。要完成一个设计文档，需要我们在前期调研和讨论的过程中，把目标、约束、取舍和实现细节等，逐一达成共识，并记录下来。一份好的设计文档，通常针对一个特定的问题，调查了可..."
categories: [Newsletter]
---

在项目开始前，设计文档往往必不可少。设计文档（Design Docs，有的公司也叫 RFC）描述了我们在一个项目中所做的决策和权衡。要完成一个设计文档，需要我们在前期调研和讨论的过程中，把目标、约束、取舍和实现细节等，逐一达成共识，并记录下来。一份好的设计文档，通常针对一个特定的问题，调查了可能的解决方案，并解释了所选方法的细节。

写设计文档的目标包括：

* 及早发现设计问题
* 在团队内达成共识
* 作为内部分享资料和留档（供学习和日后参考）

## 如何开始

Will Larson 给出了几点建议：

* Start from the problem.
* Keep the template simple.
* Gather and review together, write alone.
* Prefer good over perfect.

## 参考模板

Malte Ubl 在 <Design Docs at Google> 中提到，设计文档不一定要非常正式，因为并没有严格的格式要求，最重要的是根据项目实际需要，把需要的内容记录下来即可。

他给出了设计文档中，常见的有用章节并逐一介绍。分别是：

* Context and scope
* Goals and non-goals
* The actual design
    * System-context-diagram
    * APIs
    * Data storage
    * Code and pseudo-code
* Degree of constraint
* Alternatives considered
* Cross-cutting concerns


## 生命周期

一个项目周期，简单来说包括：

设计文档，并不仅仅作用在早期阶段，而是会参与到整个项目周期中来，即使到了中后期，依然会有很多值得记录到文档中去。在 Google，当新人接手一个系统时，第一件事就是看当时的设计文档。

***

阅读更多：
* Writing engineering strategy
* Technical Decision-Making and Alignment in a Remote Culture
* Design Docs, Markdown, and Git
