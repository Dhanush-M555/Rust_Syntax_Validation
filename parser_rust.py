import ply.yacc as yacc
from lexer_rust import tokens

number_of_errors=0

def p_statements(p):
    '''statements : declaration statements
                | whileloop statements
                | doloop statements
                | expression statements
                | '''
    
def p_declaration(p):
    '''declaration : LET var_list SEMICOLON
                    | LET MUT var_list SEMICOLON'''


def p_factor(p):
    '''factor : ID
            | NUM
    '''

def p_doloop(p):
    '''doloop : LOOP LBRACE statements RBRACE '''

def p_conditionsp(p):
    '''conditionsp : conditions AND conditions
                    | conditions OR conditions
                    | conditions
                    | TRUE
                    | FALSE
                    '''

def p_conditions(p):
    '''conditions : factor GT factor
                | factor LT factor
                | factor GTE factor
                | factor LTE factor
                | factor EQUAL factor
                | factor NEQ factor
                '''

def p_expression(p):
    '''expression : ID ASSIGN exp SEMICOLON
                | ID ADD_ASSIGN exp SEMICOLON
                | ID SUB_ASSIGN exp SEMICOLON
                | ID DIV_ASSIGN exp SEMICOLON
                | ID MUL_ASSIGN exp SEMICOLON
                '''


def p_exp(p):
    '''exp : exp ADDITION exp
        | exp SUB exp
        | exp MUL exp
        | exp DIV exp
        | exp MOD exp
        | LPAREN exp RPAREN
        | factor'''


def p_whileloop(p):
    '''whileloop : WHILE conditionsp LBRACE statements RBRACE'''


def p_var_list(p):
    '''var_list : ID
                | ID COLON TYPE
                | ID COLON TYPE COMMA var_list
                | ID COMMA var_list
    '''


def p_error(p):
    print(f"Syntax error at line {p.lineno}, position {p.lexpos}")
    number_of_errors=number_of_errors+1
    # print(f"Syntax error")

parser = yacc.yacc()
