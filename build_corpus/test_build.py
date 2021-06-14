import time
start_time = time.perf_counter()
import itertools


from math import exp

import dask
dask.config.set(scheduler='threads')  
# Create overall dict of CUIS
# Each key CUI contains a list
# That list indices are also lists for each property we take
# Can find CUI in dict with key, access index of master list, then;
# for each sub list per property iterate over as needed.

# For the Metathesaurus:
# Total lines/CUIs in MRCONSO "7,964,596"
# Total lines/CUIs/definitions: 291,835
# Total CUIs in MRHIER "2,894,771 but many many atoms for each concept"
"""
1. Find all atoms of a UMLS concept.

SELECT * FROM mrconso
WHERE cui = 'C0032344';

2. Find all source definitions associated with a UMLS concept.

SELECT * FROM mrdef
WHERE cui = 'C0032344';

3. Find all source contexts associated with a UMLS concept.

SELECT * FROM mrhier
WHERE cui = 'C0032344';

4. Find all attributes for a UMLS concept.

SELECT * FROM mrsat
WHERE cui = 'C0032344'
		 AND stype = 'CUI';

5. Find all semantic types for a UMLS concept.

SELECT * FROM mrsty
WHERE cui = 'C0032344';

6.a. Find all relationships for a UMLS concept.
Note: In MRREL, the REL/RELA always expresses the nature of the relationship from CUI2 to the "current concept", CUI1. Because we're querying CUI1 below, this represents the "natural" direction of the relationship.

SELECT * FROM mrrel
WHERE cui1 = 'C0032344'

6.b. Find all inverse relationships for a UMLS concept.
Note: In MRREL, the REL/RELA always expresses the nature of the relationship from CUI2 to the "current concept", CUI1. Because we're querying CUI2 below, this represents the opposite of the "natural" direction of the relationship.

SELECT * FROM mrrel
WHERE cui2 = 'C0032344';
		 AND stype2 = 'CUI';

7. Find all relationships for a concept and the preferred (English) name of the CUI2.

SELECT a.cui1, a.cui2, b.str FROM mrrel a, mrconso b
WHERE a.cui1 = 'C0032344'
		 AND a.stype1 = 'CUI'
		 AND a.cui2 = b.cui
		 AND b.ts = 'P'
		 AND b.stt = 'PF'
		 AND b.ispref = 'Y'
		 AND b.lat = 'ENG';
"""


##################################################################################################################################################

#MRCONSO generate CUI dictionary file, this will be faster than re-creating every time we are getting data
# Total lines/CUIs in MRCONSO 7,964,596
"""
CUIs = {}


f = open('/home/karl/UMLS/2020AB/META/MRCONSO.RRF', 'r') 
for line in f.readlines():
	print(line)
	splitline = str(line).strip().split('|')
	CUI = splitline[0]

	if not CUI in CUIs:
		CUIs[CUI] = []
f.close()

print(len(CUIs))
"""

# THIS MANY UNIQUE IN DICTIONARY 3,500,967

#Let's batch these to reduce iteration time to find unique CUIs
print('defining variables and functions')


total_batch1 = []
total_batch2 = []
total_batch3 = []
total_batch4 = []
total_batch5 = []
total_batch6 = []
total_batch7 = []
total_batch8 = []
total_batch9 = []
total_batch10 = []
total_batch11 = []
total_batch12 = []
total_batch13 = []
total_batch14 = []
total_batch15 = []
total_batch16 = []
total_batch17 = []
total_batch18 = []
total_batch19 = []
total_batch20 = []
total_batch21 = []
total_batch22 = []
total_batch23 = []
total_batch24 = []
total_batch25 = []
total_batch26 = []
total_batch27 = []
total_batch28 = []
total_batch29 = []
total_batch30 = []
total_batch31 = []
total_batch32 = []
total_batch33 = []
total_batch34 = []
total_batch35 = []
total_batch36 = []
total_batch37 = []
total_batch38 = []
total_batch39 = []
total_batch40 = []
total_batch41 = []
total_batch42 = []
total_batch43 = []
total_batch44 = []
total_batch45 = []
total_batch46 = []
total_batch47 = []
total_batch48 = []
total_batch49 = []
total_batch50 = []
total_batch51 = []
total_batch52 = []
total_batch53 = []
total_batch54 = []
total_batch55 = []
total_batch56 = []
total_batch57 = []
total_batch58 = []
total_batch59 = []
total_batch60 = []
total_batch61 = []
total_batch62 = []
total_batch63 = []
total_batch64 = []
total_batch65 = []
total_batch66 = []
total_batch67 = []
total_batch68 = []
total_batch69 = []
total_batch70 = []
total_batch71 = []
total_batch72 = []
total_batch73 = []
total_batch74 = []
total_batch75 = []
total_batch76 = []
total_batch77 = []
total_batch78 = []
total_batch79 = []
total_batch80 = []
total_batch81 = []
total_batch82 = []
total_batch83 = []
total_batch84 = []
total_batch85 = []
total_batch86 = []
total_batch87 = []
total_batch88 = []
total_batch89 = []
total_batch90 = []
total_batch91 = []
total_batch92 = []
total_batch93 = []
total_batch94 = []
total_batch95 = []
total_batch96 = []
total_batch97 = []
total_batch98 = []
total_batch99 = []
total_batch100 = []

