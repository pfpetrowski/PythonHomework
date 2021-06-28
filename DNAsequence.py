
def reverse(sequence): 
	return sequence[::-1]

genome_compliments = []
genome_orginal = []

lines=[]
with open('sequences.txt') as f:
	data = f.read().splitlines()
	#print(data)
	genome_orginal = data
for sequence in genome_orginal:
	#print(sequence)
	output = reverse(sequence)
	#print(output)
	genome_compliments.append(output)

genome_pairs = dict(zip(genome_orginal, genome_compliments))
print(genome_pairs)