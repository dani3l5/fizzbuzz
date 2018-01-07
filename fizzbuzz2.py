#Imports OrderedDict for use of storing Buzzwords and values
from collections import OrderedDict
#The spewing out words part
def fizzbuzz(r, m):
    #Used as for each line when printing
    line = ""
    #Do this for a specified number of times
    for i in range(1, int(r) + 1):
        #Go through each key and value for each value of i
        for k, v in m.items():
            #Go through each value for each key
            for item in v:
                #If i is divisible by that value add the Buzzword to line
                if i % int(item) == 0:
                    line += k
                    break
        #If no Buzzword applies just print the value of i
        if line == "":
            line += str(i)
        print(line)
        line = ""


times = input("How many times should I play FizzBuzz?: ")
#Used to control while loop
setting = True
#Used as a boolean of yes/no
cont = ""
#Creates an OrderedDict for storing Buzzwords and values.
a = OrderedDict()
#Adds to the dict
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
        #Starts the FizzBuzz process
        fizzbuzz(times, a)
    else:
        print("Please enter a valid value!")
        exit(1)