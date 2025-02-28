import streamlit as st
import pandas as pd
from Bio import SeqIO
from io import StringIO  # ✅ Fix: Needed to read text as a file

st.title("🧬 SNP Pathogenicity Predictor")

fasta_data = """>Seq1
ATGCGTACGTTAGTAACTG
>Seq2
ATGCGTACGTTAGTACCTG
>Seq3
ATGCGTACGTTGGTAACTG
>Seq4
ATGCGGACGTTAGTAACTG
"""

st.subheader("Simulated FASTA Sequences")
fasta_input = st.text_area("Edit FASTA sequences:", fasta_data, height=200)

# ✅ Fix: Use StringIO to handle the FASTA input correctly
def parse_fasta(fasta_text):
    fasta_io = StringIO(fasta_text.strip())  # Convert to file-like object
    parsed_records = list(SeqIO.parse(fasta_io, "fasta"))  # Proper parsing
    return parsed_records if parsed_records else None

def predict_pathogenicity(snp_features):
    return ["pathogenic" if sum(features) > 1 else "benign" for features in snp_features]

if st.button("Analyze SNPs"):
    parsed_sequences = parse_fasta(fasta_input)  # ✅ Now works without error!

    if not parsed_sequences:
        st.error("❌ Invalid FASTA format. Please check the input!")
    else:
        example_snp_features = [[0.5, 0.8], [0.2, 1.2], [0.9, 0.7]]
        pathogenicity_results = predict_pathogenicity(example_snp_features)

        st.success("✅ SNP Pathogenicity Analysis Complete!")
        df_results = pd.DataFrame({"SNP Features": example_snp_features, "Prediction": pathogenicity_results})
        st.dataframe(df_results)
