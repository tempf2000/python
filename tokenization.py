import nltk
from nltk.tokenize import word_tokenize
def tokenize_input(input_text):
    tokens = word_tokenize(input_text)
    return tokens
input_text = "hii my name is Deep"
tokens = tokenize_input(input_text)

print("Input_text:",input_text)
print("Tokens: ",tokens)
