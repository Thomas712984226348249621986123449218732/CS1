from PyMultiDictionary import MultiDictionary
dictionary = MultiDictionary()
dictionary.set_words_lang('en')

while True:
    adjective = input("Adjective   : ")

    print(dictionary.meaning('en', adjective))
    if "Adjective" in dictionary. meaning('en', adjective)[0]:
        break

while True:
    noun = input("Noun: ")

    if "Noun" in dictionary.meaning('en', noun)[0]:
        break

print(f"Gah Damn, this is {adjective}. This stuff is {noun}")
