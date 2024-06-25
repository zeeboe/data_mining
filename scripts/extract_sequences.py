#!/usr/bin/env python3

import argparse
import os
import subprocess
from Bio import SeqIO

# ANSI color escape sequences
class Color:
    PINK = '\033[95m'
    YELLOW = '\033[93m'
    END = '\033[0m'

def run_awk_command(home_dir, query_file):
    # Run the awk command to extract IDs from the CSV file
    sequential_hits_file = os.path.join(home_dir, f'{query_file}_sequential_clean_hits.csv')
    sequential_hits_ids_file = os.path.join(home_dir, f'{query_file}_sequential_hits_ids.txt')
    
    awk_command = f"awk -F, 'NR > 1 {{ print $1 }}' {sequential_hits_file} > {sequential_hits_ids_file}"
    
    try:
        subprocess.run(awk_command, shell=True, check=True)
        print(f"{Color.PINK}ID extraction successful! (๑˃ᴗ˂)ﻭ Extracted IDs to: {sequential_hits_ids_file}{Color.END}")
    except subprocess.CalledProcessError as e:
        print(f"{Color.YELLOW}Error running AWK command: {e}{Color.END}")
        raise

    return sequential_hits_ids_file

def extract_sequences(query_file, home_dir, fasta_file):
    # Determine the sequential_hits_ids file path
    sequential_hits_ids_file = os.path.join(home_dir, f'{query_file}_sequential_hits_ids.txt')
    
    try:
        # Read IDs from the sequential_hits_ids file
        with open(sequential_hits_ids_file, 'r') as f:
            protein_ids = [line.strip() for line in f.readlines()]
        print(f"Read {len(protein_ids)} IDs from: {sequential_hits_ids_file}")
    except Exception as e:
        print(f"{Color.YELLOW}Error reading IDs from {sequential_hits_ids_file}: {e}{Color.END}")
        raise

    # Extract sequences from the FASTA file
    sequences = []
    try:
        with open(fasta_file, 'r') as fasta:
            fasta_sequences = SeqIO.parse(fasta, 'fasta')
            for record in fasta_sequences:
                if record.id in protein_ids:
                    # Append sequence as a single line with '>' and sequence on the next line
                    sequences.append(f'>{record.id}\n{record.seq}')
        print(f"Extracted {len(sequences)} sequences from: {fasta_file}")
    except Exception as e:
        print(f"{Color.YELLOW}Error extracting sequences from {fasta_file}: {e}{Color.END}")
        raise

    # Determine output file path
    output_file = os.path.join(home_dir, f'{query_file}_hits_sequences.fasta')

    # Write sequences to the output file in FASTA format
    try:
        with open(output_file, 'w') as out:
            out.write('\n'.join(sequences) + '\n')
        print(f"{Color.PINK}Sequences written to: {output_file} (๑˃ᴗ˂)ﻭ {Color.END}")
    except Exception as e:
        print(f"{Color.YELLOW}Error writing sequences to {output_file}: {e}{Color.END}")
        raise

def main():
    parser = argparse.ArgumentParser(description="Extract sequences from a FASTA file based on IDs.")
    parser.add_argument("query_file", type=str, help="Prefix for the query and output files")
    parser.add_argument("home_dir", type=str, help="Home directory")
    parser.add_argument("fasta_file", type=str, help="FASTA file to search for sequences")

    args = parser.parse_args()

    try:
        # Run awk command to generate the sequential hits IDs file
        ids_file = run_awk_command(args.home_dir, args.query_file)
        
        # Extract sequences based on the generated IDs
        extract_sequences(args.query_file, args.home_dir, args.fasta_file)
        
        print(f"{Color.PINK}Extraction process completed successfully! (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧{Color.END}")
    except Exception as e:
        print(f"{Color.YELLOW}Error during sequence extraction: {e}{Color.END}")
        print(f"{Color.YELLOW}Extraction process encountered an error. (╯°□°）╯︵ ┻━┻{Color.END}")
        exit(1)

if __name__ == "__main__":
    main()
