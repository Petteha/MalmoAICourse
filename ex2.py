#count human to dog years
msg_template = """The equivalent of {humanyears:.2f} human years in dog years is {dogyears:.2f}.
""" # .format(humanyears, dogyears)


def count_dogyears(age):
    total = 0
    if age <= 2:
        for x in range(age) :
            total = total + 10.5
    else:
        total = 21.0
        for x in range(age - 2):
            total = total + 4

    my_msg = msg_template.format(humanyears = age, dogyears = total)
    
    print(my_msg)


