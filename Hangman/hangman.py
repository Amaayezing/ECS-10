# Maayez Imam 10/30/17
# Hangman Program


def hangman():
    guesses = 0
    letters_used = ""
    thirty_lines = "\n"
    secret_word = input("Please enter a word to be guessed\nthat does not contain ? or white space: ")
    while '?' in secret_word or ' ' in secret_word:
        secret_word = input("Please enter a word to be guessed\nthat does not contain ? or white space: ")
    print(thirty_lines * 30)
    progress = ["?"] * len(secret_word)
    print(game_progress(guesses, secret_word, progress, guesses))
    print("So far you have guessed: ")

    while guesses < 8:
        guess = input("Please enter your next guess: ")

        if len(guess) > 1 and guess.isalpha():
            print("You can only guess a single character.")
        elif guess.isspace():
            print("You must enter a guess.")
        elif (guess in secret_word) and (guess not in letters_used) and (''.join(progress) != secret_word):
            letters_used += guess
            letters_used = sorted(letters_used)
            #hanged_man(guesses, secret_word)
            print(game_progress(guess, secret_word, progress, guesses))
            print("So far you have guessed: " + ', '.join(letters_used))
        elif (guess not in secret_word) and (guess not in letters_used) and (''.join(progress) != secret_word):
            guesses += 1
            letters_used += guess
            letters_used = sorted(letters_used)
            hanged_man(guesses, secret_word)
            print("".join(progress))
            print("So far you have guessed: " + ', '.join(letters_used))
        elif guess in letters_used:
            print("You already guessed the character: " + guess)
        else:
            print("You correctly guessed the secret word: " + secret_word)
            break

    return secret_word


def hanged_man(guesses, secret_word):
    if guesses == 1:
        print(" |")
    elif guesses == 2:
        print(" |")
        print(" 0")
    elif guesses == 3:
        print(" |")
        print(" 0")
        print(" |")
    elif guesses == 4:
        print(" |")
        print(" 0")
        print("/|")
    elif guesses == 5:
        print(" |")
        print(" 0")
        print("/|\\")
    elif guesses == 6:
        print(" |")
        print(" 0")
        print("/|\\")
        print("/")
    elif guesses == 7:
        print(" |")
        print(" 0")
        print("/|\\")
        print("/ \\")
        print("You failed to guess the secret word: " + secret_word)
        exit(0)


def game_progress(guess, secret_word, progress, guesses):
    i = 0
    while i < len(secret_word):
        if guess == secret_word[i]:
            progress[i] = guess
            i += 1
        else:
            i += 1
    if ''.join(progress) == secret_word:
        print("You correctly guessed the secret word: " + secret_word)
        exit(0)
    hanged_man(guesses, secret_word)

    return "".join(progress)


hangman()
