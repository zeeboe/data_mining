# ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ 
# ♡        Finding sequentially similar hits        ♡ 
# ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡  

# this script will generate a '{query}_sequential_processed_hits.csv' file that is populated by sequentially similar hits and can be easily read as a dataframe
# OPTIONAL: Filter the resulting data frame before extracting sequences of interest

python3 script_dir/sequence_hits.py database.fasta query script_dir home_dir


# ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ 
# ♡            Attaching sequences to hits          ♡ 
# ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ 

# this script will generate a '{query}_hits_sequences.fasta' file that is populated by sequences of sequentially similar hits to the query

# run the following command in the terminal
python3 script_dir/extract_sequences.py query home_dir database.fasta


# ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ 
# ♡        Finding structurally similar hits        ♡ 
# ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ 

# IN PROGRESS BUT ON ITS WAY ᕕ(◕ヮ◕)ᕗ
