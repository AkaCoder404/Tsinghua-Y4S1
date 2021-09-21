# OS 实验内容

一，应用程序域基本执行环境
二，批处理系统
三，躲到程序域分时多任务
四，地址空间
五，进程即进程管理
六，进程间通信
七，文件系统与I/0重定向
八，拓展实验

lab1 - ch1, ch2, ch3
lab2 - ch5, 
lab3 - ch6
lab4 - ch7
可选 - ch8

uCore-Tutorial-Book 
https://learningos.github.io/uCore-Tutorial-Book/index.html


Problems
1. qemu5.2.0 正常，qemu6.0.0会出生问题
rustbi-qemu是基于qemu5开发的
ucore-tutorial依赖于rustbi-qemu项目，所以建议用qemu5
2. ch3的测试例子里面setpriority应该放在test1里面？
3. 如果想单独测试第一个编程作业可以把setpriority的策列先删掉
4. 把策列分成1 2 3，方便大家测试
5. 参考https://duskmoon314.github.io/os-tutorial-book-2021Autumn
6. ucore代码是纯c的，不要用c
7. ucore在出ch2的正常操作，make user BASE=1 CHAPTER=2 make run 会出现unknown trap 0x5?
8.
