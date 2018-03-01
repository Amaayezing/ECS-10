#Raghav Dogra & Maayez Imam 11/13/17
#Fraction Add program


def is_int(num):
    if len(num) == 0:
        return False
    elif num.strip().isdigit():
        return True
    elif num.strip()[0] == '-' and num.strip()[1:].isdigit():
        return True
    else:
        return False


def gcd(a, b):
    if a < b:
        a, b = b, a
    while True:
        r = a % b
        if r == 0:
            return b
        a, b = b, r

def frac_add():
    num1 = "a"
    denom1 = "a"
    while not is_int(num1) or not is_int(denom1) or int(denom1) <= 0:
        str = input("Enter a fraction: ").strip()
        if str.count("/") == 1:
            str = str.split("/")
            num1, denom1 = str
        elif is_int(str):
            num1 = str
            denom1 = "1"
    num1 = int(num1)
    denom1 = int(denom1)

    num2 = "a"
    denom2 = "a"
    while not is_int(num2) or not is_int(denom2) or int(denom2) <= 0:
        str = input("Enter another fraction: ").strip()
        if str.count("/") == 1:
            str = str.split("/")
            num2, denom2 = str
        elif is_int(str):
            num2 = str
            denom2 = "1"
    num2 = int(num2)
    denom2 = int(denom2)

    save_num1 = num1
    save_denom1 = denom1
    save_num2 = num2
    save_denom2 = denom2

    if gcd(denom1, denom2)== 1:
        num1 *= denom2
        num2 *= denom1
        denom1 = denom1 * denom2
        denom2 = denom1
    else:
        temp1 = denom1/gcd(denom1, denom2)
        temp2 = denom2/gcd(denom1, denom2)
        num1 *= temp2
        num2 *= temp1
        denom1 *= temp2
        denom2 *= temp1

    num_final = num1 + num2
    denom_final = denom1
    temp = gcd(num_final, denom_final)
    if (temp != 1):
        num_final /= abs(temp)
        denom_final /= abs(temp)

    print("%s/%s + %s/%s = %s/%s" % (int(save_num1),int(save_denom1),int(save_num2),int(save_denom2),int(num_final),int(denom_final)))


frac_add()