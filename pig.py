def pig_it(text):
    words = text.split()
    pig_words = []
    for word in words:
        if word.isalpha():
            pig_word = word[1:] + word[0] + "ay"
        else:
            pig_word = word
        pig_words.append(pig_word)
    return " ".join(pig_words)


print(pig_it("O tempora o mores !"))