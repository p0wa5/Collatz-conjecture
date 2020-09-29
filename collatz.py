
def collatz(number):
    if number % 2 == 0:
        return number / 2
    else:
        return number * 3 + 1


try:
    x = int(input("Bitte gebe eine Zahl ein "))

    while x > 1:
        print(collatz(x))
        x = collatz(x)
except ValueError:
    print("Bitte gebe eine Zahl ein")

