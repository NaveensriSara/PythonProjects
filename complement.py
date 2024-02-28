global dna 
dna = "AGATCGCGTA"
def complement(seq):
	basecomplement = {'A':'T','C':'G','G':'C','T':'A','N':'N',
					 'a':'t','t':'a','c':'g','g':'c','n':'n'}
	letters = list(seq)
	letters = [basecomplement[base]for base in letters]
	print( ''.join(letters))
	

complement(dna)