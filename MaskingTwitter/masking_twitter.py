email = str(input("E: "))
password = str(input("P: "))
ampersan = str('@')
length_email = len(email)


new_email = email.split(ampersan)[0]
for i in range(length_email):
    final_email = new_email.replace(new_email[1:-1], '*')
    i = i + 1
print(final_email)

