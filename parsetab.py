
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'programaAMPERSAND BEG_BRACE BEG_PAREN BREAK COLON COMMA CONST DECREMENT DIFFERENT DIVISION ELSE END_BRACE END_PAREN EQUALS EXCLAMATION FALSE FOR FUNC GREATER ID IF IMPORT INCREMENT LESS MINUS MOD NEWLINE NUMBER PACKAGE PIPE PLUS POWER QUOTATION_MARKS RETURN SEMICOLON STRING TIMES TRUE VARprograma : pacote NEWLINE importacao declaracaoGlobal NEWLINE funcoes_codigofuncoes_codigo : funcao delimitador funcoes_codigo\n                      | funcao\n                      | emptyempty :listaGlobal : ID ID EQUALS constante NEWLINE listaGlobal \n                   | ID ID NEWLINE listaGlobal\n                   | ID ID EQUALS constante\n                   | ID ID\n                   | ID ID EQUALS constante NEWLINE\n                   | ID ID NEWLINEdeclaracaoGlobal : VAR ID ID EQUALS constante\n                        | VAR ID ID\n                        | VAR BEG_PAREN listaGlobal END_PAREN\n                        | VAR BEG_PAREN NEWLINE listaGlobal END_PAREN\n                        | emptypacote : PACKAGE IDimportacao : IMPORT ID NEWLINE importacao\n                  | emptyfuncao : FUNC ID BEG_PAREN lista_parametros END_PAREN tipo_retorno BEG_BRACE codigo END_BRACEtipo_retorno : ID\n                    | emptycodigo : lista_estruturaslista_estruturas : lista_estruturas estruturasBase\n                        | emptyestruturasBase : estruturas delimitador\n                      | NEWLINEestruturas : atribuicao\n                  | declaracao\n                  | estrutura_if\n                  | estrutura_for\n                  | unario\n                  | chamadaFuncaodelimitador : NEWLINE\n                   | SEMICOLONexpressao : and\n                 | or\n                 | expressao_n2and : expressao AMPERSAND AMPERSAND expressao_n2or : expressao PIPE PIPE expressao_n2expressao_n2 : equals\n                    | different\n                    | greater\n                    | less\n                    | greater_or_equal\n                    | less_or_equal\n                    | expressao_n3equals : expressao_n2 EQUALS EQUALS expressao_n3different : expressao_n3 DIFFERENT expressao_n3greater : expressao_n2 GREATER expressao_n3less : expressao_n2 LESS expressao_n3greater_or_equal : expressao_n2 GREATER EQUALS expressao_n3less_or_equal : expressao_n2 LESS EQUALS expressao_n3 expressao_n3 : soma \n                     | sub \n                     | expressao_n4 soma : expressao_n3 PLUS expressao_n4sub : expressao_n3 MINUS expressao_n4 expressao_n4 : mult \n                     | div \n                     | mod \n                     | expressao_n5 mult : expressao_n4 TIMES expressao_n5mod : expressao_n4 MOD expressao_n5div : expressao_n4 DIVISION expressao_n5expressao_n5 : unario\n                    | operando unario : negation\n               | incremento\n               | decremento\n               | pre_incremento\n               | pre_decrementonegation : EXCLAMATION operandoincremento : ID INCREMENTpre_incremento : INCREMENT IDdecremento : ID DECREMENTpre_decremento : DECREMENT IDoperando : identificador\n                | constante\n                | chamadaFuncao\n                | expParentesesconstante : NUMBER\n                 | STRING\n                 | TRUE\n                 | FALSEidentificador : IDexpParenteses : BEG_PAREN expressao END_PARENestrutura_for : for_CLIKE\n                     | for_infinito\n                     | for_whilefor_CLIKE : FOR declaracao SEMICOLON expressao SEMICOLON expressao BEG_BRACE codigo END_BRACEfor_infinito : FOR BEG_BRACE codigo END_BRACEfor_while : FOR expressao BEG_BRACE codigo END_BRACEestrutura_if : IF expressao BEG_BRACE codigo END_BRACE estrutura_else\n                    | IF expressao BEG_BRACE codigo END_BRACEestrutura_else : ELSE BEG_BRACE codigo END_BRACE\n                      | ELSE estrutura_ifatribuicao : lista_identificadores EQUALS lista_valores\n                  | expressao_matematica_reduzidaexpressao_matematica_reduzida : assign_plus\n                                     | assign_minus\n                                     | assign_mult\n                                     | assign_divassign_plus : ID PLUS EQUALS expressaoassign_minus : ID MINUS EQUALS expressaoassign_mult : ID TIMES EQUALS expressaoassign_div : ID DIVISION EQUALS expressaodeclaracao : lista_identificadores COLON EQUALS lista_valoreschamadaFuncao : ID BEG_PAREN lista_parametros END_PARENlista_parametros : lista_identificadores\n                        | emptylista_identificadores : lista_identificadores COMMA ID\n                             | IDlista_valores : lista_valores COMMA expressao\n                    | expressao'
    
