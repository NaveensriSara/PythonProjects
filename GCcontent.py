

nbases = 0
GCbases = 0

def gc(dna):
	global nbases
	global GCbases
	for i in dna:
		if (i== 'A') or (i== 'T'):
			nbases += 1
		if (i == 'C') or (i == 'G'):
			GCbases += 1
			nbases +=1
	finalCalc = ((GCbases/nbases)*100)
	return GCbases,nbases, finalCalc



result = gc('ATGCTGCGTA')
print (result)