def apply(L, f):
	"""
	Applies function given by f to each element in L
	Parameters
	----------
	L : list containing the operands
	f : the function
	Returns
	-------
	result: resulting list
	"""

	result = []
	for i in range(len(L)):
		result.append(f(L[i]))
 
	return result
def integers_batch(line):
	block_start_time = time.perf_counter()
	integer = 0
	item = ''
	#print(line.strip())
	#print(line)
	splitline = str(line).strip().split('|')
	CUI = splitline[0]
	word = splitline[14]
	item = CUI
	integer = int(CUI[1:])
	
	if 0 < integer < 150000:
		total_batch1.append(item)
		
	elif 150000 < integer < 300000:
		total_batch2.append(item)
		
	elif 300000 < integer < 450000:
		total_batch3.append(item)
		
	elif 450000 < integer < 600000:
		total_batch4.append(item)
		
	elif 600000 < integer < 750000:
		total_batch5.append(item)
		
	elif 750000 < integer < 900000:
		total_batch6.append(item)
		
	elif 900000 < integer < 1050000:
		total_batch7.append(item)
		
	elif 1050000 < integer < 1200000:
		total_batch8.append(item)
		
	elif 1200000 < integer < 1350000:
		total_batch9.append(item)
		
	elif 1350000 < integer < 1500000:
		total_batch10.append(item)
		
	elif 1500000 < integer < 1650000:
		total_batch11.append(item)
		
	elif 1650000 < integer < 1800000:
		total_batch12.append(item)
		
	elif 1800000 < integer < 1950000:
		total_batch13.append(item)
		
	elif 1950000 < integer < 2100000:
		total_batch14.append(item)
		
	elif 2100000 < integer < 2250000:
		total_batch15.append(item)
		
	elif 2250000 < integer < 2400000:
		total_batch16.append(item)
		
	elif 2400000 < integer < 2550000:
		total_batch17.append(item)
		
	elif 2550000 < integer < 2700000:
		total_batch18.append(item)
		
	elif 2700000 < integer < 2850000:
		total_batch19.append(item)
		
	elif 2850000 < integer < 3000000:
		total_batch20.append(item)
		
	elif 3000000 < integer < 3150000:
		total_batch21.append(item)
		
	elif 3150000 < integer < 3300000:
		total_batch22.append(item)
		
	elif 3300000 < integer < 3450000:
		total_batch23.append(item)
		
	elif 3450000 < integer < 3600000:
		total_batch24.append(item)
		
	elif 3600000 < integer < 3750000:
		total_batch25.append(item)
		
	elif 3750000 < integer < 3900000:
		total_batch26.append(item)
		
	elif 3900000 < integer < 4050000:
		total_batch27.append(item)
		
	elif 4050000 < integer < 4200000:
		total_batch28.append(item)
		
	elif 4200000 < integer < 4350000:
		total_batch29.append(item)
		
	elif 4350000 < integer < 4500000:
		total_batch30.append(item)
		
	elif 4500000 < integer < 4650000:
		total_batch31.append(item)
		
	elif 4650000 < integer < 4800000:
		total_batch32.append(item)
		
	elif 4800000 < integer < 4950000:
		total_batch33.append(item)
		
	elif 4950000 < integer < 5100000:
		total_batch34.append(item)
		
	elif 5100000 < integer < 5250000:
		total_batch35.append(item)
		
	elif 5250000 < integer < 5400000:
		total_batch36.append(item)
		
	elif 5400000 < integer < 5550000:
		total_batch37.append(item)
		
	elif 5550000 < integer < 5700000:
		total_batch38.append(item)
		
	elif 5700000 < integer < 5850000:
		total_batch39.append(item)
		
	elif 5850000 < integer < 6000000:
		total_batch40.append(item)
		
	elif 6000000 < integer < 6150000:
		total_batch41.append(item)
		
	elif 6150000 < integer < 6300000:
		total_batch42.append(item)
		
	elif 6300000 < integer < 6450000:
		total_batch43.append(item)
		
	elif 6450000 < integer < 6600000:
		total_batch44.append(item)
		
	elif 6600000 < integer < 6750000:
		total_batch45.append(item)
		
	elif 6750000 < integer < 6900000:
		total_batch46.append(item)
		
	elif 6900000 < integer < 7050000:
		total_batch47.append(item)
		
	elif 7050000 < integer < 7200000:
		total_batch48.append(item)
		
	elif 7200000 < integer < 7350000:
		total_batch49.append(item)
		
	elif 7350000 < integer < 7500000:
		total_batch50.append(item)
		
	elif 7500000 < integer < 7650000:
		total_batch51.append(item)
		
	elif 7650000 < integer < 7800000:
		total_batch52.append(item)
		
	elif 7800000 < integer < 7950000:
		total_batch53.append(item)
		
	elif 7950000 < integer < 8100000:
		total_batch54.append(item)
		
	elif 8100000 < integer < 8250000:
		total_batch55.append(item)
		
	elif 8250000 < integer < 8400000:
		total_batch56.append(item)
		
	elif 8400000 < integer < 8550000:
		total_batch57.append(item)
		
	elif 8550000 < integer < 8700000:
		total_batch58.append(item)
		
	elif 8700000 < integer < 8850000:
		total_batch59.append(item)
		
	elif 8850000 < integer < 9000000:
		total_batch60.append(item)
		
	elif 9000000 < integer < 9150000:
		total_batch61.append(item)
		
	elif 9150000 < integer < 9300000:
		total_batch62.append(item)
		
	elif 9300000 < integer < 9450000:
		total_batch63.append(item)
		
	elif 9450000 < integer < 9600000:
		total_batch64.append(item)
		
	elif 9600000 < integer < 9750000:
		total_batch65.append(item)
		
	elif 9750000 < integer < 9900000:
		total_batch66.append(item)
		
	elif 9900000 < integer < 10050000:
		total_batch67.append(item)
		
	elif 10050000 < integer < 10200000:
		total_batch68.append(item)
		
	elif 10200000 < integer < 10350000:
		total_batch69.append(item)
		
	elif 10350000 < integer < 10500000:
		total_batch70.append(item)
		
	elif 10500000 < integer < 10650000:
		total_batch71.append(item)
		
	elif 10650000 < integer < 10800000:
		total_batch72.append(item)
		
	elif 10800000 < integer < 10950000:
		total_batch73.append(item)
		
	elif 10950000 < integer < 11100000:
		total_batch74.append(item)
		
	elif 11100000 < integer < 11250000:
		total_batch75.append(item)
		
	elif 11250000 < integer < 11400000:
		total_batch76.append(item)
		
	elif 11400000 < integer < 11550000:
		total_batch77.append(item)
		
	elif 11550000 < integer < 11700000:
		total_batch78.append(item)
		
	elif 11700000 < integer < 11850000:
		total_batch79.append(item)
		
	elif 11850000 < integer < 12000000:
		total_batch80.append(item)
		
	elif 12000000 < integer < 12150000:
		total_batch81.append(item)
		
	elif 12150000 < integer < 12300000:
		total_batch82.append(item)
		
	elif 12300000 < integer < 12450000:
		total_batch83.append(item)
		
	elif 12450000 < integer < 12600000:
		total_batch84.append(item)
		
	elif 12600000 < integer < 12750000:
		total_batch85.append(item)
		
	elif 12750000 < integer < 12900000:
		total_batch86.append(item)
		
	elif 12900000 < integer < 13050000:
		total_batch87.append(item)
		
	elif 13050000 < integer < 13200000:
		total_batch88.append(item)
		
	elif 13200000 < integer < 13350000:
		total_batch89.append(item)
		
	elif 13350000 < integer < 13500000:
		total_batch90.append(item)
		
	elif 13500000 < integer < 13650000:
		total_batch91.append(item)
		
	elif 13650000 < integer < 13800000:
		total_batch92.append(item)
		
	elif 13800000 < integer < 13950000:
		total_batch93.append(item)
		
	elif 13950000 < integer < 14100000:
		total_batch94.append(item)
		
	elif 14100000 < integer < 14250000:
		total_batch95.append(item)
		
	elif 14250000 < integer < 14400000:
		total_batch96.append(item)
		
	elif 14400000 < integer < 14550000:
		total_batch97.append(item)
		
	elif 14550000 < integer < 14700000:
		total_batch98.append(item)
		
	elif 14700000 < integer < 14850000:
		total_batch99.append(item)
		
	elif 14850000 < integer < 15000000:
		total_batch100.append(item)
		

	block_end_time = time.perf_counter()
	end_time = time.perf_counter()

	print("this search took", block_end_time - block_start_time,"seconds")
	print("this script has run for", end_time - start_time,"seconds")



