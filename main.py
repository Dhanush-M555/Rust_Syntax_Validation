from lexer_rust import lexer
from parser_rust import parser,number_of_errors
try:
    with open("D:/college/AFLL/Rust/Rust_Syntax_Validation/testcases/testcase3.rs", "r") as file:
        data = file.read()
    lexer.input(data)
    lexer.input(data)
    result = parser.parse(data, lexer=lexer)
    try:
        if number_of_errors == 0:
            print("\033[92m\n\nAccepted \nNO SYNTAX ERROR!\n\n\033[0m")
    except Exception as e:
        print("\033[91;1m\n\nSyntax Error TRY AGAIN\n\n\033[0m")
except FileNotFoundError:
    print("\033[91;1mFile not found.\033[0m")
except Exception as e:
    print(f"\033[91;1mAn error occurred: {e}\033[0m")
