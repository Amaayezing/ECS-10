#Maayez Imam 10/2/2017
#Capital program

String = str(input('Please enter a string: '))
finalString = ""
Vowels = 'aeiouAEIOU'
# defines what the vowels are, also included capital letters
# Vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'], could also list out vowels but more work

for letter in String:
    if letter in Vowels:
        finalString = finalString + letter.upper()
        # if the letter is defined as a vowel, this capitalizes it
    else :
        finalString = finalString + letter.lower()
        # else (if the letter is not defined as a vowel), make it lower case

print(finalString)
# print out the corresponding string after capitalizing the vowels