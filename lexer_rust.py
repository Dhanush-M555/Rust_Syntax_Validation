import ply.lex as lex

# List of token names
tokens = (
    'TRUE',
    'LOOP',
    'FALSE',
    'AND',
    'OR',
    'LET',
    'WHILE',
    'NUM',
    'NEQ',
    'LBRACE',
    'RBRACE',
    'ASSIGN',       # Assignment operator =
    'ADD_ASSIGN',   # Addition assignment +=
    'SUB_ASSIGN',   # Subtraction assignment -=
    'MUL_ASSIGN',   # Multiplication assignment *=
    'DIV_ASSIGN',   # Division assignment /=
    'ADDITION',          # Addition operator +
    'SUB',          # Subtraction operator -
    'MUL',          # Multiplication operator *
    'DIV',          # Division operator /
    'MOD',          # Modulus operator %
    'EQUAL',
    'GT',
    'LT',
    'LTE',
    'LPAREN',       # Left parenthesis (
    'RPAREN',
    'GTE',
    'MUT',
    'SEMICOLON',
    'COLON',
    'TYPE',
    'ID',
    'COMMA'
)

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ASSIGN = r'='
t_ADD_ASSIGN = r'\+='
t_SUB_ASSIGN = r'-='
t_MUL_ASSIGN = r'\*='
t_DIV_ASSIGN = r'/='
t_ADDITION = r'\+'
t_SUB = r'-'
t_MUL = r'\*'
t_DIV = r'/'
t_MOD = r'%'
t_AND=r'&&'
t_OR = r'\|\|'
t_TRUE=r'true'
t_FALSE=r'false'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_EQUAL = r'=='
t_NEQ = r'!='
t_LT = r'<'
t_LTE = r'<='
t_GT = r'>'
t_GTE = r'>='
t_COMMA=r','
t_SEMICOLON = r';'
t_COLON = r':'
t_MUT = r'mut'
t_LET = r'let'
t_TYPE = r'i32|i64|f32|f64|bool|char'
t_WHILE=r'while'
t_LOOP=r'loop'
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    if t.type == 'ID' and t.value in reserved.values():
        print(f"Syntax error: '{t.value}' is a reserved word.")
        t.lexer.skip(1)
    return t

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignored characters (whitespace and newline)
t_ignore = ' \t\n'

# Reserved words
reserved = {
    'i32': 'TYPE',
    'i64': 'TYPE',
    'f32': 'TYPE',
    'f64': 'TYPE',
    'bool': 'TYPE',
    'char': 'TYPE',
    'let':'LET',
    'mut':'MUT',
    'while':'WHILE',
    'true':'TRUE',
    'false':'FALSE',
    'loop':'LOOP'
}

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
