import json
import wordnets
wn = wordnets.WordNet('fra')

arasaac = open('png.arasaac.color.fr.txt').read().split('\n')

output = {}
counts = []

for i in range(len(arasaac)):
	words = arasaac[i].split('_')[0].replace('\'', ' ').split(' ')
	synsets = []
	for word in words:
		s = wn.get_synsets(word)
		if len(s) == 0:
			for sw in word.split('-'):
				s += wn.get_synsets(sw)
		if len(s) == 0: print(word)
		synsets += s
	for synset in synsets:
		if synset in output: output[synset].append(i)
		else: output[synset] = [i]
	counts.append(len(synsets))

json.dump(output, open('png.arasaac.color.json', 'w'))
json.dump(counts, open('png.arasaac.color.counts.json', 'w'))