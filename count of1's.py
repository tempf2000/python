def count_ones_and_zeros(input_str):
    count_1 = 0
    count_0 = 0

    for symbol in input_str:
        if symbol == '1':
            count_1 += 1
        elif symbol == '0':
            count_0 += 1

    return count_1, count_0

# Example usage:
input_str = input("Enter a binary string: ")
count_1, count_0 = count_ones_and_zeros(input_str)

print(f"Number of '1's: {count_1}")
print(f"Number of '0's: {count_0}")
