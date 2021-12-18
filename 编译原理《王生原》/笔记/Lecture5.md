# Lecture 5 2021年10月13日

复习

- 单词分析
- 词法分析
- 语法分析

predictive parsing vs recursive descent parsing - https://pediaa.com/what-is-the-difference-between-recursive-descent-parsing-and-predictive-parsing/#:~:text=Difference%20Between%20Recursive%20Descent%20Parsing%20and%20Predictive%20Parsing,predictive%20parsing.%203%20Functionality.%20...%204%20Conclusion.%20

# 自定向下，语法分析

LL(k), k-symbol lookahead into the remaining output

LL(0)? https://stackoverflow.com/questions/5253816/are-there-such-a-thing-as-ll0-parsers

## LL（1）分析

left leftmost lookahead 1

compiler that calculates it - http://hackingoff.com/compilers/ll-1-parser-generator

First 集合, Follow 集合 - https://www.jambe.co.nz/UNI/FirstAndFollowSets.html

预测集合 Predictive Set
