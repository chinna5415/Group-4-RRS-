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

"<=" {printf(&quot;\n %s is Relational operator Lessthan or Equal to;,yytext);}
"<" {printf(&quot;\n %s is Relational operator Lessthan;,yytext);}
">=" {printf(&quot;\n %s is Relational operator Greaterthan or Equal to;,yytext);}
">" {printf(&quot;\n %s is Relational operator Greaterthan;,yytext);}
"==" {printf(&quot;\n %s is Relational operator Equal to;,yytext);}
"!=" {printf(&quot;\n %s is Relational operator Not Equal to,yytext);}

{id} { printf(&quot;\n %s is identifier&quot;,yytext); }
{num} { printf(&quot;\n %s is float&quot;,yytext);}
{digit} {printf(&quot;\n %s is digit&quot;,yytext);}
%%

int main() {
	yylex();
}

int yywrap() {
	return 1;
}
