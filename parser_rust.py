import ply.yacc as yacc
from lexer_rust import tokens

number_of_errors=0

def p_main(p):
    '''main : FN MAIN LPAREN RPAREN LBRACE statements RBRACE'''
def p_statements(p):
    '''statements : declaration statements
                | whileloop statements
                | doloop statements
                | expression statements
                | forloop statements
                | BREAK SEMICOLON statements
                | '''
    
def p_declaration(p):
    '''declaration : LET var_list SEMICOLON
                    | LET MUT var_list SEMICOLON
                    | STATIC ID COLON TYPE ASSIGN exp SEMICOLON
                    | STATIC MUT ID COLON TYPE ASSIGN exp SEMICOLON'''


def p_forconditions(p):
    '''forconditions : ID DOT iterator 
                    | LPAREN ID RPAREN DOT iterator
                    | rangeexpr
                    | LPAREN rangeexpr RPAREN
                    | ID DOT STEPBY LPAREN factor RPAREN
                    | LPAREN ID RPAREN DOT STEPBY LPAREN factor RPAREN
                    | ID
                    | LPAREN rangeexpr RPAREN DOT STEPBY LPAREN factor RPAREN
                    | ID DOT CHARS LPAREN RPAREN
                    | ID DOT BYTES LPAREN RPAREN
                    | LPAREN rangeexpr RPAREN DOT iterator
                '''


def p_forloop(p):
    '''forloop : FOR ID IN forconditions LBRACE statements RBRACE
                | FOR LPAREN ID COMMA ID RPAREN IN LPAREN rangeexpr RPAREN DOT ENUMERATE LPAREN RPAREN LBRACE statements RBRACE
                | FOR LPAREN ID COMMA ID RPAREN IN ID DOT ENUMERATE LPAREN RPAREN LBRACE statements RBRACE
                | FOR LPAREN ID COMMA ID RPAREN IN LPAREN ID RPAREN DOT ENUMERATE LPAREN RPAREN LBRACE statements RBRACE
                | FOR LPAREN ID COMMA ID RPAREN IN ID DOT iterator DOT ENUMERATE LPAREN RPAREN LBRACE statements RBRACE
                | FOR LPAREN ID COMMA ID RPAREN IN LPAREN ID RPAREN DOT iterator DOT ENUMERATE LPAREN RPAREN LBRACE statements RBRACE
                '''

def p_rangeexpr(p):
    '''rangeexpr : factor DOTDOT factor
                | factor DOTDOTEQ factor
                | factor DOTDOT ID DOT LEN LPAREN RPAREN
                | factor DOTDOTEQ ID DOT LEN LPAREN RPAREN
                '''
def p_iterator(p):
    '''iterator : ITER LPAREN RPAREN '''

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
                    | NOT LPAREN conditions RPAREN
                    | TRUE
                    | FALSE
                    | NOT ID
                    | ID 
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
        | factor
        | TRUE
        | FALSE
        '''


def p_whileloop(p):
    '''whileloop : WHILE conditionsp LBRACE statements RBRACE'''


def p_var_list(p):
    '''var_list : ID COLON TYPE
                | ID COLON TYPE COMMA var_list
                | ID COMMA var_list
                | ID ASSIGN exp
                | ID COLON TYPE ASSIGN exp
                | ID COLON TYPE ASSIGN exp COMMA var_list
                | ID COLON LSQRBRACE TYPE SEMICOLON factor RSQRBRACE 
    '''


def p_error(p):
    print(f"\033[91;1m\n\nSyntax error at line {p.lineno}, position {p.lexpos}\033[0m\n\n")
    number_of_errors=number_of_errors+1
    # print(f"Syntax error")

parser = yacc.yacc()
