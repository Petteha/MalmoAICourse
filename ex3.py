def is_prime(number):
    if number < 1:
        print("Not prime.")
        return

    for x in range(2, number):
        if number % x == 0:
          print("Not prime.")  
          return
          
    print("Is prime.")

