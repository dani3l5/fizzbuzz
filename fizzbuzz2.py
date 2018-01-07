from collections import OrderedDict
def fizzbuzz(r, m):
    line = ""
    for i in range(1, int(r) + 1):
        for k, v in m.items():
            for item in v:
                if i % int(item) == 0:
                    line += k
                    break
        if line == "":
            line += str(i)
        print(line)
        line = ""


times = input("How many times should I play FizzBuzz?: ")
setting = True
cont = ""
a = OrderedDict()
while setting:
    name = input("Give the name of a Buzzword: ")
    multiples = input("At the multiples of which number should the word be used?"
                      " (Use commas): ")

    a[name] = multiples.split(',')

    cont = input("Do you want to create another Buzzword? (yes/no): ")
    if cont.lower() == "yes":
        pass
    elif cont.lower() == "no":
        setting = False
        fizzbuzz(times, a)
    else:
        print("Please enter a valid value!")
        exit(1)