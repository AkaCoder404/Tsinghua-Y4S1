# Lecture 5 2021年10月14日

# Review

周期傅里叶级数展开

非周期的傅里叶变换

周期信号的级数展开和非周期的傅里叶变换能量上对应的，parcavell定义存在的

今天、下周： 连续信号 to 离散信号，前四周对连续信号，时间领域和频率领域，特性

FS/FT - 30% of test


# 采样与量化的概念

采样、抽样 - 时间取得点，记录下来，精确的？如何保留连续信号的特点？

> 采样，吧模拟信号编程数字信号时，每隔一个时间间隔在模拟信号波形上抽取一个幅度值，这称之为采样

no possible way to keep all information of 连续信号

量化，近似的

$T_s$ represents 采样周期，最相邻的采样点之间的距离

# 采样与采样定义

在什么条件下，when can a 连续信号 use a 离散时间样 represent without losing information?

$x_p(t)$

连续傅里叶频谱 -> 离散傅里叶频谱

## Nyquist Theorem

> The Nyquist theorem specifies that a sinuisoidal function in time or distance can be regenerated with no loss of information as long as it is sampled at a frequency greater than or equal to twice per cycle.

why 44.1 instead of 40khz?
