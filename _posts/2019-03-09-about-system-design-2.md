---
date: 2019-03-09
layout: post
title: System Design 2 - Everything You Need to Know about
description: "In this article, we’ll go through Load Balancing, Caching, Data Partitioning, Indexes, Replication and Consistent Hashing. These are the basics that you need to know about system design."
categories: [Tech]
---

Whenever we are designing a large system, we need to consider a few things:
1. What are the different architectural pieces that can be used?
2. How do these pieces work with each other?
3. How can we best utilize these pieces: what are the right tradeoffs?

In this article, we’ll go through Load Balancing, Caching, Data Partitioning, Indexes, Replication and Consistent Hashing. These are the basics that you need to know about system design.

## Key Characteristics of Distributed Systems
Before diving into a specific section, we’ll discuss the key characteristics of distributed system including Scalability, Reliability, Availability and Manageability.

**Scalability** is the capability of a system, process, or a network to grow and manage increased demand. Any distributed system that can continuously evolve in order to support the growing amount of work is considered to be scalable.

Horizontal scaling means that you can add more servers while Vertical scaling means that you scale by replacing the existing servers with more powerful machine(CPU, RAM, Storage, etc.)

**Reliability** represents one of the main characteristics of any distributed system. A distributed system is considered reliable if it keeps delivering its services even when one or several of its software or hardware components fail.

**Availability** is the time a system remains operational to perform its required function in a specific period.

**Manageability**, which is another important consideration while designing a distributed system is how easy it is to operate and maintain, is the simplicity and speed with which a system can be repaired or maintained.

## Load Balancing
LB helps to spread the traffic across a cluster of servers to improve responsiveness and availability of applications, websites or databases. LB also keeps track of the status of all the resources while distributing requests.

By balancing application requests across multiple servers, a load balancer reduces individual server load and prevents any one application server from becoming a single point of failure.

There is a variety of load balancing methods:
* Least Connection Method
* Least Response Time Method
* Least Bandwidth Method
* Round Robin Method
* Weighted Round Robin Method
* IP Hash

The load balancer can be a single point of failure; to overcome this, a second load balancer can be connected to the first to form a cluster.

## Caching
Caches take advantage of the locality of reference principle: recently requested data is likely to be requested again.

Placing a cache directly on a request layer node enables the local storage of response data. Each time a request is made to the service, the node will quickly return local cached data if it exists. If it is not in the cache, the requesting node will query the data from disk.

### Cache Invalidation:

* **Write-through cache**: Data is written into the cache and the corresponding database at the same time. when a read is done, main memory can always reply with the requested data.
* **Write-around cache**: This technique is similar to write through cache, but data is written directly to permanent storage, bypassing the cache. This can reduce the cache being flooded with write operations that will not subsequently be re-read, but has the disadvantage that a read request for recently written data will create a “cache miss” and must be read from slower back-end storage and experience higher latency.
* **Write-back cache**: Under this scheme, data is written to cache alone and completion is immediately confirmed to the client. The write to the permanent storage is done after specified intervals or under certain conditions.

Cache eviction policies:
* FIFO
* LIFO
* LRU
* MRU
* Least Frequently Used (LFU)
* Random Replacement (RR)

## Data Partitioning
It is the process of splitting up a DB/table across multiple machines to improve the manageability, performance, availability, and load balancing of an application.

### Partitioning Methods
1. Horizontal partitioning: This schema split rows into different tables. But the key problem with this approach is that if the value whose range is used for sharding isn’t chosen carefully, then the partitioning scheme will lead to unbalanced servers.
2. Vertical Partitioning: In this scheme, we divide our data to store tables related to a specific feature in their own server.
3. Directory Based Partitioning: We can also create a lookup service which knows your current partitioning scheme and abstracts it away from the DB access code.

Partitioning Strategy:
* Key or Hash-based partitioning
* List partitioning
* Round-robin partitioning
* Composite partitioning

### Common Problems of Sharding

Most of these constraints are due to the fact that operations across multiple tables or multiple rows in the same table will no longer run on the same server.

* Joins and Denormalization
* Referential integrity
* Rebalancing

## Proxies
A proxy server is an intermediate server between the client and the back-end server. Proxies are used to filter requests, log requests, or sometimes transform requests. Another advantage of a proxy server is that its cache can serve a lot of requests. 

### Proxy Server Types
1. Open Proxy: An open proxy is a proxy server that is accessible by any Internet user. Generally, a proxy server only allows users within a network group (i.e. a closed proxy) to store and forward Internet services such as DNS or web pages to reduce and control the bandwidth used by the group. With an open proxy, however, any user on the Internet is able to use this forwarding service. 
2. Reverse Proxy: A reverse proxy retrieves resources on behalf of a client from one or more servers. These resources are then returned to the client, appearing as if they originated from the proxy server itself.

## SQL vs. NoSQL
There are two main types of solutions: SQL and NoSQL (also known relational databases and non-relational databases). 

Relational databases are structured and have predefined schemas like phone books that store phone numbers and addresses. Non-relational databases are unstructured, distributed, and have a dynamic schema like file folders that hold everything.

### NoSQL
Following are the most common types of NoSQL:
1. Key-value Stroes
2. Document Databases
3. Wide-column Databases
4. Graph Databases

### High level differences between SQL and NoSQL
**Storage**: SQL stores data in tables where each row represents an entity and each column represents a data point about that entity. NoSQL databases have different data storage models. The main ones are key-value, document, graph, and column-based.

**Schema**: In SQL, each record conforms to a fixed schema, meaning the columns must be decided and chosen before data entry and each row must have data for each column. In NoSQL, schemas are dynamic.

**Querying**: SQL databases use SQL (structured query language) for defining and manipulating the data. In a NoSQL database, queries are focused on a collection of documents. Sometimes it is also called UnQL (Unstructured Query Language). Different databases have different syntax for using UnQL.

**Scalability**: In most common situations, SQL databases are vertically scalable, i.e., by increasing the memory or CPU of the hardware, which can get very expensive. On the other hand, NoSQL databases are horizontally scalable, meaning we can add more servers easily in our NoSQL database infrastructure to handle a lot of traffic.

**Reliability or ACID Compliance**: The vast majority of relational databases are ACID compliant. When it comes to data reliability and safe guarantee of performing transactions, SQL databases are still the better bet.

### Which one to use?
Reasons to use SQL database:
1. If you have to ensure ACID compliance
2. If your data is structured and unchanging

Reasons to use NoSQL database:
1. Storing large volumes of data
2. If you want rapid development

## References
* [Grokking the System Design Interview](https://www.educative.io/collection/5668639101419520/5649050225344512)
* [system-design-primer](https://github.com/donnemartin/system-design-primer) 
* [caching - Write-back vs Write-Through](https://stackoverflow.com/questions/27087912/write-back-vs-write-through)
