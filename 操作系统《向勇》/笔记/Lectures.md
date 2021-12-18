# Lecture 1  2021年9月14

Introduction to Class

# Lecture 2 2021年9月17日

中断，异常域系统调用

我们可以在应用程序中直接调用内核的函数吗？不能
我们可以在内核中使用应用程序普通的函数调用码？不能

内核不能直接用用户态的堆栈，需要自己的堆栈

为什么需要先 open(file)，然后才能read？

- 缓存优势，因为CPU速度越快，所以读数据的时候就很快乐
- 文件是内核态的数据(not official reason)

什么是隔离？强制隔离可以避免对整个系统的可用性、可靠性、安全影响

虚拟内存

- 页表 only changed by 操作系统
- 快表 TLB， Virtual Address - TLB - Physical Address

RISC-V easiest/shortest to read documentation
系统模式

- M模式
- S模式

CSR 空置状态寄存器

M模式

- 如果S态try to访问M态,发生异常

# Lecture 3 2021年9月18日

# 进程域调度

进程 - 程序的执行过程，执行的时候分配ID，进程状态

> 进程是只一个具有一定独立功能的程序在一个数据集合上的一次动态执行过程

- 进程包含了正在运行的一个程序的所有状态信息，包括：代码，数据，状态寄存器，通用寄存器，进程占用系统资源

进程地址空间

- 栈
- 堆

进程的控制块PCB

1. 每一个程序执行时，会创建一个PCB

- 进程创建 -> 生成该进程的PCB

# 处理机调度

不同调度算法

- 进程切换有开销的，需要八寸当前进程在PCB中的执行上下文，回复下一个进程的执行上下文

处理机调度？什么时候需要做调度？

- 就绪中的进程选一个进程来运行
- 运行结束出的arrow来调度

先来先服务算法？

## 同步胡扯域进程间通信

协调
并发进程的正确性

- 独立进程，不和其他进程共享资源火状态
- 并发进程

原子操作（Atomic Operation）？
指一次不存任何中断或失败的操作

临界区 （Critical Section）
只能有一个进程进入临界区
实现方法？

- 禁用中断 - 没有中断，没有赏析文切换，因此没有并发

进程通信 IPC Inter-Process Communication

1. 间接通信
2. 直接通信 send、recieve，需要一个共享的空间

# Lecture 4 2021年9月24日

# 存储管理

存储技术比较多，图灵自带能存储所有信息，但是计算机不养

- 计算机有很多地方可以存，考虑不同的问题，比如性能，速度，成本
- 最复杂的

虚拟存储：

- 外排序，如果空间不够，需要把程序分成小的部分，一个一个排
- 如果代码太多了，把一部分程序放到内存里面，把不用的扔出去

文件系统

- 硬盘数据 - 多数情况上一块一块读，然后从块选择，需要保存文件内容一直在，需要用户来read/write名字

## 计算机系统结构

CPU - 能用代码来优化，

- 应该和CPU的地址一样
  I/O设备

MMU （硬件，CPU，L1和L2）vs 操作系统 （内存和外存）

重定位 - relocate code to somewhere else, let others deal with it
分段 -
分页 - 内存分配时，每一个分片分一页，但是页面多大，多少问题，但是可以标准的砖头，把分片连起来
虚拟存储 - 如何组合这些空间，常用的放在内存，不用的内存

实现依赖硬件

## 空间分配

地址空间和地址生成 - 海报例子，如何plan文章的placement，cpu，mmu，alu，和硬件功能
操作系统 - 逻辑地址和物理地址的转换
TLB

## 虚拟存储

RISCV SV39 - represents 512 size

# Lecture 5 2021年9月28日

逻辑地址vs物理地址？

> **Virtual address**: The address you use in your programs, the address that your CPU use to fetch data, is not real and gets translated via MMU to some physical address; everyone has one and its size depends on your system(Linux running 32-bit has 4GB address space)
>
> **Physical address** : The address you'll never reach if you're running on top of an OS. It's where your data, regardless of its virtual address, resides in RAM. This will change if your data is sent back and forth to the hard disk to accommodate more space for other processes.

page vs frame?

> Physical memory is organized into PAGE FRAMES. The size of a page frame is a power of 2 in bytes and varies among systems.
>
> Logical memory is organized into PAGES. The size of page matches a page frame.
>
> A logical address is divided into a page selector and an offset into the page.
>
> Logical pages are mapped to page frames using page tables. The structure of a page table varies among systems. The pages selector of a logical address serves as an index into a page table.
>
> In most systems, the page tables can specify valid logical addresses that have no associated page frame. This is a virtual memory system. If an application attempt to access such a page, it triggers a page fault exception. The operating system page fault handler must allocate a physical page frame, load the page frame using data from secondary storage, update the page table to map the logical page to the newly allocated physical page frame, and finally restart the instruction that caused the fault.
>
> The operating system manages the page tables. The CPU (transparently to the application) translates logical page frames into physical page frames using the page table.

slab？

快表TLB？

page table: 多级页表 vs 反值页表

# Lecture 6 2021年10月4日

局部性原理

- 虚拟存储的需求背景
- 局部性原理

覆盖和交换

虚拟也是存储

RISCV缺页异常 （重点）
