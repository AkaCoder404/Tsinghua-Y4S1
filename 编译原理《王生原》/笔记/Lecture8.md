# Lecture 8 2021年11月3日

上次课　
- LR分析基础，　算法，直观的理解，状态，状态机介绍

这次
- 状态机的正式定义，算法，结论（不要求证明）

13.35 移进－规约分析的一个例子
- add a new 文化　(0) S -> E, new language G'[S]
- 期待，状态０, (e, E), (e, E + T), (e, T), (e, T * F), (e, F), (e, (E)), (e, v), (e, d)
状态
1. shift, (v, e) -> has to reduce, reduce 6
2. reduce, (F, e) -> has to reduce, reduce 4
3. reduce, (T, e), (T, *F) -> (T, e) can reduce, (T, *F) ａlso known as 移进归约冲突，　(SLR(1)分析可以解决这个冲突)
4. reduce, (1) -> has to shift
5. shift, (v, e) -> has to reduce, reduce 6
6. reduce, (F, e) -> has to reduce, reduce 4
7. 
8. 
9.
10.
11.
12.
13. reduce, (1), -> meets # and accepts

14.00 状态转移图

14.10 状态分析表
活前缀

14.20 LR(0)的fsm构造















https://www.jianshu.com/p/a400cf1a191e