#!/usr/bin/env python3

import argparse
import os
import subprocess
from Bio import SeqIO

def extract_sequences(query_file, output_dir, home_dir, fasta_file):
    # Run the awk command to extract IDs from the CSV file
    sequential_hits_file = os.path.join(home_dir, f'{query_file}_sequential_hits.csv')
    sequential_hits_ids_file = os.path.join(home_dir, f'{query_file}_sequential_hits_ids.txt')
    
    awk_command = f"awk -F, 'NR > 1 {{ print $1 }}' {sequential_hits_file} > {sequential_hits_ids_file}"
    subprocess.run(awk_command, shell=True, check=True)
    
    # Read IDs from the sequential_hits_ids file
    with open(sequential_hits_ids_file, 'r') as f:
        protein_ids = [line.strip() for line in f.readlines()]

    # Extract sequences from the FASTA file
    sequences = []
    with open(fasta_file, 'r') as fasta:
        fasta_sequences = SeqIO.parse(fasta, 'fasta')
        for record in fasta_sequences:
            if record.id in protein_ids:
                sequences.append(record)

    # Determine output file path
    output_file = os.path.join(output_dir, '{query_file}_hits_sequences.fasta')

    # Write sequences to the output file in FASTA format
    with open(output_file, 'w') as out:
        SeqIO.write(sequences, out, 'fasta')

def main():
    parser = argparse.ArgumentParser(description="Extract sequences from a FASTA file based on IDs.")
    parser.add_argument("query_file", type=str, help="Prefix for the query and output files")
    parser.add_argument("scripts_dir", type=str, help="Directory containing scripts")
    parser.add_argument("home_dir", type=str, help="Home directory")
    parser.add_argument("fasta_file", type=str, help="FASTA file to search for sequences")

    args = parser.parse_args()

    extract_sequences(args.query_file, args.scripts_dir, args.home_dir, args.fasta_file)

if __name__ == "__main__":
    main()
