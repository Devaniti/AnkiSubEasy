import re

Substitution_List = [
  [r"[(（].*?[)）]", ""],
  [r"[\[].*?[\]]", ""]
]

def filter_text(string):
    for substitution in Substitution_List:
        string = re.sub(substitution[0], substitution[1], string)
    return string