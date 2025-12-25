with open("input.txt") as file:
    lines = file.readlines()

value = 50
total = 0


for line in lines:
    vorzeichen = line[0]
    number = int(line[1:])
    #print("value",value)
    #print("vorzeicehn",vorzeichen)
    #print("number ", number)
    if vorzeichen == "L":
        for x in range(0,number):
            value = value - 1
            if value == -1:
                value += 100
            if value == 0:
                total += 1
    else:
        for x in range(0,number):
            value = value + 1
            if value == 100:
                value -= 100
            if value == 0:
                total += 1

    #print("new value ",value)
    #print("current total ",total)
    #print("\n")


print("TOTAL", total)

