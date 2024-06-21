#!/usr/bin/env python3

def extract_sequences(protein_ids_file, fasta_file, output_file):
    # Read protein IDs into a set for fast lookup
    with open(protein_ids_file, 'r') as ids_file:
        protein_ids = set(line.strip() for line in ids_file)

    # Initialize variables to track sequence extraction
    current_protein_id = None
    found_protein_id = False
    output_lines = []

    # Iterate through the FASTA file and extract matching sequences
    with open(fasta_file, 'r') as fasta:
        for line in fasta:
            if line.startswith('>'):
                # Check if previous protein ID was in our list
                if current_protein_id and found_protein_id:
                    output_lines.append('\n')
                current_protein_id = line.strip()[1:]  # Extract protein ID from header
                found_protein_id = current_protein_id in protein_ids
            if found_protein_id:
                output_lines.append(line)

    # Write extracted sequences to the output file
    with open(output_file, 'w') as output:
        output.writelines(output_lines)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 4:
        print("Usage: python extract_sequences.py <protein_ids_file> <fasta_file> <output_file>")
        sys.exit(1)

    protein_ids_file = sys.argv[1]
    fasta_file = sys.argv[2]
    output_file = sys.argv[3]

    extract_sequences(protein_ids_file, fasta_file, output_file)
    print(f"Sequences extracted and saved to {output_file}")
