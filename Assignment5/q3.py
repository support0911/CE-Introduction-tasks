def price(n):
    return n * 1.15 + 2.25


scoops = int(input("Ice cream cone price calculator\n"
                   "How many scoops would you like: "))
print(f"A {scoops}-scoop cone will cost ${price(scoops):.2f}")
