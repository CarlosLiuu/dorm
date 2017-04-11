%{  
#include <stdio.h>  
int lineno=1;  
%}  
  
%%  
  
[^\n]   {yymore();}  
\n  {printf("%1d %s",lineno++,yytext);}  
  
%%  
  
int yywrap(void)  
{  
  return 1;  
}  
  
main()  
{  
  yylex();  
}  