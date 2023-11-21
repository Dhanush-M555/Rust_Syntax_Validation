from lexer_rust import lexer
from parser_rust import parser,number_of_errors
try:
    with open("D:/college/AFLL/Rust/var_declaration/input.txt", "r") as file:
        data = file.read()
    lexer.input(data)
    lexer.input(data)
    result = parser.parse(data, lexer=lexer)
    if number_of_errors == 0:
        print("Accepted")
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(f"An error occurred: {e}")


# from lexer_rust import lexer
# from parser_rust import parser

# while True:
#     try:
#         data = input("Enter a Rust variable declaration:")
#         lexer.input(data)
        
#         # Print tokens for debugging
#         # for tok in lexer:
#         #     print(tok)
#         lexer.input(data)
#         result = parser.parse(data, lexer=lexer)
#         if result is not None:
#             print("Accepted")
#     except EOFError:
#         break