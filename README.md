# (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ *:･ﾟ✧*:･ﾟ✧ *:･ﾟ✧ MINING LARGE DATA SETS  ✧*

 For anyone who is completely new: Welcome! Coding is hard, but maybe this will help.
 
 This script will search for sequentially similar entries to a query in a large data base.
 
The input is a list of FASTA sequences from known organisms and the output is a csv of sequentially similar hits that can be read as a data frame in python

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Preparing all of the variables
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

 1. Create script directory where you can pull from my script repository on github : https://github.com/zeeboe/data_mining.git

 2. Create a home directory where the resulting files can be deposited

 3. Create a database.fasta file that has all of the sequences in the database in FASTA format

 4. Create a sequences.fasta file that is a list of FASTA sequences similar to the query sequence from various organisms. Name this fasta file with the naming convention 'query_sequences.fasta' (query can be whatever you choose to name the query, the important part is the "_sequences.fasta")
