from profanity_filter import ProfanityFilter

pf = ProfanityFilter()

extra_negative_words = {'en': {}}
with open("five-letter-words-extra-negative.txt", "r") as extra_negative_file:
    words = extra_negative_file.read().splitlines()
    extra_negative_words['en'] = dict.fromkeys(words)

pf.extra_profane_word_dictionaries = extra_negative_words

with open("five-letter-words.txt", "r") as source_file, open("five-letter-words-clean.txt", "w") as clean_file, open("five-letter-words-profane.txt", "w") as profane_file:
    words = source_file.read().splitlines()
    for word in words:
        if pf.is_profane(word):
            profane_file.write(f"{word}\n")
            print(f"Word \'{word}\' is profane or negative. Omitting from the cleaned file.")
        else:
            clean_file.write(f"{word}\n")
