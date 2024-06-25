#!/usr/bin/env python3

import pandas as pd
import argparse

def process_hits(query):
    # Define the columns and the separator
    columns = [
        'ProteinID', 'target_accession', 'query_name', 'query_accession', 
        'full_sequence_evalue', 'full_sequence_score', 'full_sequence_bias', 
        'domain_e_evalue', 'domain_score', 'domain_bias', 'domain#est_exp', 
        'domain#est_reg', 'domain#est_clu', 'domain#est_ov', 'domain#est_env', 
        'domain#est_dom', 'domain#est_rep', 'domain#est_inc', 
        'description_of_target'
    ]
    
    # Construct the input and output file names
    input_file = f'{query}_sequential_hits.csv'
    output_file = f'{query}_sequential_processed_hits.csv'
    
    # Read the sequential hits CSV file into a DataFrame
    sequential_hits = pd.read_csv(input_file, sep='\s+', skiprows=3, skipfooter=10, 
                                  header=None, names=columns, index_col=False, 
                                  engine='python')
    
    # Save the cleaned DataFrame to a new CSV file
    sequential_hits.to_csv(output_file, index=False)
    
    print(f"Processed file saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process sequential hits CSV file")
    parser.add_argument("query", type=str, help="Query name prefix for input and output files")
    
    args = parser.parse_args()
    
    process_hits(args.query)
