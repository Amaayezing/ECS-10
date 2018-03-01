#Maayez Imam 10/18/17
#Cipher Program


def mod(string, shift_amount):
    return (string + shift_amount) % 26


def cipher():
    final_string = ""
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    initial_string = input("Please enter a string to be ciphered: ")
    shift = int(input("Please enter a shift amount between 0 and 25: "))

    while shift < 0 or shift > 25:
        shift = int(input("Please enter a shift amount between 0 and 25: "))

    for i in initial_string:

        if i in alphabet_upper:
            new_string = ord(i) - ord('A')
            newer_string = mod(new_string, shift)
            letter = chr(ord('A') + newer_string)

        elif i in alphabet_lower:
            new_string = ord(i) - ord('a')
            newer_string = mod(new_string, shift)
            letter = chr(ord('a') + newer_string)

        else:
            letter = i
        final_string = final_string + letter

    print("%s" % final_string)


cipher()

# initial_string = input("Please enter a string to be ciphered: ")
# shift = int(input("Please enter a shift amount between 0 and 25: "))
#
#
# def cipher(string_initial, shift_amount):
#     space = ""
#     for char in string_initial:
#         if char.isalpha():
#             alphabet = ord(char) + shift_amount
#             if alphabet > ord('z'):
#                 alphabet -= 26
#             final_string = chr(alphabet)
#         space += final_string
#     print(space)
#     return space
#
#
# cipher(initial_string, shift)
#
#
# # initial_string = input("Please enter a string to be cipehered: ")
# # shift = int(input("Please enter a shift amount between 0 and 25: "))
# #
# #
# # def cipher(initial_string, shift):
# #     new_string = list(initial_string)
# #     for i, char in enumerate(new_string):
# #         new_string[i] = chr((ord(char) + shift) % 26)
# #         final_string = str(new_string)
# #         print(final_string)
# #         return final_string
# #
# #
# # cipher(initial_string, shift)