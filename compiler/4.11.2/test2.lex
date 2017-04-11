%{  
#include <stdio.h>  
%}  
id auto|double|int|struct|break|else|long|switch|case|enum|register|typedef|char|extern|return|union|const|float|short|unsigned|continue|for|signed|void|default|goto|sizeof|volatile|do|if|while|static  
%%  
{id} {  
 int i;  
 for(i=0;i<yyleng;i++)  
 {  
   if(yytext[i]>='a'&&yytext[i]<='z')  
       printf("%c",yytext[i]+'A'-'a');  
    else  
       printf("%c",yytext[i]);    
 }  
}  
%%  
int yywrap(void)  
{  
  return 1;  
}  
  
main()  
{  
  yylex();  
}  