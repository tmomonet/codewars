def to_jaden_case(string):
    stringList = string.split(" ")
    output = []
    for word in stringList:
        word = word[0].upper() + word[1: ].lower()
        output.append(word)
    return " ".join(output)

# Community Solution
# def to_jaden_case(string):
#     return ' '.join(word.capitalize() for word in string.split())
