file = "input.txt"
product_id_arr = []
total = 0


def value_is_invalid(value):
    value = str(value)
    len_value = len(value)
    invalid = False


    for split_val in range(1,(len_value//2)+1):
        origin_val = value[0:split_val]
        invalid = True
        for x in range(split_val, len_value, split_val):
            if origin_val != value[x:x+split_val]:
                invalid = False
                break
        if invalid:
            return True

    return False


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
        if value_is_invalid(value):
            total += value




print(total)
