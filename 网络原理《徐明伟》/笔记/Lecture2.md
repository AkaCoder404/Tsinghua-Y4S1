# Lecture 2 2021年9月18日


# 计算机网络的定义

一批独立在自治的计算机系统的互联集合体
重点是研究“计算机”的联网

互联网的组成，有两级

- 资源子网（服务器，客户计算机）
- 通信子网（通信设备，路由器，hub，等等）
  - 基本通信方式（交换时通信，广播是通信）

网络的构成

- 居于望楼，成语网络，光宇网络

# 计算机网络体系结构

功能的角度来描述网络，层次和层间关系的集合

不定义协议的实现细节和各层协议之前的接口关系

- 功能的角度来学习，功能来分层 -》协议的分层 -》 体系结构的分层

## 计算机网络功能的分层

基本功能是为地理位置不同的计算机用户之间提供访问通路

## 协议和协议的分层结构

计算机网络同等层次中，通信双方进行信息交换是必须遵守的规则
目的主机第N层收到的报文域源主机第N层发出的报文相同
add/remove headers when sending/recieving packets
另据层之间都有一个interface，它定义了下层向上层提供的原语操作和服务

## 计算机网络的体系结构

SAP Service Access Point

- 每一个SAP有唯一的识别地址（比如80是HTTPS）

SDU Service Data Unit

IDU Interface Data Unit

PDU Protocol Data Unit

- PDU = PCI (Protocol Control Information) + SDU

服务分类和服务原语primatives

- 面向连接的服务
- 无连接服务
- 无连接并不意味可靠，可靠要通过确认，重传等机制来保证

## 分层原则

Layering?

1. Advantages - modularity, abstract functionality, reuse （(比如，微信，QQ都可以用下层的TCP)
2. Disadvantages - information hiding - inefficient implementations （上层看不见下层的内部

## 端对端原则

End to End Argument

- 把新功能放在底层iff不影响本层气态的动能、应用
- implementing a functionality at a lower level should have minimum performancei mpact on the application that do not use that functionality

1983年ISO的OSI模型正式成为国际标准

1. 物理层
2. 数据链路层
3. 网络层(computer to computer)
4. 传输层(进程 to 进程)
