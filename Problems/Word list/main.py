text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
        ["Ephemeral", "lasts", "one", "day", "only"],
        ["Accolade", "is", "an", "expression", "of", "praise"]]

a = int(input())

output_ = [word for lst_ in text for word in lst_ if len(word) <= a]
print(output_)
