import re

def findAndReplaceInstances(input_string, replacementsList):
    result = input_string
    replacement_index = 0
    
    while "(*)" in result and replacement_index < len(replacementsList):
        result = result.replace("(*)", replacementsList[replacement_index], 1)
        replacement_index += 1
    # todo2: swap (*) to column names to make it order agnostic 
    return result

def replace_placeholders(text, replacements):
    for i, replacement in enumerate(replacements, start=1):
        placeholder = f"[{chr(65 + i)}]"
        text = text.replace(placeholder, replacement)
    return text