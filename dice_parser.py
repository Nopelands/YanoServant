from random import randint
import re
from enum import Enum

# token regexes
modifier_regex = re.compile(r"(\-?[0-9]+)$")
dice_roll_regex = re.compile(r"([0-9]+d[0-9]+)$")
operation_regex = re.compile(r"([\-\+])$")


class TokenType(Enum):
    MOD = 1
    DR = 2
    OP = 3


class Token:
    def __init__(self, text: str, token_type: TokenType):
        self.text = text
        self.token_type = token_type


def roll_dice(expression: str) -> [str]:
    result = ["0", ""]
    rolls = ""
    aux = expression.split("d")
    if aux[0] == 0 or aux[1] == 0:
        return ["0", "[0]"]
    else:
        if len(aux[0]) > 6:
            exceeding = int(aux[0]) - 500000
            result[0] = (int(aux[1]) + 1) * (exceeding / 2)
            aux[0] = "500000"
        for i in range(0, int(aux[0])):
            roll = randint(1, int(aux[1]))
            rolls += str(roll) + ", "
            result[0] = str(int(result[0]) + roll)
    result[1] = f"[{rolls[:-2]}]"
    return result


def dice_parser(query_string: str) -> str:
    total = 0
    results = ""
    expression = ""
    tokens = []
    split_string = query_string.split(" ")

    if len(split_string) > 100:
        return "Query is too long"

    for i in split_string:
        if modifier_regex.match(i):
            tokens.append(Token(i, TokenType.MOD))
        elif operation_regex.match(i):
            tokens.append(Token(i, TokenType.OP))
        elif dice_roll_regex.match(i):
            tokens.append(Token(i, TokenType.DR))
        else:
            return f"Unexpected token while parsing: {i}"

    if tokens[0].token_type is not TokenType.OP and tokens[len(tokens) - 1] is not TokenType.OP:
        for i in range(1, len(tokens) - 2):
            if i % 2 == 1 and tokens[i].token_type is not TokenType.OP:
                return "Missing operator while parsing"
            elif i % 2 == 0 and (tokens[i].token_type is not TokenType.DR or tokens[i].token_type is not TokenType.MOD):
                return "Missing operand while parsing"
    else:
        return "Missing operator while parsing"

    for i in tokens:
        if i.token_type is TokenType.MOD or i.token_type is TokenType.OP:
            expression += i.text
        elif i.token_type is TokenType.DR:
            aux = roll_dice(i.text)
            expression += aux[0]
            results += f"{aux[1]}, "

    total = eval(expression)
    response = f"You rolled {total} ({results[:-2]})."
    if len(response) > 2000:
        return f"You rolled {total} (Discrete dice limit exceeded)."
    else:
        return response
