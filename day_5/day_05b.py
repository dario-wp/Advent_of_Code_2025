filepath = "input.txt"
range_ids =  []
fresh_ingredients = 0

def merge_range_ids(range_ids):
    new_range_ids = []
    len_range = len(range_ids)
    can_be_ignored = -1
    for i in range(0,len_range-1):
        start1,end1 = range_ids[i]
        start2,end2 = range_ids[i+1]
        if i == can_be_ignored:
            if i == len_range-2:
                new_range_ids.append([start2,end2])
            continue
        if end1 >= start2 and end1<end2:
            new_range_ids.append([start1,end2])
            can_be_ignored = i+1
        elif end1 >= start2 and end1 >= end2:
            new_range_ids.append([start1, end1])
            can_be_ignored = i + 1
        elif i == len_range-2:
            new_range_ids.append([start1,end1])
            new_range_ids.append([start2, end2])
        else:
            new_range_ids.append([start1,end1])

    return new_range_ids

with open (filepath) as f:
    lines = f.readlines()
    for line in lines:
        if line == "\n":
            break
        temp_array = []
        for x in line.strip().split("-"):
            temp_array.append(int(x))
        range_ids.append(temp_array)


#print("range before sort",range_ids)
range_ids.sort()
#print("range after sort",range_ids)

for x in range(0,1000):
    range_ids = merge_range_ids(range_ids)
#print(range_ids)
for [start,end] in range_ids:
    fresh_ingredients += end-start+1

#print(fresh_ingredients)
print(fresh_ingredients)