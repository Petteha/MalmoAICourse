
def kanelbulle(amount):
    fresh = amount * 35.0
    discount = fresh * 0.60
    total = fresh - discount
    print("The fresh price is {0:.2f}, and the discount for day-old is {1:.2f}.".format(fresh, discount))
    print("The total will be {0:.2f}".format(total))

kanelbulle(5)