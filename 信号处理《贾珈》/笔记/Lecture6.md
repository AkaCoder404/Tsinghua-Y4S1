# Lecture 6 2021年10月21日

复习：采样与采样定理
Q. 在什么条件可以用离散时间样替代二不丢失原有的信息
A. 频带受限信号！符合抽样定理限定条件，大于2被的

Q. 如何从来纳许时间信号的离散时间样本不失真地回复程原来连续时间信号？
A.

离散在连续上就是一个包？

1. 复习采样，相关的内容左扩展
2. 频域和时域表示离散傅里叶变换

Sa函数on时间域 -> Rectangle频率域
内插：有样本值重建某一函数地过程

- 理想型 工程应用没法用，no way to replicate the 矩形
- 近似的
- Interpolation - process of converting a sampled digital signal to that of a higher sampling rate using various digital filtering techniques, so that the sample values are close to the values of the continous signal at the sample times.

欠采样 Undersampling

- samples a bandpass -filtered signal at a sample rate below its Nyquist rate (twice the upper cutoff frequency), but is still able to reconstruct the signal.

频谱?short for频率谱密度,spectrum

- 是频率的分布曲线

如果ws = 2wm，还不足够 maintain all information
采样之后有抽样？

要求时间域在频率域是带限的、

时间域到频率域，连续到离散，
1. 周期信号，傅里叶级数展开 - 系数ci，F_n, 谐波
2. 非周期信号，傅里叶变换

非周期信号离散化之后的傅里叶变换 -> 周期的
1. 画图
2.

Fn 周期信号 -> FT 非周期信号 ---画图--> FT
|---> 离散化
<----内插----|

第三章 1.离散时间信号傅里叶变换

1.
2. 如何存储有限范围的信号？
