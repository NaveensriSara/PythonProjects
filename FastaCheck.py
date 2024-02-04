# Run checks on Fasta file

# 1) Check if the file exists in the right directory
try:
    f = open("dna2.fasta")
except IOError:
    print("File does not exist!")

# Check if it is a fasta file
RecordCount = 0
seqs = {}
seq_lengths = []

for line in f:
    line = line.rstrip()
    if line[0] == ">":
        words = line.split()
        name = words[0][1:]
        seqs[name] = ''
        RecordCount += 1
    else:
        seqs[name] = seqs[name] + line
print(RecordCount)

# Calculate sequence lengths and find min and max
name_lengths = []
names = []

for name, seq in seqs.items():
    name_length = len(name)
    names.append(name)  # Append the actual name, not the length
    seq_length = len(seq)
    seq_lengths.append(seq_length)
    name_lengths.append(name_length)

# Find min and max sequence lengths
min_seq_length = min(seq_lengths)
max_seq_length = max(seq_lengths)

# Find min and max name lengths
min_name_length = min(name_lengths)
max_name_length = max(name_lengths)

# Print results
print("Min sequence length:", min_seq_length)
print("Max sequence length:", max_seq_length)
print("Min name length:", min_name_length)
print("Max name length:", max_name_length)

# Print corresponding names for min and max sequence lengths
min_seq_index = seq_lengths.index(min_seq_length)
max_seq_index = seq_lengths.index(max_seq_length)

print("Name corresponding to min sequence length:", names[min_seq_index])
print("Name corresponding to max sequence length:", names[max_seq_index])

for name, seqs in seqs.tems():
    start_codon = ['atg']
    start_codon_found = False 
    for i in range[0, len(seqs),3]

# Close the file
f.close()

def find_orfs(sequence):
    start_codon = "ATG"
    stop_codons = ["TAA", "TAG", "TGA"]

    orfs = []
    in_orf = False
    current_orf = ""

    for i in range(0, len(sequence), 3):
        codon = sequence[i:i + 3]

        if codon == start_codon:
            if not in_orf:
                in_orf = True
                current_orf = start_codon
        elif codon in stop_codons:
            if in_orf:
                in_orf = False
                orfs.append(current_orf + codon)
                current_orf = ""
        elif in_orf:
            current_orf += codon

    return orfs


# Run checks on Fasta file
try:
    with open("dna2.fasta") as f:
        # Sequence and name information
        RecordCount = 0
        seqs = {}
        seq_lengths = []

        for line in f:
            line = line.rstrip()
            if line[0] == ">":
                words = line.split()
                name = words[0][1:]
                seqs[name] = ''
                RecordCount += 1
            else:
                seqs[name] = seqs[name] + line

    # Print sequences
    for sequence_id, sequence in seqs.items():
        print(f"Sequence ID: {sequence_id}")
        print(f"Sequence: {sequence}")

    # ORF Analysis
    # Analyze each sequence for ORFs
    max_orf_length = 0
    max_orf_sequence_id = None
    max_orf_sequence = None
    max_orf_start_position = None

    for sequence_id, sequence in seqs.items():
        for reading_frame in range(1, 4):  # Loop over forward reading frames
            current_frame_sequence = sequence[reading_frame - 1:]
            orfs = find_orfs(current_frame_sequence)
            for orf in orfs:
                orf_length = len(orf)
                if orf_length > max_orf_length:
                    max_orf_length = orf_length
                    max_orf_sequence_id = sequence_id
                    max_orf_sequence = orf
                    max_orf_start_position = sequence.find(orf) + 1 + reading_frame - 1

    print("\nORF Analysis:")
    print("Length of the longest ORF:", max_orf_length)
    print("Identifier of the sequence containing the longest ORF:", max_orf_sequence_id)
    print("Longest ORF:", max_orf_sequence)
    print("Starting position of the longest ORF:", max_orf_start_position)

    # Calculate sequence lengths and find min and max
    name_lengths = []
    names = []

    for name, seq in seqs.items():
        name_length = len(name)
        names.append(name)
        seq_length = len(seq)
        seq_lengths.append(seq_length)
        name_lengths.append(name_length)

    # Find min and max sequence lengths
    min_seq_length = min(seq_lengths)
    max_seq_length = max(seq_lengths)

    # Find min and max name lengths
    min_name_length = min(name_lengths)
    max_name_length = max(name_lengths)

    # Print results
    print("\nSequence and Name Length Analysis:")
    print("Min sequence length:", min_seq_length)
    print("Max sequence length:", max_seq_length)
    print("Min name length:", min_name_length)
    print("Max name length:", max_name_length)

    # Print corresponding names for min and max sequence lengths
    min_seq_index = seq_lengths.index(min_seq_length)
    max_seq_index = seq_lengths.index(max_seq_length)

    print("Name corresponding to min sequence length:", names[min_seq_index])
    print("Name corresponding to max sequence length:", names[max_seq_index])

    # Print corresponding names for min and max name lengths
    min_name_index = name_lengths.index(min_name_length)
    max_name_index = name_lengths.index(max_name_length)

    print("Name corresponding to min name length:", names[min_name_index])
    print("Name corresponding to max name length:", names[max_name_index])

except IOError:
    print("File does not exist!")

