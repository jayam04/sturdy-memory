testcases = int(input())

numbered = [
    'zer',
    'one',
    'two',
    'thr',
    'fou',
    'fiv',
    'six',
    'sev',
    'eig',
    'nin',
]

def sigleize(num):
    while num // 10 != 0:
        num = str(num)
        add = 0
        for char in num:
            add += int(char)
        num = add
    return num

for testcase in range(testcases):
    inpt = input().split()
    if len(inpt) != 2:
        print("Invalid")
        continue
    number, name = inpt
    e = 0
    e_breaked = False
    inited = False
    first = 0
    firsted = False
    add = 0
    negative = False
    invalid = False
    if number[0] == '-':
        nnegative = '-'
        number = number[1:]
    else:
        nnegative = ''
    for char in number:
        if char == '0' and not inited:
            continue
        elif char == '.':
            if not inited:
                e = 1
                inited = True
                negative = True
            else:
                e_breaked = True
        elif char < '0' or char > '9':
            invalid = True
            break
        elif not firsted and char != '0':
            first = int(char)
            firsted = True
            inited = not inited
            if negative:
                e_breaked = True
        else:
            add += int(char)
            if not e_breaked:
                e += 1
    for char in name:
        if char < 'a' or char > 'z':
            invalid = True
            break
    odd = e % 2
    password = ""
    negative = '-' if negative else '+'
    if e == 0:
        negative = ''
    password += f"{numbered[sigleize(first)]}.{numbered[sigleize(add)]}e{negative}{numbered[sigleize(e)]}@"
    if odd:
        name = name[0::2]
    else:
        name = name[1::2]
    if invalid:
        print("Invalid")
        continue
    print(nnegative+password+name)