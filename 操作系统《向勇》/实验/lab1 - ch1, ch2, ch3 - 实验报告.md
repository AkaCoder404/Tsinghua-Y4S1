# ch1

## 实验目的

1. 结合实验指导书，掌握代码基本结构
2. 读懂os/kernel.ld和Makefile
3. make debug,自学gdb调试的方式

## 问答作业

1. 请学习gdb调用工具的使用（这对后续调试很重要），并通过gdb简单跟踪从机器加电到跳转到0x80200000的简单过程，就需要描述重要跳转即可，就需要描述上qemu的情况。

首先我们用gdb看汇编，最开头0x1000那四五个执行

```shell
$ make debug
0x0000000000001000 in ?? ()
Breakpoint 1 at 0x1000
(gdb) ni
0x0000000000001004 in ?? ()
1: x/12i $pc-8
   0xffc:	unimp
   0xffe:	unimp
   0x1000:	auipc	t0,0x0				# add upper immediate to pc
=> 0x1004:	addi	a1,t0,32			# add immediate
   0x1008:	csrr	a0,mhartid			# control status register read machine hardware thread id to a0
   0x100c:	ld	t0,24(t0)
   0x1010:	jr	t0
   0x1014:	unimp
   0x1016:	unimp
   0x1018:	unimp
   0x101a:	0x8000
   0x101c:	unimp
(gdb) 




```

0x80000000以后可直接看rustbi的源代码，不看gdb汇编了

# ch2

## 实验目的

## 问道作业
