def is_prime(number):
    if number < 1:
        print("Not prime.")
        return False

    for x in range(2, number):
        if number % x == 0:
          return False
          return
          
    return True

def find_prime(number):
    prime = False
    temp = number + 1
    while (prime == False):
        if (is_prime(temp) == False):
            temp = temp + 1
        else:
            print("Next prime number is {0}.".format(temp))
            prime = True