from typing import List
from .ast_nodes import Token, BinOp, Num

def parse_tokens(t: List[Token]):
    # first_node = Num(value=int(t[0].token_value))
    # return first_node
    
    # impl binop and return it
    return BinOp(
        left= Num(value=int(t[0].token_value)),
        right= Num(value=int(t[2].token_value)),
        op= t[1].token_type)