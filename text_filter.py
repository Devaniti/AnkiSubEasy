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

# Remove text in parenthesis 
# assuming that parenthesis mainly include names which we don't want to generate cards for
def filter_text(string):
    string = remove_nested_parentheses(string)
    for substitution in Substitution_List:
        string = re.sub(substitution[0], substitution[1], string)
    return string