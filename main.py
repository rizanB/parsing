from typing import List
from dataclasses import dataclass, astuple

MATH_OPS = {
    "+": "PLUS", 
    "-": "MINUS", 
    "*": "MULT", 
    "/": "DIV"
}

# expression to parse
expression = "1 + 2"

@dataclass
class Token:
    token_type: str
    token_value: str

@dataclass
class Num:
    value: int

@dataclass
class BinOp:
    left: Num
    op: str
    right: Num 

    
def tokenize(text: str) -> list[Token]:
    result = []
    i = 0
    while i < len(text):
        if text[i] == " ":
            i += 1         
            continue
        elif text[i].isdigit():
            full_digit = ""
            while i < len(text) and text[i].isdigit(): 
                full_digit += text[i]
                i += 1       
            p = Token(token_type="NUM", token_value=full_digit)
            result.append(p)
            
        elif text[i] in MATH_OPS:
            p = Token(token_type=MATH_OPS[text[i]], token_value=text[i])
            result.append(p)
            i += 1
    return result

tokens = tokenize(expression)
print(f"Tokens: {tokens}\n")

# print(f"value of first token: {tokens[0][1]}\n")
def parse_tokens(t: List[Token]):
    first_node = Num(value=int(t[0].token_value))
    # return first_node
    
    # impl binop and return it
    return BinOp(
        left= Num(value=int(t[0].token_value)),
        right= Num(value=int(t[2].token_value)),
        op= t[1].token_type)
    
print(f"parsing tokens: {parse_tokens(tokens)}")

# [('NUM', '1'), ('PLUS', '+'), ('NUM', '2')]