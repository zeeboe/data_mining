# (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ *:･ﾟ✧*:･ﾟ✧ *:･ﾟ✧ MINING LARGE DATA SETS  ✧ﾟ･:* ✧ﾟ･:* ✧ﾟ･:*ヽ(◕ヮ◕ヽ)

# For anyone who is completely new: Welcome! Coding is hard, but maybe this will help.
# This script will search for sequentially similar entries to a query in a large data base
# The input is a list of FASTA sequences from known organisms and the output is a csv of sequentially similar hits that can be read as a data frame in python

# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Preparing all of the variables
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Before we start running our commands, set up the following:

# 1. Create script directory where you can pull from my script repository on github : https://github.com/zeeboe/data_mining.git

# 2. Create a home directory where the resulting files can be deposited

# 3. Create a database.fasta file that has all of the sequences in the database in FASTA format

# 4. Create a sequences.fasta file that is a list of FASTA sequences similar to the query sequence from various organisms. Name this fasta file with the naming convention 'query_sequences.fasta' (query can be whatever you choose to name the query, the important part is the "_sequences.fasta")

# ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ 
# ♡        Finding sequentially similar hits        ♡ 
# ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡  

# this script will generate a '{query}_sequential_processed_hits.csv' file that is populated by sequentially similar hits and can be easily read as a dataframe
# OPTIONAL: Filter the resulting data frame before extracting sequences of interest

python3 sequence_hits.py query path/to/scripts /path/to/home database.fasta


# ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ 
# ♡            Attaching sequences to hits          ♡ 
# ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ 

# this script will generate a '{query}_hits_sequences.fasta' file that is populated by sequences of sequentially similar hits to the query

# run the following command in the terminal
python3 path/to/scripts/extract_sequences.py query /path/to/home /path/to/database.fasta


# ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ 
# ♡        Finding structurally similar hits        ♡ 
# ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ 

# IN PROGRESS BUT ON ITS WAY ᕕ(◕ヮ◕)ᕗ