print('opening and reading MRCONSO RRF')
lines = []
filelines = open('/home/karl/UMLS/2020AB/META/MRCONSO.RRF', 'r')
for line in filelines:
	lines.append(str(line.strip()))
filelines.close()

for i in lines:
	integers_batch(i)

'''Define function to run mutiple processors and pool the results together'''



tbatch_list = 	[total_batch1, total_batch2, total_batch3, total_batch4, total_batch5, total_batch6, total_batch7, total_batch8,
				total_batch9, total_batch10, total_batch11, total_batch12, total_batch13, total_batch14, total_batch15, total_batch16,
				total_batch17, total_batch18, total_batch19,total_batch20, total_batch21, total_batch22,total_batch23, total_batch24,
				total_batch25, total_batch26,total_batch27, total_batch28, total_batch29, total_batch30,total_batch31, total_batch32,
				total_batch33, total_batch34, total_batch35, total_batch36, total_batch37,total_batch38, total_batch39, total_batch40,
				total_batch41, total_batch42, total_batch43, total_batch44, total_batch45, total_batch46, total_batch47, total_batch48,
				total_batch49, total_batch50, total_batch51, total_batch52, total_batch53, total_batch54, total_batch55, total_batch56,
				total_batch57, total_batch58, total_batch59, total_batch60, total_batch61, total_batch62, total_batch63, total_batch64,
				total_batch65, total_batch66, total_batch67, total_batch68, total_batch69, total_batch70, total_batch71, total_batch72,
				total_batch73,total_batch74, total_batch75, total_batch76, total_batch77, total_batch78, total_batch79,	total_batch80,
				total_batch81, total_batch82, total_batch83, total_batch84, total_batch85, total_batch86, total_batch87, total_batch88,
				total_batch89,total_batch90, total_batch91, total_batch92, total_batch93, total_batch94, total_batch95,	total_batch96,
				total_batch97, total_batch98, total_batch99, total_batch100]






