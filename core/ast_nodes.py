from dataclasses import dataclass

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

   