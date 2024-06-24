#!/usr/bin/env python3

import argparse
import os
import subprocess
from Bio import SeqIO

def main():
    parser = argparse.ArgumentParser(description="Extract sequences from a FASTA file based on IDs.")
    parser.add_argument("query", type=str, help="Prefix for the query and output files")
    parser.add_argument("scripts_dir", type=str, help="Directory containing scripts")
    parser.add_argument("home_dir", type=str, help="Home directory")
    parser.add_argument("fasta_file", type=str, help="FASTA file to search for sequences")

    args = parser.parse_args()

    query = args.query
    home_dir = args.home_dir
    fasta_file = args.fasta_file
    output_dir = args.scripts_dir

    # Step 1: Run the AWK command to extract IDs
    sequential_hits_file = os.path.join(home_dir, f'{query}_sequential_hits.csv')
    sequential_hits_ids_file = os.path.join(home_dir, f'{query}_sequential_hits_ids.txt')
    
    try:
        awk_command = f"awk -F, 'NR > 1 {{ print $1 }}' {sequential_hits_file} > {sequential_hits_ids_file}"
        subprocess.run(awk_command, shell=True, check=True)
        print(f"ID's extracted to {sequential_hits_ids_file} (๑˃ᴗ˂)ﻭ")
    except subprocess.CalledProcessError as e:
        print(f"Error running AWK command: {e}, cannot extract ID's from {sequential_hits_file} (╯°□°）╯")
        return

    # Step 2: Read the extracted IDs
    try:
        with open(sequential_hits_ids_file, 'r') as f:
            protein_ids = [line.strip() for line in f.readlines()]
        print(f"Read {len(protein_ids)} protein IDs from {sequential_hits_ids_file} (๑˃ᴗ˂)ﻭ")
    except Exception as e:
        print(f"Error reading IDs from {sequential_hits_ids_file}: {e} (╯°□°）╯")
        return

    # Step 3: Extract sequences from the FASTA file
    sequences = []
    try:
        with open(fasta_file, 'r') as fasta:
            fasta_sequences = SeqIO.parse(fasta, 'fasta')
            for record in fasta_sequences:
                if record.id in protein_ids:
                    sequences.append(record)
        print(f"Extracted {len(sequences)} sequences from {fasta_file} (๑˃ᴗ˂)ﻭ")
    except Exception as e:
        print(f"Error extracting sequences from {fasta_file}: {e} (╯°□°）╯")
        return

    # Step 4: Write the extracted sequences to an output file
    output_file = os.path.join(output_dir, f'{query}_hits_sequences.fasta')
    try:
        with open(output_file, 'w') as out:
            SeqIO.write(sequences, out, 'fasta')
        print(f"Sequences written to {output_file}")
        print("Congratulations! You done it! (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧")
    except Exception as e:
        print(f"Error writing sequences to {output_file}: {e} (╯°□°）╯")

if __name__ == "__main__":
    main()
