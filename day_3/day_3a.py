file = "input.txt"
total = 0
all_banks = []

with open (file) as f:
    for line in f:
        line = line.rstrip()

        all_banks.append(list(line))
print(all_banks)

for bank in all_banks:
    first_max = max(bank[:-1])
    first_max_index = bank.index(first_max)

    second_max = max(bank[first_max_index+1:])

    total += int(first_max+second_max)

print(total)
