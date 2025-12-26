filepath = "input.txt"
range_ids =  []
available_ids = []
fresh_ingredients = 0

with open (filepath) as f:
    lines = f.readlines()
    part_one = True
    for line in lines:
        if line == "\n":
            part_one = False
        elif part_one:
            temp_array = []
            for x in line.strip().split("-"):
                temp_array.append(int(x))
            range_ids.append(temp_array)

        else:
            available_ids.append(int(line.strip()))

#print(range_ids)
#print(available_ids)

for id in available_ids:
    for [start,end] in range_ids:
        if start <= id <= end+1:
            fresh_ingredients += 1
            break

print(fresh_ingredients)