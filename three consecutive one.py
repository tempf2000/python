def accepts_three_consecutive_ones(input_str):
    current_state = 'q0'

    for symbol in input_str:
        if current_state == 'q0' and symbol == '1':
            current_state = 'q1'
        elif current_state == 'q1' and symbol == '1':
            current_state = 'q2'
        elif current_state == 'q2' and symbol == '1':
            return True
        else:
            current_state = 'q0'

    return False

input_str = input("Enter a binary string: ")
result = accepts_three_consecutive_ones(input_str)

if result:
    print("Accepted: The string contains three consecutive '1's.")
else:
    print("Rejected: The string does not contain three consecutive '1's.")
