# (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ *:･ﾟ✧*:･ﾟ✧ *:･ﾟ✧ MINING LARGE DATA SETS  ✧ﾟ･:* ✧ﾟ･:* ✧ﾟ･:*ヽ(◕ヮ◕ヽ)

# For anyone who is completely new: Welcome! Coding is hard, but maybe this will help.

# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Project pipeline:
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Here are the steps we need to take to mine large data sets to find proteins of interest:

# 1. Create script directory where you can pull from my script repository on github : https://github.com/zeeboe/data_mining.git

# 2. Ensure that the database that is going to be mined is in a FASTA format

# 3. Find the amino acid sequence of your query, Uniprot is a good resource for this

# 4. Feed this sequence into NCBI protein BLAST using the clustered nr data base. Download these sequences as one large FASTA file and name it using the following naming convention: query_sequences.fasta

# 5. Create a home directory where you want the resulting files to be deposited into, and deposit the query_sequences.fasta into it

# 6. Feed this fasta into the "Looking for sequentially similar hits" command loop and set the variables accordingly. Use my variables as an example (◕‿◕✿)


# ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ 
# ♡      Looking for sequentially similar hits      ♡ 
# ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡  

# run all of this in the command line (◕‿◕✿)

# first set all of the necessary variables
query="pretzel" #this is the specific protein you're looking for
script_dir="/stor/work/Marcotte/project/zoya/github_repos/data_mining/scripts/" #this directory points to where the necessary scripts are located
home_dir="/stor/work/Marcotte/project/zoya/guaymas_mining/${query}/data" #this directory points to where all of the files will be deposited
database="/stor/work/Marcotte/project/zoya/polymerase/code/Guaymas_scaffold_data_base.fasta" #this is the data base that will be searched through
fasta_sequences_file="${home_dir}/${query}_sequences.fasta"
deduplicated_fasta="${home_dir}/${query}_sequences_deduplicated.fasta"
msa_file="${home_dir}/${query}_msa"
hmm_profile="${home_dir}/${query}_hmm"
sequential_hits="${home_dir}/${query}_sequential_hits.csv"

# run all of this after setting the variables
# Check if the input file exists
if [ -f "$fasta_sequences_file" ]; then
    # Run the deduplication script
    python3 "${script_dir}deduplicate_fasta.py" "$fasta_sequences_file" "$deduplicated_fasta"
    echo "DEDUPLICATION WORKED (๑˃ᴗ˂)ﻭ"
    if [ $? -ne 0 ]; then
        echo "Fasta file wasn't deduplicated (╯°□°）╯"
    fi
else
    echo "Input file not found: $fasta_sequences_file"
fi

# running the multiple sequence alignment
# Check if the input file exists
if [ -f "$deduplicated_fasta" ]; then
    # Run the muscle command
    muscle -in "$deduplicated_fasta" -out "$msa_file"
    echo "MSA WORKED (๑˃ᴗ˂)ﻭ"
    if [ $? -ne 0 ]; then
        echo "muscle command isn't working (╯°□°）╯"
    fi
else
    echo "Input file not found: $deduplicated_fasta"
fi

# creating a hammer profile
# Check if the input file exists
if [ -f "$msa_file" ]; then
    # Run the hmmbuild command
    hmmbuild --amino "$hmm_profile" "$msa_file"
    echo "HMMBUILD WORKED (๑˃ᴗ˂)ﻭ"
    if [ $? -ne 0 ]; then
        echo "HMMbuild command isn't working (╯°□°）╯"
    fi
else
    echo "Input file not found: $msa_file"
fi

# now that we have our hmmr profile we can search through a data base to find sequentially similar hits
# Check if the input file exists
if [ -f "$hmm_profile" ]; then
    # Run the hmmsearch command to give a table of sequentially similar hits
    hmmsearch -o /dev/null --cpu 6 -E 0.00005 --tblout "$sequential_hits"  "$hmm_profile" "$database"
    echo "HMMSEARCH WORKED (๑˃ᴗ˂)ﻭ"
    echo "Congrations! You done it! (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧"
    if [ $? -ne 0 ]; then
        echo "HMMsearch command isn't working (╯°□°）╯"
    fi
else
    echo "Input file not found: $hmm_profile"
fi
