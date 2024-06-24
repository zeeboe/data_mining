#!/usr/bin/env python3

# ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ 
# ♡        Finding sequentially similar hits        ♡ 
# ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡  

# script for finding sequentially similar queries in a database

import argparse
import os
import subprocess

def main():
    parser = argparse.ArgumentParser(description="Processing sequence data to find sequentially similar hits.")
    parser.add_argument("database", type=str, help="The database that will be searched through")
    parser.add_argument("query", type=str, help="The name of the specific sequence you're looking for")
    parser.add_argument("script_dir", type=str, help="The directory where the necessary scripts are located")
    parser.add_argument("home_dir", type=str, help="The directory where all of the files will be deposited")

    args = parser.parse_args()

    # Set variables from arguments
    query = args.query
    database = args.database
    script_dir = args.script_dir
    home_dir = args.home_dir


    fasta_sequences_file = os.path.join(home_dir, f"{query}_sequences.fasta")
    deduplicated_fasta = os.path.join(home_dir, f"{query}_sequences_deduplicated.fasta")
    msa_file = os.path.join(home_dir, f"{query}_msa")
    hmm_profile = os.path.join(home_dir, f"{query}_hmm")
    sequential_hits = os.path.join(home_dir, f"{query}_sequential_hits_table")

    # Check if the input file exists
    if os.path.isfile(fasta_sequences_file):
        # Run the deduplication script
        result = subprocess.run(["python3", os.path.join(script_dir, "deduplicate_fasta.py"), fasta_sequences_file, deduplicated_fasta])
        if result.returncode == 0:
            print("DEDUPLICATION WORKED (๑˃ᴗ˂)ﻭ")
        else:
            print("Fasta file wasn't deduplicated (╯°□°）╯")
    else:
        print(f"Input file not found: {fasta_sequences_file}")
        return

    # Run the multiple sequence alignment
    if os.path.isfile(deduplicated_fasta):
        result = subprocess.run(["muscle", "-in", deduplicated_fasta, "-out", msa_file])
        if result.returncode == 0:
            print("MSA WORKED (๑˃ᴗ˂)ﻭ")
        else:
            print("muscle command isn't working (╯°□°）╯")
    else:
        print(f"Input file not found: {deduplicated_fasta}")
        return

    # Create a hammer profile
    if os.path.isfile(msa_file):
        result = subprocess.run(["hmmbuild", "--amino", hmm_profile, msa_file])
        if result.returncode == 0:
            print("HMMBUILD WORKED (๑˃ᴗ˂)ﻭ")
        else:
            print("HMMbuild command isn't working (╯°□°）╯")
    else:
        print(f"Input file not found: {msa_file}")
        return

    # Search through a database to find sequentially similar hits
    if os.path.isfile(hmm_profile):
        result = subprocess.run(["hmmsearch", "-o", "/dev/null", "--cpu", "6", "-E", "0.00005", "--tblout", sequential_hits, hmm_profile, database])
        if result.returncode == 0:
            print("HMMSEARCH WORKED (๑˃ᴗ˂)ﻭ")
            print("Congratulations! You done it! (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧")
        else:
            print("HMMsearch command isn't working (╯°□°）╯")
    else:
        print(f"Input file not found: {hmm_profile}")

if __name__ == "__main__":
    main()
