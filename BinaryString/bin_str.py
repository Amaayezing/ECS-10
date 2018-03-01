# Raghav Dogra & Maayez Imam 12/4/17
# Binary String Program


def perms(string, output):
    if len(string) == 0:
        print(output)
    else:
        if string[0] == 'X' or string[0] == 'x':
            for i in '01':
                perms(string[1:], output + i)
        else:
            perms(string[1:], output + string[0])


def main():
    value = input('Enter a binary string: ')
    perms(value, '')


main()