final_tbatch_list = list(itertools.chain.from_iterable(tbatch_list))
tbatch_list = []
print(len(final_tbatch_list))



def f7(seq):
	seen = set()
	seen_add = seen.add
	return [x for x in seq if not (x in seen or seen_add(x))]



unique_list = f7(final_tbatch_list)
print(len(unique_list))

#for i in unique_list:
	#print(i)


final_tbatch_list = []

end_time = time.perf_counter()
print(end_time - start_time, " seconds to run this code")








# TO NOTE YOU WERE THINKING USING THE DEF APPLY FX TO USE WITH A LIST COMPREHENSION LIKE apply(L,f) where L is a list of str objects (i.e. lines in a file)
# THEN F PERFORMS A FX ON EACH LINE IN A LOOP FOR BATCHING - ?>?? MULTITHREAD?PROCESS




"""
f = open('/home/karl/UMLS/2020AB/META/MRCONSO.RRF', 'r') 
for line in f.readlines():
	#print(line)
	splitline = str(line).strip().split('|')
	CUI = splitline[0]
	word = splitline[14]
	integer = int(CUI[1:])
	print('starting run for: ', word, CUI, integer)
	print('starting multiprocessing')

	if __name__ == '__main__':
		[q() for q in ql, 10]:
			p = multiprocessing.Process(target=q)
			p.start()
f.close()
f = ''
"""







