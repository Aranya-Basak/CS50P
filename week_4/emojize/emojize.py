import emoji

inp = input("Input: ")
out = emoji.emojize(inp, language='alias')
print(f"Output: {out}")
