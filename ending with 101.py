
def accepts_string_ending_with_101(input_str):
    current_state = 'q0'

    for symbol in input_str:
        if current_state == 'q0' and symbol == '1':
            current_state = 'q1'
        elif current_state == 'q1' and symbol == '0':
            current_state = 'q2'
        elif current_state == 'q2' and symbol == '1':
            current_state = 'q3'
        else:
            current_state = 'q0'

    return current_state == 'q3'

input_str = input("Enter a binary string: ")
result = accepts_string_ending_with_101(input_str)

if result:
    print("Accepted: The string ends with '101'.")
else:
    print("Rejected: The string does not end with '101'.")
