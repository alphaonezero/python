while True:
    vowels = 0
    consonants = 0
    word = input("Type in a word: ").strip()

    for letter in word:
        if letter.lower() in "aeiou":
            vowels = vowels + 1
        elif letter == " ":
            pass
        else:
            consonants = consonants + 1
    else:
        print("There are {} vowels and {} consonants in the word {}.".format(vowels,consonants,word))
