digit [0-9]*
id [a-zA-Z][a-zA-Z0-9]*
num [0-9]*\.[0-9]*

%{
%}

%%
int |
float |
char |
double |
void |
main { printf(&quot; \n %s is keyword&quot;,yytext);}

"<=" {printf("\n %s is Relational operator Lessthan or Equal to",yytext);}
"<" {printf("\n %s is Relational operator Lessthan",yytext;}
">=" {printf("\n %s is Relational operator Greaterthan or Equal to",yytext);}
">" {printf("\n %s is Relational operator Greaterthan",yytext);}
"==" {printf("\n %s is Relational operator Equal to",yytext);}
"!=" {printf("\n %s is Relational operator Not Equal to",yytext);}

{id} { printf("\n %s is identifier",yytext); }
{num} { printf("\n %s is float",yytext);}
{digit} {printf("\n %s is digit",yytext);}
%%

int main() {
	yylex();
}

int yywrap() {
	return 1;
}
