def is_divisible_by_2(input_str):
    current_state = 'q0'

    for digit in input_str:
        if current_state == 'q0' and digit in '02468':
            current_state = 'q1'
        elif current_state == 'q1' and digit in '02468':
            current_state = 'q0'
        else:
            return False

    return current_state == 'q0'


input_str = input("Enter a decimal number: ")

result = is_divisible_by_2(input_str)

if result:
    print("Accepted: The decimal number is divisible by 2.")
else:
    print("Rejected: The decimal number is not divisible by 2.")
