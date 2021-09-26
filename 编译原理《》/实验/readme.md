# Readme.md

Lab Documentation: https://decaf-lang.github.io/minidecaf-tutorial/
Original Test Cases: https://github.com/decaf-lang/minidecaf-tests
Writing a C Compiler: https://norasandler.com/2017/11/29/Write-a-Compiler.html
Bison Doc: https://www.gnu.org/software/bison/manual/html_node/Complete-Symbols.html


# 实验背景和实验要求
1. 第一个编译器（step0-step1）。我们给的实验框架可以通过所有测试用例，你需要做的事情为跟着文档阅读学习实验框架代码。请各位同学注意，stage0 尤为重要，掌握好实验框架是高质量和高效率完成后续实验的保证。
2. 常量表达式（step2-step4）。在这个 stage 中你将实现常量操作（加减乘除模等）。
3. 变量和语句（step5-step6）。在这个 stage 中你将第一次支持变量声明与赋值，以及条件跳转语句。
4. 块语句和循环（step7-step8）。在这个 stage 中你将支持块语句，所谓块语句，就是多个语句组成一个块，每个块都是一个作用域。作为一种特殊的块语句，你也将实现循环操作。
5. 全局变量和函数（step9-step10）。在这个 stage 中你将支持声明全局变量，并且支持函数的声明和调用。
6. 数组（step11）。在这个 stage 中，你将支持数组，包括全局数组和局部数组。

同时，为了帮助大家通过实验学习语法分析，我们单独设置了一个手工自顶向下语法分析的小实验，需要大家手动实现一个支持 step1 - step6 语法规范的手工 parser。

语法分析？syntax analysis (AST) -> parser (Bison)

# Step 0 
配置环境

# Step 1 仅一个return的main函数
框架已经包括step1的代码，能直接通过step1的testcases和failcases 

## 学习
scanner.l - flex - 词法分析
parser.y - bison - 语法分析


yytext is variable name when you enter anything into compiler (result of lexer), yylval is how you call it  
good intro to flex and bison 
- https://www.oreilly.com/library/view/flex-bison/9780596805418/ch01.html


# Step 2 Unary Operator
需要支持negation -, bitwise not ~, and logical not!
## 学习
precedence? https://www.gnu.org/software/bison/manual/html_node/Precedence.html
by looking at NEG, these are the files we need to update

1. Parser.y - update grammer tree
2. Scanner.l - update tokens to scan for
"~"           { return yy::parser::make_BNOT (loc);     }
"!"           { return yy::parser::make_LNOT (loc);     }
3. translation.cpp - add 
/* Translating an ast::BitNotExpr node.
*/
void Translation::visit(ast::BitNotExpr *e) {
    e->e->accept(this);

    e->ATTR(val) = tr->genBNot(e->e->ATTR(val));
}
4. riscv_md - add cases for emitInstr, such as
case RiscvInstr::BITNOT:
  oss << "not" << i->r0->name << ", " << i->r1->name;
  break;

seqz for NOT

5. type_check
/* Visits an ast::BitNotExpr node.
 *
 * PARAMETERS:
 *   e     - the ast::BitNotExpr node
 */
void SemPass2::visit(ast::BitNotExpr *e) {
    e->e->accept(this);
    expect(e->e, BaseType::Int);

    e->ATTR(type) = BaseType::Int;
}
6. 



# Step 3
             | Expr PLUS Expr
                { $$ = new ast::AddExpr($1, $3, POS(@2)); }
            | Expr MINUS Expr 
                { $$ = new ast::MinusExpr($1, $3, POS(@2)); }
            | Expr TIMES Expr
                { $$ = new ast::TimesExpr($1, $3, POS(@2)); }
            | Expr MOD Expr 
                { $$ = new ast::ModExpr($1, $3, POS(@2)); }