"""
ubatch_list = 	[unique_batch0, unique_batch1, unique_batch2, unique_batch3, unique_batch4, unique_batch5, unique_batch6, unique_batch7,
				unique_batch8, unique_batch9, unique_batch10, unique_batch11, unique_batch12, unique_batch13, unique_batch14, unique_batch15,
				unique_batch16, unique_batch17, unique_batch18, unique_batch19,unique_batch20, unique_batch21, unique_batch22,unique_batch23,
				unique_batch24, unique_batch25, unique_batch26,unique_batch27, unique_batch28, unique_batch29, unique_batch30,unique_batch31,
				unique_batch32, unique_batch33, unique_batch34, unique_batch35, unique_batch36, unique_batch37,unique_batch38, unique_batch39,
				unique_batch40, unique_batch41, unique_batch42, unique_batch43, unique_batch44, unique_batch45, unique_batch46, unique_batch47,
				unique_batch48, unique_batch49, unique_batch50, unique_batch51, unique_batch52, unique_batch53, unique_batch54, unique_batch55,
				unique_batch56, unique_batch57, unique_batch58, unique_batch59, unique_batch60, unique_batch61, unique_batch62, unique_batch63,
				unique_batch64, unique_batch65, unique_batch66, unique_batch67, unique_batch68, unique_batch69, unique_batch70, unique_batch71,
				unique_batch72, unique_batch73,unique_batch74, unique_batch75, unique_batch76, unique_batch77, unique_batch78, unique_batch79,
				unique_batch80, unique_batch81, unique_batch82, unique_batch83, unique_batch84, unique_batch85, unique_batch86, unique_batch87,
				unique_batch88, unique_batch89,unique_batch90, unique_batch91, unique_batch92, unique_batch93, unique_batch94, unique_batch95,
				unique_batch96, unique_batch97, unique_batch98, unique_batch99, unique_batch100]


final_ubatch_list = list(itertools.chain.from_iterable(ubatch_list))
ubatch_list = []

print(len(final_ubatch_list))
final_ubatch_list = []

"""





"""tbatch_list = 	[total_batch1, total_batch2, total_batch3, total_batch4, total_batch5, total_batch6, total_batch7, total_batch8,
				total_batch9, total_batch10, total_batch11, total_batch12, total_batch13, total_batch14, total_batch15, total_batch16,
				total_batch17, total_batch18, total_batch19,total_batch20, total_batch21, total_batch22,total_batch23, total_batch24,
				total_batch25, total_batch26,total_batch27, total_batch28, total_batch29, total_batch30,total_batch31, total_batch32,
				total_batch33, total_batch34, total_batch35, total_batch36, total_batch37,total_batch38, total_batch39, total_batch40,
				total_batch41, total_batch42, total_batch43, total_batch44, total_batch45, total_batch46, total_batch47, total_batch48,
				total_batch49, total_batch50, total_batch51, total_batch52, total_batch53, total_batch54, total_batch55, total_batch56,
				total_batch57, total_batch58, total_batch59, total_batch60, total_batch61, total_batch62, total_batch63, total_batch64,
				total_batch65, total_batch66, total_batch67, total_batch68, total_batch69, total_batch70, total_batch71, total_batch72,
				total_batch73,total_batch74, total_batch75, total_batch76, total_batch77, total_batch78, total_batch79,	total_batch80,
				total_batch81, total_batch82, total_batch83, total_batch84, total_batch85, total_batch86, total_batch87, total_batch88,
				total_batch89,total_batch90, total_batch91, total_batch92, total_batch93, total_batch94, total_batch95,	total_batch96,
				total_batch97, total_batch98, total_batch99, total_batch100]



final_tbatch_list = list(itertools.chain.from_iterable(tbatch_list))
tbatch_list = []


print(len(final_tbatch_list))
final_tbatch_list = []"""





