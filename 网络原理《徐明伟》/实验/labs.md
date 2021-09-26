# 编程编程作业

Routing Lab： https://lab.cs.tsinghua.edu.cn/router/doc/requirement/
RIPng for IPv6


# 实验编程
一共包括四个编程实验，
- eui64：基于 EUI64 构造 IPv6 Link Local 地址
- internet-checksum：进行 UDP 和 ICMPv6 的校验和检验和计算
- lookup：路由表的查询
- protocol：RIPng 协议的处理

这都是什么？

# 实验要求
## 必须实现的有：
1. 转发功能，支持直连路由和间接路由，包括 Hop Limit 减一，查表并向正确的 interface 发送出去。
2. 周期性地向所有端口发送 RIPng Response（周期为 5s，而不是 RFC 2080 Section 2.3 Timers 要求的 30s），目标地址为 RIPng 的组播地址。
3. 对收到的 RIPng Request 生成 RIPng Response 进行回复，目标地址为 RIPng Request 的源地址。
4. 实现水平分割（split horizon）和毒性反转（reverse poisoning）。
5. 收到 RIPng Response 时，对路由表进行维护，处理 RIPng 中 metric=16 的情况。
6. 对 ICMPv6 Echo Request 进行 ICMPv6 Echo Reply 的回复，见 RFC 4443 Echo Reply Message。
7. 在接受到 IPv6 packet，按照目的地址在路由表中查找不到路由的时候，回复 ICMPv6 Destination Unreachable (No route to destination)，见 RFC 4443 Section 3.1 Destination Unreachable Message。
8. 在 Hop Limit 减为 0 时，回复 ICMPv6 Time Exceeded (Hop limit exceeded in transit)，见 RFC 4443 Section 3.3 Time Exceeded Message。
9. 在发送的 RIPng Response 大小超过 MTU 时进行拆分。

## 可选实现的有（不加分，但对调试有帮助）：
1. 定期或者在更新的时候向 stdout/stderr 打印最新的 RIP 路由表。
2. 在路由表出现更新的时候立即发送 RIPng Response（完整或者增量），可以加快路由表的收敛速度。
3. 路由的超时（Timeout）和垃圾回收（Garbage Collection）定时器。
4. 程序启动时向所有 interface 发送 RIPng Request。

## 不需要实现的有：
1. NDP 的处理，已经在 HAL 中实现。
2. interface 状态的跟踪（UP/DOWN 切换）。


# 本地测试
pcap格式？