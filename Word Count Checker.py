import re
def word_count(file):
    with(open(file, "r", encoding="utf-8")) as f:
        text = f.read()
    average_word_length = 0
    word_count = 0
    word_length = 0
    char_count = 0
    word = ""
    words = []
    word_frequencies = {}
    for char in text:
        if re.match("[^\s]", char):
            char_count += 1
        if re.match("[\w']", char):
            word_length += 1
            word += char
        else:
            if word_length > 0:
                word_count += 1
                average_word_length = average_word_length+(word_length-average_word_length)/word_count
                words.append(word)

                try:
                    word_frequencies[word] += 1
                except(KeyError):
                    word_frequencies[word] = 1

                word = ""
                word_length = 0
    print("Word count:", word_count)
    print("Average word length:", round(average_word_length, 2))
    print("Character count:", char_count)
    print((sorted(word_frequencies.items(), key=lambda x:x[1], reverse=True))[:10])

if __name__ == "__main__":
    file = input("Please enter the intended file path: ")
    word_count(file)