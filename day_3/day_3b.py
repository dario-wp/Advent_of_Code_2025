file = "sample_input.txt"
total = 0
all_banks = []

with open (file) as f:
    for line in f:
        line = line.rstrip()
        all_banks.append(list(line))


for bank in all_banks:
    long_digit = []
    x = 12
    for digit in range(1,x):
        current_max = max(bank[ :-(x-digit)])
        long_digit.append(current_max)
        current_max_index = bank.index(current_max)
        bank = bank[current_max_index+1:]

    last_max = max(bank)
    long_digit.append(last_max)

    total += int("".join(long_digit))

print(total)
