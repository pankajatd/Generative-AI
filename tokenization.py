import tiktoken
encoder=tiktoken.encoding_for_model("gpt-4o") 
print("Vocalubary size:",encoder.n_vocab)

text="hello, how are you?"
tokens=encoder.encode(text)
print("Tokens:",tokens)

"""
decoded_text=encoder.decode(tokens)
print("Decoded text:",decoded_text)
"""

"""
To find the Decoded text for an Individual token

"""
decoded_text=encoder.decode([24912])
print("Decoded text:",decoded_text)