_lr_action_items = {'PACKAGE':([0,],[3,]),'$end':([1,13,17,18,19,26,27,28,34,62,],[0,-5,-1,-3,-4,-5,-34,-35,-2,-20,]),'NEWLINE':([2,4,5,6,8,9,11,12,15,16,18,21,25,27,28,31,33,36,37,38,39,40,41,48,58,60,61,62,63,64,65,66,67,68,69,70,71,73,75,76,77,78,79,80,81,82,84,85,86,87,92,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,122,123,130,133,134,135,136,137,138,140,159,162,167,169,171,172,173,174,175,176,177,178,179,180,181,182,185,186,187,188,189,190,191,192,194,195,198,199,200,203,204,],[4,-5,-17,-5,-19,13,-16,16,23,-5,27,-13,-18,-34,-35,-14,43,-12,-82,-83,-84,-85,-15,52,-5,65,-25,-20,-24,27,-27,-28,-29,-30,-31,-32,-33,-99,-88,-89,-90,-68,-69,-70,-71,-72,-100,-101,-102,-103,-26,-36,-37,-38,-41,-42,-43,-44,-45,-46,-47,-54,-55,-56,-59,-60,-61,-62,-66,-67,-78,-79,-80,-81,-86,-74,-76,-5,-73,-86,-75,-77,-98,-115,-5,-5,-108,-50,-51,-49,-57,-58,-63,-65,-64,-87,-109,-104,-105,-106,-107,-92,-114,-95,-39,-40,-48,-52,-53,-93,-94,-5,-97,-5,-96,-91,]),'ID':([3,7,10,14,15,20,23,24,27,28,35,43,50,51,52,58,60,61,63,65,74,88,89,90,91,92,93,120,121,130,139,140,144,145,146,147,148,149,150,151,154,155,156,157,158,159,161,164,165,166,168,170,193,198,200,],[5,12,14,21,24,29,24,33,-34,-35,44,24,53,56,24,-5,83,-25,-24,-27,119,132,134,135,136,-26,119,119,44,-5,119,-5,119,119,119,119,119,119,119,119,119,119,119,119,119,-5,119,119,119,119,119,119,119,-5,-5,]),'IMPORT':([4,16,],[7,7,]),'VAR':([4,6,8,16,25,],[-5,10,-19,-5,-18,]),'BEG_PAREN':([10,29,74,83,88,89,93,119,120,132,134,139,144,145,146,147,148,149,150,151,154,155,156,157,158,161,164,165,166,168,170,193,],[15,35,120,121,120,120,120,121,120,121,121,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,]),'FUNC':([13,26,27,28,],[20,20,-34,-35,]),'SEMICOLON':([18,37,38,39,40,62,64,66,67,68,69,70,71,73,75,76,77,78,79,80,81,82,84,85,86,87,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,122,123,128,133,134,135,136,137,138,162,167,169,171,172,173,174,175,176,177,178,179,180,181,182,183,185,186,187,188,189,190,191,192,194,195,199,203,204,],[28,-82,-83,-84,-85,-20,28,-28,-29,-30,-31,-32,-33,-99,-88,-89,-90,-68,-69,-70,-71,-72,-100,-101,-102,-103,-36,-37,-38,-41,-42,-43,-44,-45,-46,-47,-54,-55,-56,-59,-60,-61,-62,-66,-67,-78,-79,-80,-81,-86,-74,-76,158,-73,-86,-75,-77,-98,-115,-108,-50,-51,-49,-57,-58,-63,-65,-64,-87,-109,-104,-105,-106,-107,193,-92,-114,-95,-39,-40,-48,-52,-53,-93,-94,-97,-96,-91,]),'EQUALS':([21,33,37,38,39,40,56,72,78,79,80,81,82,83,94,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,122,123,124,125,126,127,132,133,134,135,136,143,144,145,167,169,171,172,173,174,175,176,177,178,188,189,190,191,192,],[30,42,-82,-83,-84,-85,-112,93,-68,-69,-70,-71,-72,-113,139,143,-41,-42,-43,-44,-45,-46,-47,-54,-55,-56,-59,-60,-61,-62,-66,-67,-78,-79,-80,-81,-86,-74,-76,154,155,156,157,-86,-73,-86,-75,-77,166,168,170,-50,-51,-49,-57,-58,-63,-65,-64,-87,-109,143,143,-48,-52,-53,]),'END_PAREN':([22,32,33,35,37,38,39,40,43,44,45,46,47,48,49,52,56,57,78,79,80,81,82,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,121,122,123,133,134,135,136,152,153,167,169,171,172,173,174,175,176,177,178,188,189,190,191,192,],[31,41,-9,-5,-82,-83,-84,-85,-11,-113,50,-110,-111,-8,-7,-10,-112,-6,-68,-69,-70,-71,-72,-36,-37,-38,-41,-42,-43,-44,-45,-46,-47,-54,-55,-56,-59,-60,-61,-62,-66,-67,-78,-79,-80,-81,-86,-5,-74,-76,-73,-86,-75,-77,177,178,-50,-51,-49,-57,-58,-63,-65,-64,-87,-109,-39,-40,-48,-52,-53,]),'IF':([27,28,58,60,61,63,65,92,130,140,159,196,198,200,],[-34,-35,-5,74,-25,-24,-27,-26,-5,-5,-5,74,-5,-5,]),'FOR':([27,28,58,60,61,63,65,92,130,140,159,198,200,],[-34,-35,-5,88,-25,-24,-27,-26,-5,-5,-5,-5,-5,]),'EXCLAMATION':([27,28,58,60,61,63,65,74,88,92,93,120,130,139,140,144,145,146,147,148,149,150,151,154,155,156,157,158,159,161,164,165,166,168,170,193,198,200,],[-34,-35,-5,89,-25,-24,-27,89,89,-26,89,89,-5,89,-5,89,89,89,89,89,89,89,89,89,89,89,89,89,-5,89,89,89,89,89,89,89,-5,-5,]),'INCREMENT':([27,28,58,60,61,63,65,74,83,88,92,93,119,120,130,132,139,140,144,145,146,147,148,149,150,151,154,155,156,157,158,159,161,164,165,166,168,170,193,198,200,],[-34,-35,-5,90,-25,-24,-27,90,122,90,-26,90,122,90,-5,122,90,-5,90,90,90,90,90,90,90,90,90,90,90,90,90,-5,90,90,90,90,90,90,90,-5,-5,]),'DECREMENT':([27,28,58,60,61,63,65,74,83,88,92,93,119,120,130,132,139,140,144,145,146,147,148,149,150,151,154,155,156,157,158,159,161,164,165,166,168,170,193,198,200,],[-34,-35,-5,91,-25,-24,-27,91,123,91,-26,91,123,91,-5,123,91,-5,91,91,91,91,91,91,91,91,91,91,91,91,91,-5,91,91,91,91,91,91,91,-5,-5,]),'END_BRACE':([27,28,58,59,60,61,63,65,92,130,140,159,160,163,184,198,200,201,202,],[-34,-35,-5,62,-23,-25,-24,-27,-26,-5,-5,-5,185,187,194,-5,-5,203,204,]),'NUMBER':([30,42,74,88,89,93,120,139,144,145,146,147,148,149,150,151,154,155,156,157,158,161,164,165,166,168,170,193,],[37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'STRING':([30,42,74,88,89,93,120,139,144,145,146,147,148,149,150,151,154,155,156,157,158,161,164,165,166,168,170,193,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'TRUE':([30,42,74,88,89,93,120,139,144,145,146,147,148,149,150,151,154,155,156,157,158,161,164,165,166,168,170,193,],[39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'FALSE':([30,42,74,88,89,93,120,139,144,145,146,147,148,149,150,151,154,155,156,157,158,161,164,165,166,168,170,193,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'TIMES':([37,38,39,40,78,79,80,81,82,83,108,109,110,111,112,113,114,115,116,117,118,119,122,123,132,133,134,135,136,172,173,174,175,176,177,178,],[-82,-83,-84,-85,-68,-69,-70,-71,-72,126,149,-59,-60,-61,-62,-66,-67,-78,-79,-80,-81,-86,-74,-76,-86,-73,-86,-75,-77,149,149,-63,-65,-64,-87,-109,]),'DIVISION':([37,38,39,40,78,79,80,81,82,83,108,109,110,111,112,113,114,115,116,117,118,119,122,123,132,133,134,135,136,172,173,174,175,176,177,178,],[-82,-83,-84,-85,-68,-69,-70,-71,-72,127,150,-59,-60,-61,-62,-66,-67,-78,-79,-80,-81,-86,-74,-76,-86,-73,-86,-75,-77,150,150,-63,-65,-64,-87,-109,]),'MOD':([37,38,39,40,78,79,80,81,82,108,109,110,111,112,113,114,115,116,117,118,119,122,123,132,133,134,135,136,172,173,174,175,176,177,178,],[-82,-83,-84,-85,-68,-69,-70,-71,-72,151,-59,-60,-61,-62,-66,-67,-78,-79,-80,-81,-86,-74,-76,-86,-73,-86,-75,-77,151,151,-63,-65,-64,-87,-109,]),'DIFFERENT':([37,38,39,40,78,79,80,81,82,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,122,123,132,133,134,135,136,172,173,174,175,176,177,178,],[-82,-83,-84,-85,-68,-69,-70,-71,-72,146,-54,-55,-56,-59,-60,-61,-62,-66,-67,-78,-79,-80,-81,-86,-74,-76,-86,-73,-86,-75,-77,-57,-58,-63,-65,-64,-87,-109,]),'PLUS':([37,38,39,40,78,79,80,81,82,83,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,122,123,132,133,134,135,136,167,169,171,172,173,174,175,176,177,178,190,191,192,],[-82,-83,-84,-85,-68,-69,-70,-71,-72,124,147,-54,-55,-56,-59,-60,-61,-62,-66,-67,-78,-79,-80,-81,-86,-74,-76,-86,-73,-86,-75,-77,147,147,147,-57,-58,-63,-65,-64,-87,-109,147,147,147,]),'MINUS':([37,38,39,40,78,79,80,81,82,83,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,122,123,132,133,134,135,136,167,169,171,172,173,174,175,176,177,178,190,191,192,],[-82,-83,-84,-85,-68,-69,-70,-71,-72,125,148,-54,-55,-56,-59,-60,-61,-62,-66,-67,-78,-79,-80,-81,-86,-74,-76,-86,-73,-86,-75,-77,148,148,148,-57,-58,-63,-65,-64,-87,-109,148,148,148,]),'GREATER':([37,38,39,40,78,79,80,81,82,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,122,123,132,133,134,135,136,167,169,171,172,173,174,175,176,177,178,188,189,190,191,192,],[-82,-83,-84,-85,-68,-69,-70,-71,-72,144,-41,-42,-43,-44,-45,-46,-47,-54,-55,-56,-59,-60,-61,-62,-66,-67,-78,-79,-80,-81,-86,-74,-76,-86,-73,-86,-75,-77,-50,-51,-49,-57,-58,-63,-65,-64,-87,-109,144,144,-48,-52,-53,]),'LESS':([37,38,39,40,78,79,80,81,82,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,122,123,132,133,134,135,136,167,169,171,172,173,174,175,176,177,178,188,189,190,191,192,],[-82,-83,-84,-85,-68,-69,-70,-71,-72,145,-41,-42,-43,-44,-45,-46,-47,-54,-55,-56,-59,-60,-61,-62,-66,-67,-78,-79,-80,-81,-86,-74,-76,-86,-73,-86,-75,-77,-50,-51,-49,-57,-58,-63,-65,-64,-87,-109,145,145,-48,-52,-53,]),'BEG_BRACE':([37,38,39,40,50,53,54,55,78,79,80,81,82,88,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,122,123,129,132,133,134,135,136,167,169,171,172,173,174,175,176,177,178,188,189,190,191,192,196,197,],[-82,-83,-84,-85,-5,-21,58,-22,-68,-69,-70,-71,-72,130,140,-36,-37,-38,-41,-42,-43,-44,-45,-46,-47,-54,-55,-56,-59,-60,-61,-62,-66,-67,-78,-79,-80,-81,-86,-74,-76,159,-86,-73,-86,-75,-77,-50,-51,-49,-57,-58,-63,-65,-64,-87,-109,-39,-40,-48,-52,-53,198,200,]),'AMPERSAND':([37,38,39,40,78,79,80,81,82,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,122,123,129,132,133,134,135,136,138,141,152,167,169,171,172,173,174,175,176,177,178,179,180,181,182,183,186,188,189,190,191,192,197,],[-82,-83,-84,-85,-68,-69,-70,-71,-72,141,-36,-37,-38,-41,-42,-43,-44,-45,-46,-47,-54,-55,-56,-59,-60,-61,-62,-66,-67,-78,-79,-80,-81,-86,-74,-76,141,-86,-73,-86,-75,-77,141,164,141,-50,-51,-49,-57,-58,-63,-65,-64,-87,-109,141,141,141,141,141,141,-39,-40,-48,-52,-53,141,]),'PIPE':([37,38,39,40,78,79,80,81,82,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,122,123,129,132,133,134,135,136,138,142,152,167,169,171,172,173,174,175,176,177,178,179,180,181,182,183,186,188,189,190,191,192,197,],[-82,-83,-84,-85,-68,-69,-70,-71,-72,142,-36,-37,-38,-41,-42,-43,-44,-45,-46,-47,-54,-55,-56,-59,-60,-61,-62,-66,-67,-78,-79,-80,-81,-86,-74,-76,142,-86,-73,-86,-75,-77,142,165,142,-50,-51,-49,-57,-58,-63,-65,-64,-87,-109,142,142,142,142,142,142,-39,-40,-48,-52,-53,142,]),'COMMA':([37,38,39,40,44,46,56,72,78,79,80,81,82,83,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,122,123,131,132,133,134,135,136,137,138,162,167,169,171,172,173,174,175,176,177,178,186,188,189,190,191,192,],[-82,-83,-84,-85,-113,51,-112,51,-68,-69,-70,-71,-72,-113,-36,-37,-38,-41,-42,-43,-44,-45,-46,-47,-54,-55,-56,-59,-60,-61,-62,-66,-67,-78,-79,-80,-81,-86,-74,-76,51,-113,-73,-86,-75,-77,161,-115,161,-50,-51,-49,-57,-58,-63,-65,-64,-87,-109,-114,-39,-40,-48,-52,-53,]),'COLON':([56,72,83,131,132,],[-112,94,-113,94,-113,]),'ELSE':([187,],[196,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'pacote':([0,],[2,]),'importacao':([4,16,],[6,25,]),'empty':([4,6,13,16,26,35,50,58,121,130,140,159,198,200,],[8,11,19,8,19,47,55,61,47,61,61,61,61,61,]),'declaracaoGlobal':([6,],[9,]),'funcoes_codigo':([13,26,],[17,34,]),'funcao':([13,26,],[18,18,]),'listaGlobal':([15,23,43,52,],[22,32,49,57,]),'delimitador':([18,64,],[26,92,]),'constante':([30,42,74,88,89,93,120,139,144,145,146,147,148,149,150,151,154,155,156,157,158,161,164,165,166,168,170,193,],[36,48,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,]),'lista_parametros':([35,121,],[45,153,]),'lista_identificadores':([35,60,88,121,],[46,72,131,46,]),'tipo_retorno':([50,],[54,]),'codigo':([58,130,140,159,198,200,],[59,160,163,184,201,202,]),'lista_estruturas':([58,130,140,159,198,200,],[60,60,60,60,60,60,]),'estruturasBase':([60,],[63,]),'estruturas':([60,],[64,]),'atribuicao':([60,],[66,]),'declaracao':([60,88,],[67,128,]),'estrutura_if':([60,196,],[68,199,]),'estrutura_for':([60,],[69,]),'unario':([60,74,88,93,120,139,144,145,146,147,148,149,150,151,154,155,156,157,158,161,164,165,166,168,170,193,],[70,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,]),'chamadaFuncao':([60,74,88,89,93,120,139,144,145,146,147,148,149,150,151,154,155,156,157,158,161,164,165,166,168,170,193,],[71,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,]),'expressao_matematica_reduzida':([60,],[73,]),'for_CLIKE':([60,],[75,]),'for_infinito':([60,],[76,]),'for_while':([60,],[77,]),'negation':([60,74,88,93,120,139,144,145,146,147,148,149,150,151,154,155,156,157,158,161,164,165,166,168,170,193,],[78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,]),'incremento':([60,74,88,93,120,139,144,145,146,147,148,149,150,151,154,155,156,157,158,161,164,165,166,168,170,193,],[79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,]),'decremento':([60,74,88,93,120,139,144,145,146,147,148,149,150,151,154,155,156,157,158,161,164,165,166,168,170,193,],[80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,]),'pre_incremento':([60,74,88,93,120,139,144,145,146,147,148,149,150,151,154,155,156,157,158,161,164,165,166,168,170,193,],[81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,]),'pre_decremento':([60,74,88,93,120,139,144,145,146,147,148,149,150,151,154,155,156,157,158,161,164,165,166,168,170,193,],[82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,]),'assign_plus':([60,],[84,]),'assign_minus':([60,],[85,]),'assign_mult':([60,],[86,]),'assign_div':([60,],[87,]),'expressao':([74,88,93,120,139,154,155,156,157,158,161,193,],[95,129,138,152,138,179,180,181,182,183,186,197,]),'and':([74,88,93,120,139,154,155,156,157,158,161,193,],[96,96,96,96,96,96,96,96,96,96,96,96,]),'or':([74,88,93,120,139,154,155,156,157,158,161,193,],[97,97,97,97,97,97,97,97,97,97,97,97,]),'expressao_n2':([74,88,93,120,139,154,155,156,157,158,161,164,165,193,],[98,98,98,98,98,98,98,98,98,98,98,188,189,98,]),'equals':([74,88,93,120,139,154,155,156,157,158,161,164,165,193,],[99,99,99,99,99,99,99,99,99,99,99,99,99,99,]),'different':([74,88,93,120,139,154,155,156,157,158,161,164,165,193,],[100,100,100,100,100,100,100,100,100,100,100,100,100,100,]),'greater':([74,88,93,120,139,154,155,156,157,158,161,164,165,193,],[101,101,101,101,101,101,101,101,101,101,101,101,101,101,]),'less':([74,88,93,120,139,154,155,156,157,158,161,164,165,193,],[102,102,102,102,102,102,102,102,102,102,102,102,102,102,]),'greater_or_equal':([74,88,93,120,139,154,155,156,157,158,161,164,165,193,],[103,103,103,103,103,103,103,103,103,103,103,103,103,103,]),'less_or_equal':([74,88,93,120,139,154,155,156,157,158,161,164,165,193,],[104,104,104,104,104,104,104,104,104,104,104,104,104,104,]),'expressao_n3':([74,88,93,120,139,144,145,146,154,155,156,157,158,161,164,165,166,168,170,193,],[105,105,105,105,105,167,169,171,105,105,105,105,105,105,105,105,190,191,192,105,]),'soma':([74,88,93,120,139,144,145,146,154,155,156,157,158,161,164,165,166,168,170,193,],[106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,]),'sub':([74,88,93,120,139,144,145,146,154,155,156,157,158,161,164,165,166,168,170,193,],[107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,]),'expressao_n4':([74,88,93,120,139,144,145,146,147,148,154,155,156,157,158,161,164,165,166,168,170,193,],[108,108,108,108,108,108,108,108,172,173,108,108,108,108,108,108,108,108,108,108,108,108,]),'mult':([74,88,93,120,139,144,145,146,147,148,154,155,156,157,158,161,164,165,166,168,170,193,],[109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,]),'div':([74,88,93,120,139,144,145,146,147,148,154,155,156,157,158,161,164,165,166,168,170,193,],[110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,]),'mod':([74,88,93,120,139,144,145,146,147,148,154,155,156,157,158,161,164,165,166,168,170,193,],[111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,]),'expressao_n5':([74,88,93,120,139,144,145,146,147,148,149,150,151,154,155,156,157,158,161,164,165,166,168,170,193,],[112,112,112,112,112,112,112,112,112,112,174,175,176,112,112,112,112,112,112,112,112,112,112,112,112,]),'operando':([74,88,89,93,120,139,144,145,146,147,148,149,150,151,154,155,156,157,158,161,164,165,166,168,170,193,],[114,114,133,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,]),'identificador':([74,88,89,93,120,139,144,145,146,147,148,149,150,151,154,155,156,157,158,161,164,165,166,168,170,193,],[115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,]),'expParenteses':([74,88,89,93,120,139,144,145,146,147,148,149,150,151,154,155,156,157,158,161,164,165,166,168,170,193,],[118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,]),'lista_valores':([93,139,],[137,162,]),'estrutura_else':([187,],[195,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> pacote NEWLINE importacao declaracaoGlobal NEWLINE funcoes_codigo','programa',6,'p_programa','analiseSintatica.py',11),
  ('funcoes_codigo -> funcao delimitador funcoes_codigo','funcoes_codigo',3,'p_funcoes_codigo','analiseSintatica.py',15),
  ('funcoes_codigo -> funcao','funcoes_codigo',1,'p_funcoes_codigo','analiseSintatica.py',16),
  ('funcoes_codigo -> empty','funcoes_codigo',1,'p_funcoes_codigo','analiseSintatica.py',17),
  ('empty -> <empty>','empty',0,'p_empty','analiseSintatica.py',21),
  ('listaGlobal -> ID ID EQUALS constante NEWLINE listaGlobal','listaGlobal',6,'p_listaGlobal','analiseSintatica.py',25),
  ('listaGlobal -> ID ID NEWLINE listaGlobal','listaGlobal',4,'p_listaGlobal','analiseSintatica.py',26),
  ('listaGlobal -> ID ID EQUALS constante','listaGlobal',4,'p_listaGlobal','analiseSintatica.py',27),
  ('listaGlobal -> ID ID','listaGlobal',2,'p_listaGlobal','analiseSintatica.py',28),
  ('listaGlobal -> ID ID EQUALS constante NEWLINE','listaGlobal',5,'p_listaGlobal','analiseSintatica.py',29),
  ('listaGlobal -> ID ID NEWLINE','listaGlobal',3,'p_listaGlobal','analiseSintatica.py',30),
  ('declaracaoGlobal -> VAR ID ID EQUALS constante','declaracaoGlobal',5,'p_declaracaoGlobal','analiseSintatica.py',43),
  ('declaracaoGlobal -> VAR ID ID','declaracaoGlobal',3,'p_declaracaoGlobal','analiseSintatica.py',44),
  ('declaracaoGlobal -> VAR BEG_PAREN listaGlobal END_PAREN','declaracaoGlobal',4,'p_declaracaoGlobal','analiseSintatica.py',45),
  ('declaracaoGlobal -> VAR BEG_PAREN NEWLINE listaGlobal END_PAREN','declaracaoGlobal',5,'p_declaracaoGlobal','analiseSintatica.py',46),
  ('declaracaoGlobal -> empty','declaracaoGlobal',1,'p_declaracaoGlobal','analiseSintatica.py',47),
  ('pacote -> PACKAGE ID','pacote',2,'p_pacote','analiseSintatica.py',58),
  ('importacao -> IMPORT ID NEWLINE importacao','importacao',4,'p_importacao','analiseSintatica.py',62),
  ('importacao -> empty','importacao',1,'p_importacao','analiseSintatica.py',63),
  ('funcao -> FUNC ID BEG_PAREN lista_parametros END_PAREN tipo_retorno BEG_BRACE codigo END_BRACE','funcao',9,'p_funcao','analiseSintatica.py',67),
  ('tipo_retorno -> ID','tipo_retorno',1,'p_tipo_retorno','analiseSintatica.py',73),
  ('tipo_retorno -> empty','tipo_retorno',1,'p_tipo_retorno','analiseSintatica.py',74),
  ('codigo -> lista_estruturas','codigo',1,'p_codigo','analiseSintatica.py',79),
  ('lista_estruturas -> lista_estruturas estruturasBase','lista_estruturas',2,'p_lista_estruturas','analiseSintatica.py',84),
  ('lista_estruturas -> empty','lista_estruturas',1,'p_lista_estruturas','analiseSintatica.py',85),
  ('estruturasBase -> estruturas delimitador','estruturasBase',2,'p_estruturasBase','analiseSintatica.py',95),
  ('estruturasBase -> NEWLINE','estruturasBase',1,'p_estruturasBase','analiseSintatica.py',96),
  ('estruturas -> atribuicao','estruturas',1,'p_estruturas','analiseSintatica.py',101),
  ('estruturas -> declaracao','estruturas',1,'p_estruturas','analiseSintatica.py',102),
  ('estruturas -> estrutura_if','estruturas',1,'p_estruturas','analiseSintatica.py',103),
  ('estruturas -> estrutura_for','estruturas',1,'p_estruturas','analiseSintatica.py',104),
  ('estruturas -> unario','estruturas',1,'p_estruturas','analiseSintatica.py',105),
  ('estruturas -> chamadaFuncao','estruturas',1,'p_estruturas','analiseSintatica.py',106),
  ('delimitador -> NEWLINE','delimitador',1,'p_delimitador','analiseSintatica.py',111),
  ('delimitador -> SEMICOLON','delimitador',1,'p_delimitador','analiseSintatica.py',112),
  ('expressao -> and','expressao',1,'p_expressao','analiseSintatica.py',116),
  ('expressao -> or','expressao',1,'p_expressao','analiseSintatica.py',117),
  ('expressao -> expressao_n2','expressao',1,'p_expressao','analiseSintatica.py',118),
  ('and -> expressao AMPERSAND AMPERSAND expressao_n2','and',4,'p_and','analiseSintatica.py',122),
  ('or -> expressao PIPE PIPE expressao_n2','or',4,'p_or','analiseSintatica.py',126),
  ('expressao_n2 -> equals','expressao_n2',1,'p_expressao_n2','analiseSintatica.py',130),
  ('expressao_n2 -> different','expressao_n2',1,'p_expressao_n2','analiseSintatica.py',131),
  ('expressao_n2 -> greater','expressao_n2',1,'p_expressao_n2','analiseSintatica.py',132),
  ('expressao_n2 -> less','expressao_n2',1,'p_expressao_n2','analiseSintatica.py',133),
  ('expressao_n2 -> greater_or_equal','expressao_n2',1,'p_expressao_n2','analiseSintatica.py',134),
  ('expressao_n2 -> less_or_equal','expressao_n2',1,'p_expressao_n2','analiseSintatica.py',135),
  ('expressao_n2 -> expressao_n3','expressao_n2',1,'p_expressao_n2','analiseSintatica.py',136),
  ('equals -> expressao_n2 EQUALS EQUALS expressao_n3','equals',4,'p_equals','analiseSintatica.py',140),
  ('different -> expressao_n3 DIFFERENT expressao_n3','different',3,'p_different','analiseSintatica.py',144),
  ('greater -> expressao_n2 GREATER expressao_n3','greater',3,'p_greater','analiseSintatica.py',148),
  ('less -> expressao_n2 LESS expressao_n3','less',3,'p_less','analiseSintatica.py',152),
  ('greater_or_equal -> expressao_n2 GREATER EQUALS expressao_n3','greater_or_equal',4,'p_greater_or_equal','analiseSintatica.py',156),
  ('less_or_equal -> expressao_n2 LESS EQUALS expressao_n3','less_or_equal',4,'p_less_or_equal','analiseSintatica.py',160),
  ('expressao_n3 -> soma','expressao_n3',1,'p_expressao_n3','analiseSintatica.py',164),
  ('expressao_n3 -> sub','expressao_n3',1,'p_expressao_n3','analiseSintatica.py',165),
  ('expressao_n3 -> expressao_n4','expressao_n3',1,'p_expressao_n3','analiseSintatica.py',166),
  ('soma -> expressao_n3 PLUS expressao_n4','soma',3,'p_soma','analiseSintatica.py',172),
  ('sub -> expressao_n3 MINUS expressao_n4','sub',3,'p_sub','analiseSintatica.py',176),
  ('expressao_n4 -> mult','expressao_n4',1,'p_expressao_n4','analiseSintatica.py',180),
  ('expressao_n4 -> div','expressao_n4',1,'p_expressao_n4','analiseSintatica.py',181),
  ('expressao_n4 -> mod','expressao_n4',1,'p_expressao_n4','analiseSintatica.py',182),
  ('expressao_n4 -> expressao_n5','expressao_n4',1,'p_expressao_n4','analiseSintatica.py',183),
  ('mult -> expressao_n4 TIMES expressao_n5','mult',3,'p_mult','analiseSintatica.py',189),
  ('mod -> expressao_n4 MOD expressao_n5','mod',3,'p_mod','analiseSintatica.py',193),
  ('div -> expressao_n4 DIVISION expressao_n5','div',3,'p_div','analiseSintatica.py',197),
  ('expressao_n5 -> unario','expressao_n5',1,'p_expressao_n5','analiseSintatica.py',201),
  ('expressao_n5 -> operando','expressao_n5',1,'p_expressao_n5','analiseSintatica.py',202),
  ('unario -> negation','unario',1,'p_unario','analiseSintatica.py',206),
  ('unario -> incremento','unario',1,'p_unario','analiseSintatica.py',207),
  ('unario -> decremento','unario',1,'p_unario','analiseSintatica.py',208),
  ('unario -> pre_incremento','unario',1,'p_unario','analiseSintatica.py',209),
  ('unario -> pre_decremento','unario',1,'p_unario','analiseSintatica.py',210),
  ('negation -> EXCLAMATION operando','negation',2,'p_negation','analiseSintatica.py',214),
  ('incremento -> ID INCREMENT','incremento',2,'p_incremento','analiseSintatica.py',218),
  ('pre_incremento -> INCREMENT ID','pre_incremento',2,'p_pre_incremento','analiseSintatica.py',222),
  ('decremento -> ID DECREMENT','decremento',2,'p_decremento','analiseSintatica.py',226),
  ('pre_decremento -> DECREMENT ID','pre_decremento',2,'p_pre_decremento','analiseSintatica.py',230),
  ('operando -> identificador','operando',1,'p_operando','analiseSintatica.py',234),
  ('operando -> constante','operando',1,'p_operando','analiseSintatica.py',235),
  ('operando -> chamadaFuncao','operando',1,'p_operando','analiseSintatica.py',236),
  ('operando -> expParenteses','operando',1,'p_operando','analiseSintatica.py',237),
  ('constante -> NUMBER','constante',1,'p_constante','analiseSintatica.py',241),
  ('constante -> STRING','constante',1,'p_constante','analiseSintatica.py',242),
  ('constante -> TRUE','constante',1,'p_constante','analiseSintatica.py',243),
  ('constante -> FALSE','constante',1,'p_constante','analiseSintatica.py',244),
  ('identificador -> ID','identificador',1,'p_identificador','analiseSintatica.py',248),
  ('expParenteses -> BEG_PAREN expressao END_PAREN','expParenteses',3,'p_expParenteses','analiseSintatica.py',255),
  ('estrutura_for -> for_CLIKE','estrutura_for',1,'p_estrutura_for','analiseSintatica.py',259),
  ('estrutura_for -> for_infinito','estrutura_for',1,'p_estrutura_for','analiseSintatica.py',260),
  ('estrutura_for -> for_while','estrutura_for',1,'p_estrutura_for','analiseSintatica.py',261),
  ('for_CLIKE -> FOR declaracao SEMICOLON expressao SEMICOLON expressao BEG_BRACE codigo END_BRACE','for_CLIKE',9,'p_for_CLIKE','analiseSintatica.py',265),
  ('for_infinito -> FOR BEG_BRACE codigo END_BRACE','for_infinito',4,'p_for_infinito','analiseSintatica.py',269),
  ('for_while -> FOR expressao BEG_BRACE codigo END_BRACE','for_while',5,'p_for_while','analiseSintatica.py',273),
  ('estrutura_if -> IF expressao BEG_BRACE codigo END_BRACE estrutura_else','estrutura_if',6,'p_estrutura_if','analiseSintatica.py',278),
  ('estrutura_if -> IF expressao BEG_BRACE codigo END_BRACE','estrutura_if',5,'p_estrutura_if','analiseSintatica.py',279),
  ('estrutura_else -> ELSE BEG_BRACE codigo END_BRACE','estrutura_else',4,'p_estrutura_else','analiseSintatica.py',289),
  ('estrutura_else -> ELSE estrutura_if','estrutura_else',2,'p_estrutura_else','analiseSintatica.py',290),
  ('atribuicao -> lista_identificadores EQUALS lista_valores','atribuicao',3,'p_atribuicao','analiseSintatica.py',300),
  ('atribuicao -> expressao_matematica_reduzida','atribuicao',1,'p_atribuicao','analiseSintatica.py',301),
  ('expressao_matematica_reduzida -> assign_plus','expressao_matematica_reduzida',1,'p_expressao_matematica_reduzida','analiseSintatica.py',308),
  ('expressao_matematica_reduzida -> assign_minus','expressao_matematica_reduzida',1,'p_expressao_matematica_reduzida','analiseSintatica.py',309),
  ('expressao_matematica_reduzida -> assign_mult','expressao_matematica_reduzida',1,'p_expressao_matematica_reduzida','analiseSintatica.py',310),
  ('expressao_matematica_reduzida -> assign_div','expressao_matematica_reduzida',1,'p_expressao_matematica_reduzida','analiseSintatica.py',311),
  ('assign_plus -> ID PLUS EQUALS expressao','assign_plus',4,'p_assign_plus','analiseSintatica.py',315),
  ('assign_minus -> ID MINUS EQUALS expressao','assign_minus',4,'p_assign_minus','analiseSintatica.py',319),
  ('assign_mult -> ID TIMES EQUALS expressao','assign_mult',4,'p_assign_mult','analiseSintatica.py',323),
  ('assign_div -> ID DIVISION EQUALS expressao','assign_div',4,'p_assign_div','analiseSintatica.py',327),
  ('declaracao -> lista_identificadores COLON EQUALS lista_valores','declaracao',4,'p_declaracao','analiseSintatica.py',331),
  ('chamadaFuncao -> ID BEG_PAREN lista_parametros END_PAREN','chamadaFuncao',4,'p_chamadaFuncao','analiseSintatica.py',338),
  ('lista_parametros -> lista_identificadores','lista_parametros',1,'p_lista_parametros','analiseSintatica.py',342),
  ('lista_parametros -> empty','lista_parametros',1,'p_lista_parametros','analiseSintatica.py',343),
  ('lista_identificadores -> lista_identificadores COMMA ID','lista_identificadores',3,'p_lista_identificadores','analiseSintatica.py',350),
  ('lista_identificadores -> ID','lista_identificadores',1,'p_lista_identificadores','analiseSintatica.py',351),
  ('lista_valores -> lista_valores COMMA expressao','lista_valores',3,'p_lista_valores','analiseSintatica.py',358),
  ('lista_valores -> expressao','lista_valores',1,'p_lista_valores','analiseSintatica.py',359),
]