"""
print('THERE ARE THIS MANY TOTAL CUIs in MRCONSO:')
print(sum(len(total_batch), len(total_batch2 ), len(total_batch3), len(total_batch4), len(total_batch5), 
	len(total_batch6), len(total_batch7), len(total_batch8), len(total_batch9), len(total_batch10), len(total_batch11),
	len(total_batch12), len(total_batch13), len(total_batch14), len(), len(total_batch15), len(total_batch16)))


print('FOR EACH BATCH OF CUIs IN RANGE OF 500K BATCHES, 16 BATCHES, FOR A MAX INTEGER OF 8,000,000, THERE ARE THIS MANY TOTAL CUIs in MRCONSO:')
print(len(total_batch), len(total_batch2 ), len(total_batch3), len(total_batch4), len(total_batch5), 
	len(total_batch6), len(total_batch7), len(total_batch8), len(total_batch9), len(total_batch10), len(total_batch11),
	len(total_batch12), len(total_batch13), len(total_batch14), len(), len(total_batch15), len(total_batch16))

print('THERE ARE THIS MANY UNIQUE CUIs in MRCONSO:')
print(sum(len(unique_batch), len(unique_batch2 ), len(unique_batch3), len(unique_batch4), len(unique_batch5), 
	len(unique_batch6), len(unique_batch7), len(unique_batch8), len(unique_batch9), len(unique_batch10), len(unique_batch11),
	len(unique_batch12), len(unique_batch13), len(unique_batch14), len(), len(unique_batch15), len(unique_batch16)))

print('FOR EACH BATCH OF CUIs IN RANGE OF 500K BATCHES, 16 BATCHES, FOR A MAX INTEGER OF 8,000,000, THERE ARE THIS MANY UNIQUE CUIs in MRCONSO:')
print(len(unique_batch), len(unique_batch2 ), len(unique_batch3), len(unique_batch4), len(unique_batch5), 
	len(unique_batch6), len(unique_batch7), len(unique_batch8), len(unique_batch9), len(unique_batch10), len(unique_batch11),
	len(unique_batch12), len(unique_batch13), len(unique_batch14), len(), len(unique_batch15), len(unique_batch16))
"""






#print('This many total in MRCONSO by line - not unique: ', len(CUIs))
# 7964596

#with open("./CUI_dictionary.txt", "w+") as f:
#	f.write(str(CUIs))

"""
#MRCONSO - interate over file
import ast
file = open("CUI_dictionary.txt", "r")

contents = file.read()
dictionary = ast.literal_eval(contents)

file.close()
print(len(dictionary))
"""
"""
def unique(list1):
 
		# intilize a null list
		unique_list = []
		 
		# traverse for all elements
		for x in list1:
				print(x)
				# check if exists in unique_list or not
				if x not in unique_list:
						unique_list.append(x)
		# print list
		print('This many unique in MRCONSO by unique list fx: ', len(unique_list))

		with open ('unique_CUI_list.txt', 'w+') as f2:
			f2.write(unique_list) # write to file so we don't have to do this again

unique(CUIs)
"""
"""
f = open('/home/karl/UMLS/2020AB/META/MRCONSO.RRF', 'r') 
count = 0
for line in f.readlines():
	#print(line)
	splitline = str(line).strip().split('|')
	CUI = splitline[0]
	AUI = splitline[7]
	word = splitline[14]
	count = count + 1
	print(CUI, AUI, word)
	print(count)

f.close()
"""



#read dictionary file

#print(type(dictionary))


##################################################################################################################################################

"""
#MRDEF - interate over file
f = open('/home/karl/UMLS/2020AB/META/MRDEF.RRF', 'r') 
count = 0
for line in f.readlines():
	#print(line)
	splitline = str(line).strip().split('|')
	CUI = splitline[0]
	AUI = splitline[1]
	definition = splitline[5]
	count = count + 1
	print(CUI, AUI, definition)
	print(count)

f.close()
"""

##################################################################################################################################################
"""
#MRHIER 
atoms = {}

f = open('/home/karl/UMLS/2020AB/META/MRHIER.RRF', 'r') 
count = 0
for line in f.readlines():
	count = count + 1
	print(count)
	print(line)
	splitline = line.split('|')
	CUI = splitline[0]
	atom = splitline[1]
	print(CUI, atom)
	#if not atom in CUIs:
	#	CUIs[CUI] = []
f.close()
"""