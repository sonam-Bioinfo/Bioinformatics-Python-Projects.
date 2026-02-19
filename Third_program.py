# ----GC Content Calculation----
# Formula: ((G + C) / Total Length) * 100
# 1. DNA Sequence
dna_seq = "ATGCATGCATGC"
# 2. G aur C ko count karna
g_count = dna_seq.count('G')
c_count = dna_seq.count('C')
# 3. Total length nikalna 
total_len = len(dna_seq)
# 4.Math lagana (GC Percentage)
gc_content = ((g_count + c_count) / total_len) * 100
# 5. result print karna 
print("DNA Sequence:", dna_seq)
print("GC Content Percentage:", gc_content, "%")
