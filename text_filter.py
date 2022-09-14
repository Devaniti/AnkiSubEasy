import re

Open_Parentheses_List = "(（["
Closed_Parentheses_List = ")）]"

Substitution_List = [
]

def remove_nested_parentheses(string):
    ret = ''
    skip = 0
    for i in string:
        if i in Open_Parentheses_List:
            skip += 1
        elif i in Closed_Parentheses_List and skip > 0:
            skip -= 1
        elif skip == 0:
            ret += i
    return ret

def filter_text(string):
    string = remove_nested_parentheses(string)
    for substitution in Substitution_List:
        string = re.sub(substitution[0], substitution[1], string)
    return string