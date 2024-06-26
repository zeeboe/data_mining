#!/usr/bin/env python3

# this is a modified version of the esmfold script by darylrbarth
# she is the best in general, but especially for making this script

import argparse
from Bio import SeqIO
import pandas as pd
import torch
from transformers import AutoTokenizer, EsmForProteinFolding
from transformers.models.esm.openfold_utils.protein import to_pdb, Protein as OFProtein
from transformers.models.esm.openfold_utils.feats import atom14_to_atom37
from src.make_pdb import convert_outputs_to_pdb, output_pdb, fasta2dict
from tqdm import tqdm

# Model setup
tokenizer = AutoTokenizer.from_pretrained("facebook/esmfold_v1")
model = EsmForProteinFolding.from_pretrained("facebook/esmfold_v1", low_cpu_mem_usage=True)

model = model.cuda()
model.esm = model.esm.half()

# Enable TensorFloat32 computation
torch.backends.cuda.matmul.allow_tf32 = True

# Reduce the 'chunk_size' for folding trunk
model.trunk.set_chunk_size(64)

def read_fasta_to_dataframe(fasta_file):
    """Reads a FASTA file and returns a pandas DataFrame."""
    ids = []
    sequences = []
    for record in SeqIO.parse(fasta_file, "fasta"):
        ids.append(record.id)
        sequences.append(str(record.seq))
    df = pd.DataFrame({'ID': ids, 'Sequence': sequences})
    return df

def run_esm_fold(aa):
    """Runs ESMFold on a given amino acid sequence."""
    tokenized_input = tokenizer([aa], return_tensors="pt", add_special_tokens=False)['input_ids']
    tokenized_input = tokenized_input.cuda()
    with torch.no_grad():
        output = model(tokenized_input)
    pdb = convert_outputs_to_pdb(output)
    return pdb

def main(fasta_fp, output_fp):
    """Main function to process the FASTA file and generate PDB outputs."""
    # Read in fasta file to a dictionary
    protein_dict = fasta2dict(fasta_fp)

    # Run esm fold on each protein sequence
    for prot_name, aa in tqdm(protein_dict.items()):
        pdb = run_esm_fold(aa)
        print(f"Finished folding {prot_name}")
        output_pdb(prot_name, output_fp, pdb)

    print('Done!')

    # Clean up memory
    del model 
    torch.cuda.empty_cache()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run ESMFold on a FASTA file and save the PDB outputs.")
    parser.add_argument("fasta_fp", type=str, help="Path to the input FASTA file.")
    parser.add_argument("output_fp", type=str, help="Path to the output directory for PDB files.")
    args = parser.parse_args()

    main(args.fasta_fp, args.output_fp)
