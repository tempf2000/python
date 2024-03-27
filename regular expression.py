import re
def generate_regex_from_grammar(grammar):
    regex_dict = {}

    for rule in grammar:
        non_terminal, production = rule.split(' -> ')
        if non_terminal not in regex_dict:
            regex_dict[non_terminal] = set()

        for symbol in production.split('|'):
            if symbol.isalpha() and len(symbol) == 1:
                regex_dict[non_terminal].add(re.escape(symbol))

            else:
                regex_dict[non_terminal].add(symbol)

    for non_terminal, expressions in regex_dict.items():
        regex_dict[non_terminal] = '|'.join(expressions)

    return regex_dict


grammar = [
    "S -> aA|bB",
    "A -> a|cA",
    "B -> b|d"
]

regex_dict = generate_regex_from_grammar(grammar)

for non_terminal, regex in regex_dict.items():
    print(f"{non_terminal} -> {regex}")
