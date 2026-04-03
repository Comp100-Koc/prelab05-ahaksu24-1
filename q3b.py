def add_binary(a, b):
    '''
    Given two strings perform binary addition and return the result as a string
    '''
    a = a[2:]
    b = b[2:]

    i = len(a) - 1
    j = len(b) - 1
    k = 0
    result = ""

    while i >= 0 or j >= 0 or k == 1:
        a2 = 0
        b2 = 0

        if i >= 0:
            if a[i] == "1":
                a2= 1

        if j >= 0:
            if b[j] == "1":
                b2 = 1

        total = a2 + b2 + k

        if total == 0:
            result = "0" + result
            k =0
        elif total == 1:
            result = "1" + result
            k= 0
        elif total == 2:
            result = "0" + result
            k = 1
        else:
            result = "1" + result
            k = 1

        i -= 1
        j -= 1

    result = result.lstrip("0")

    if result == "":
        result = "0"

    return "0b" + result