file = "input.txt"
product_id_arr = []
total = 0

with open (file) as f:
    for line in f:
        line = line.rstrip().split(",")
        for product_id in line:
            if product_id:
                if not(product_id[0] == "0"):
                    product_id = product_id.split("-")
                    product_id_arr.append(product_id)


for val_pair in product_id_arr:
    a,b = val_pair
    a = int(a)
    b = int(b)

    for value in range(a,b+1):
        value = str(value)
        len_value = len(value)
        if len_value % 2 == 0:
            v_teil_1 = value[0:(len_value//2)]
            v_teil_2 = value[len_value//2:]
            if v_teil_1 == v_teil_2:
                total += int(value)


print(total)

