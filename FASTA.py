 #!/usr/bin/python 
import sys
filename=sys.argv[0]

f = {}
try: 
	f= open("FASTA")
except IOError: 
	print ("File does not exisit!")
seqs={}
for line in f:
	#print (line)
	line = line.rstrip()
	#print (line )
	if line[0] == '>':
		words=line.split()
		#print ( words)
		name =words[0][1:]
		#print (name)
		seqs[name]= ''
		#print (seqs[name])
	else:
		seqs[name]=seqs[name]+line
f.close()


for name,seq in seqs.items():
       print(name,seq)