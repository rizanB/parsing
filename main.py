from core import tokenize, parse_tokens

expression = "1 + 2"

def main():
    print(f"input expresion : {expression}")
    
    tokens = tokenize(expression)
    print(f"tokens : {tokens}")

    ast = parse_tokens(tokens)
    print(f"AST: {ast}")

if __name__ == "__main__":
    main()