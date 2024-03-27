def accepts_equal_01(input_str):
    count_1 = 0
    count_0 = 0

    for symbol in input_str:
        if symbol == '1':
            count_1 += 1
        elif symbol == '0':
            count_0 += 1

    return count_1 == count_0

# Example usage:
input_str = input("Enter a binary string: ")
result = accepts_equal_01(input_str)

if result:
    print("Accepted: The string has an equal number of '1's and '0's.")
else:
    print("Rejected: The string does not have an equal number of '1's and '0's.")
