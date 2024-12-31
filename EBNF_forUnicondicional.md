<for-statement> ::= "for" <condition> <block> ;

<condition> ::= <expression> ;

<block> ::= "{" { <statement> } "}" ;

<statement> ::= <assignment> | <expression> | <control-flow> ;

<assignment> ::= <identifier> "=" <expression> ;

<expression> ::= <term> { ("+" | "-" | "*" | "/" | "&&" | "||") <term> } ;

<term> ::= <identifier> | <literal> | "(" <expression> ")" ;

<control-flow> ::= "break" | "continue" ;

<identifier> ::= <letter> { <letter> | <digit> } ;

<literal> ::= <digit> { <digit> } ;

<letter> ::= "a" | "b" | ... | "z" | "A" | "B" | ... | "Z" ;

<digit> ::= "0" | "1" | ... | "9" ;
