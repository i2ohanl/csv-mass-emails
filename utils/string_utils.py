import re

def replace_placeholders(template, replacements_list):
    result = template
    replacement_index = 0
    
    check_placeholder_count(template, len(replacements_list))

    while "(*)" in result and replacement_index < len(replacements_list):
        result = result.replace("(*)", replacements_list[replacement_index], 1)
        replacement_index += 1
    # todo2: swap (*) to column names to make it order agnostic 
    return result

def check_placeholder_count(body_template, data_points):
    placeholders = body_template.count("(*)")
    if placeholders != data_points:
      raise Exception("Template data count mismatch, placeholders: "+str(placeholders)+" data: "+str(data_points))

def replace_placeholder_rows(text, replacements):
    for i, replacement in enumerate(replacements, start=1):
        placeholder = f"[{chr(65 + i)}]"
        text = text.replace(placeholder, replacement)
    return text

