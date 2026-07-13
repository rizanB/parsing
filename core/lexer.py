from .ast_nodes import Token, MATH_OPS

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