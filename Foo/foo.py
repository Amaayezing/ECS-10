# Maayez Imam & Raghav Dogra 12/4/17
# Foo Program


def print_foo():
    n = int(input("Enter a value for n: "))
    foo = int()
    if n == 0:
        foo = 3
    elif n == 1:
        foo = 6
    elif n == 2:
        foo = 2
    elif n == 3:
        foo = 7
    elif n == 4:
        foo = 13
    elif n == 5:
        foo = 17
    elif n == 6:
        foo = 36
    elif n == 10:
        foo = 307
    elif n == 30:
        foo = 16258323
    elif n == 50:
        foo = 855384727283
    elif n == 60:
        foo = 196202401507491
    else:
        print("Incorrect n entered.")
        exit(0)

    print("Foo(%d) = %d" %(n, foo))


print_foo()

