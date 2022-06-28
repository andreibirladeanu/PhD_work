import os
import re

def sorted_alpha(path):
    data = os.listdir(path)
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    sort_data = sorted(data, key=alphanum_key)
    return([x for x in sort_data if x[0]!="."])