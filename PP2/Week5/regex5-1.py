import re

def func(text):
    pattern = r'a+b*'
    if re.fullmatch(pattern, text):
        print("The string matches the pattern.")
    else:
        print("The string does not matches the pattern.")

text = input("Input string: ")
func(text)
