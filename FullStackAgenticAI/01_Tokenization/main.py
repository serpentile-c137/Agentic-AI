import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hey There! My name is Shardul Gore"
tokens = enc.encode(text)

# Tokens [25216, 3274, 0, 3673, 1308, 382, 1955, 597, 361, 79171]
print("Tokens: ", tokens)

decoded = enc.decode([25216, 3274, 0, 3673, 1308, 382, 1955, 597, 361, 79171])
print("Decoded: ", decoded)