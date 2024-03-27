def generate_derivation(grammar, start_symbol, sequence, max_depth=10):
    derivation_sequences = []
    def derive(current_sequence, depth):
        if depth == 0:
            return
        for rule in grammar:
            non_terminal, production = rule.split(' -> ')
            alternatives = production.split('|')
            for alt in alternatives:
                if current_sequence.startswith(alt):
                    new_sequence = current_sequence.replace(alt, non_terminal, 1)
                    derivation_sequences.append(new_sequence)
                    derive(new_sequence, depth - 1)
    derive(sequence, max_depth)
    return derivation_sequences
grammar = [
    "S -> AB",
    "A -> a|ε",
    "B -> b"
]
start_symbol = 'S'
target_sequence = 'ab'
derivation_sequences = generate_derivation(grammar, start_symbol, target_sequence)
for i, deriv_seq in enumerate(derivation_sequences, 1):
    print(f"Derivation Sequence {i}: {deriv_seq}")
