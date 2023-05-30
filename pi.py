text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO

# remove symbols
text = text.replace(",", "")
text = text.replace(".", "")
text = text.replace("\n", " ")
text = text.replace("    ", "")

# list to str
text = list(map(len, text.split(' ')))
text = text[1:-1]
answer = "".join(map(str, text))

print(answer)
