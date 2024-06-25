#!/usr/bin/env python3

import sys

def deduplicating_fasta_sequences(input_file, output_file):
    # Read the input FASTA file
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Initialize variables
    fasta_dict = {}
    current_sequence = []
    current_sequence_id = ''

    # Process the lines
    for line in lines:
        if line.startswith('>'):  # Sequence ID line
            if current_sequence:  # If we have collected a sequence, store it
                fasta_dict[current_sequence_id] = ''.join(current_sequence)
                current_sequence = []
            current_sequence_id = line.strip()[1:]
        else:  # Sequence line
            current_sequence.append(line.strip())

    # Store the last sequence
    if current_sequence_id and current_sequence:
        fasta_dict[current_sequence_id] = ''.join(current_sequence)

    # Write the processed sequences back to a new file
    with open(output_file, 'w') as file:
        for sequence_id, sequence in fasta_dict.items():
            file.write(f'>{sequence_id}\n{sequence}\n')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python deduplicate_fasta.py <input_file> <output_file>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        deduplicating_fasta_sequences(input_file, output_file)
