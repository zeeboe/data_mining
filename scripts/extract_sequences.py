#!/usr/bin/env python3

import argparse
import os
from Bio import SeqIO

def extract_sequences(ids_file, fasta_file, output_file):
    # Read IDs from the input file
    with open(ids_file, 'r') as f:
        protein_ids = [line.strip() for line in f.readlines()]

    # Extract sequences from the FASTA file
    sequences = []
    with open(fasta_file, 'r') as fasta:
        fasta_sequences = SeqIO.parse(fasta, 'fasta')
        for record in fasta_sequences:
            if record.id in protein_ids:
                sequences.append(record)

    # Write sequences to the output file in FASTA format
    with open(output_file, 'w') as out:
        for seq in sequences:
            out.write(f'>{seq.id}\n{seq.seq}\n')

def main():
    parser = argparse.ArgumentParser(description="Extract sequences from a FASTA file based on IDs.")
    parser.add_argument("ids_file", type=str, help="File containing IDs to extract")
    parser.add_argument("fasta_file", type=str, help="FASTA file to search for sequences")
    parser.add_argument("output_file", type=str, help="Output file to write extracted sequences")

    args = parser.parse_args()

    extract_sequences(args.ids_file, args.fasta_file, args.output_file)

if __name__ == "__main__":
    main()
