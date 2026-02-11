import ast
def safe_parse(user_input):
    ast.literal_eval(user_input)
    