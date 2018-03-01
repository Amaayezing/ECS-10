#Maayez Imam 11/20/17
#Most Common Words Program

from collections import Counter


def most_common_word():
    file = input("Enter the name of the file: ")
    find_words(file)
    return file


def find_words(file):
    num_words = int(input("Enter how many top words you want to see: "))
    count = Counter()
    with open(file) as open_file:
        for words in open_file:
            count.update(words.lower().split())
    common = (count.most_common(num_words))
    for (word, count) in common:
        word = str(word).strip(',.:;"|\\!@#$%^&*()_+-=[]{}<>?/~`''')
        print("The following words appeared %d times each: %s" % (count, word))


most_common_word()
