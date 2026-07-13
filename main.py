from typing import List
from dataclasses import dataclass, astuple

    
MATH_OPS = {
    "+": "PLUS", 
    "-": "MINUS", 
    "*": "MULT", 
    "/": "DIV"
}

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

# TODO: THIS SEEMS UNNECESSARY; TO REFACTOR
def make_tuple_from_token_helper(a: str, b:str) -> tuple:
    return astuple(Token(token_type=a, token_value=b))
    
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
            p = make_tuple_from_token_helper(a="NUM", b=full_digit)
            result.append(p)
            
        elif text[i] in MATH_OPS:
            p = make_tuple_from_token_helper(a=MATH_OPS[text[i]], b=text[i])
            result.append(p)
            i += 1
    return result
tokens = tokenize("1 + 2")
print(tokens)

# print(f"value of first token: {tokens[0][1]}\n")
def parse_tokens(t: List[Token]):
    first_node = Num(value=int(t[0][1]))
    # return first_node
    
    # impl binop and return it
    return BinOp(
        left= Num(value=int(t[0][1])),
        right= Num(value=int(t[2][1])),
        op= t[1][0])
    
print(f"parsing tokens: {parse_tokens(tokens)}")

[('NUM', '1'), ('PLUS', '+'), ('NUM', '2')]