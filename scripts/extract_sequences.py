#!/usr/bin/env python3

import argparse
import os
from Bio import SeqIO

def extract_sequences(query_file, output_dir, home_dir, fasta_file):
    # Read IDs from the query file
    with open(query_file, 'r') as f:
        protein_ids = [line.strip() for line in f.readlines()]

    # Extract sequences from the FASTA file
    sequences = []
    with open(fasta_file, 'r') as fasta:
        fasta_sequences = SeqIO.parse(fasta, 'fasta')
        for record in fasta_sequences:
            if record.id in protein_ids:
                sequences.append(record)

    # Determine output file path
    output_file = os.path.join(output_dir, 'hits_sequences.fasta')

    # Write sequences to the output file in FASTA format
    with open(output_file, 'w') as out:
        for seq in sequences:
            out.write(f'>{seq.id}\n{seq.seq}\n')

def main():
    parser = argparse.ArgumentParser(description="Extract sequences from a FASTA file based on IDs.")
    parser.add_argument("query_file", type=str, help="File containing IDs to extract")
    parser.add_argument("scripts_dir", type=str, help="Directory containing scripts")
    parser.add_argument("home_dir", type=str, help="Home directory")
    parser.add_argument("fasta_file", type=str, help="FASTA file to search for sequences")

    args = parser.parse_args()

    extract_sequences(args.query_file, args.scripts_dir, args.home_dir, args.fasta_file)

if __name__ == "__main__":
    main()
