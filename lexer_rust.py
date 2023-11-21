import ply.lex as lex

tokens = (
    'NOT',
    'BREAK',
    'FN',
    'MAIN',
    'LSQRBRACE',
    'RSQRBRACE',
    'CHARS',
    'BYTES',
    'STEPBY',
    'ITER',
    'STATIC',
    'IN',
    'LEN',
    'ENUMERATE',
    'DOTDOT',
    'DOTDOTEQ',     
    'DOT',
    'FOR',
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
    'ASSIGN',
    'ADD_ASSIGN',
    'SUB_ASSIGN',
    'MUL_ASSIGN',
    'DIV_ASSIGN',
    'ADDITION',
    'SUB',
    'MUL',
    'DIV',
    'MOD',
    'EQUAL',
    'GT',
    'LT',
    'LTE',
    'LPAREN',
    'RPAREN',
    'GTE',
    'MUT',
    'SEMICOLON',
    'COLON',
    'TYPE',
    'ID',
    'COMMA'
)

# t_LSQRBRACE=r'['
# t_RSQRBRACE=r']'
t_BREAK=r'break'
t_NOT=r'!'
t_FN=r'fn'
t_MAIN=r'main'
t_LSQRBRACE = r'\['
t_RSQRBRACE = r'\]'
t_STATIC=r'static'
t_CHARS=r'chars'
t_LEN=r'len'
t_BYTES=r'bytes'
t_FOR=r'for'
t_IN=r'in'
t_ENUMERATE=r'enumerate'
t_STEPBY=r'step_by'
t_DOT = r'\.'
t_DOTDOT = r'\.\.'
t_DOTDOTEQ = r'\.\.='
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
t_TYPE = r'i32|i64|u8|u16|u32|u64|f32|f64|char|bool'
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
    'loop':'LOOP',
    'u8':'TYPE',
    'u16':'TYPE',
    'u32':'TYPE',
    'u64':'TYPE',
    'in':'IN',
    'for':'FOR',
    'static':'STATIC',
    'chars':'CHARS',
    'iter':'ITER',
    'enumerate':'ENUMERATE',
    'len':'LEN',
    'step_by':'STEPBY',
    'fn':'FN',
    'main':'MAIN',
    'break':'BREAK'
}


def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
