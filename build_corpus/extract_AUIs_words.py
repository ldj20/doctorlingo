import time
start_time = time.perf_counter()
import itertools


from math import exp

import dask
dask.config.set(scheduler='threads')  

print('defining variables and functions')

def f7(seq):
	seen = set()
	seen_add = seen.add
	return [x for x in seq if not (x in seen or seen_add(x))]


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


def integers_batch(line):
	block_start_time = time.perf_counter()
	integer = 0
	item = ''
	#print(line.strip())
	#print(line)
	splitline = str(line).strip().split('|')
	CUI = splitline[0]
	ISPREF = splitline[6]
	AUI = splitline[7]
	word = splitline[14]
	item = CUI+'|'+'ISPREF-'+ISPREF+'~AUI-'+AUI+'~word-'+word
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


unique_batch1 = f7(total_batch1)
unique_batch2 = f7(total_batch2)
unique_batch3 = f7(total_batch3)
unique_batch4 = f7(total_batch4)
unique_batch5 = f7(total_batch5)
unique_batch6 = f7(total_batch6)
unique_batch7 = f7(total_batch7)
unique_batch8 = f7(total_batch8)
unique_batch9 = f7(total_batch9)
unique_batch10 = f7(total_batch10)
unique_batch11 = f7(total_batch11)
unique_batch12 = f7(total_batch12)
unique_batch13 = f7(total_batch13)
unique_batch14 = f7(total_batch14)
unique_batch15 = f7(total_batch15)
unique_batch16 = f7(total_batch16)
unique_batch17 = f7(total_batch17)
unique_batch18 = f7(total_batch18)
unique_batch19 = f7(total_batch19)
unique_batch20 = f7(total_batch20)
unique_batch21 = f7(total_batch21)
unique_batch22 = f7(total_batch22)
unique_batch23 = f7(total_batch23)
unique_batch24 = f7(total_batch24)
unique_batch25 = f7(total_batch25)
unique_batch26 = f7(total_batch26)
unique_batch27 = f7(total_batch27)
unique_batch28 = f7(total_batch28)
unique_batch29 = f7(total_batch29)
unique_batch30 = f7(total_batch30)
unique_batch31 = f7(total_batch31)
unique_batch32 = f7(total_batch32)
unique_batch33 = f7(total_batch33)
unique_batch34 = f7(total_batch34)
unique_batch35 = f7(total_batch35)
unique_batch36 = f7(total_batch36)
unique_batch37 = f7(total_batch37)
unique_batch38 = f7(total_batch38)
unique_batch39 = f7(total_batch39)
unique_batch40 = f7(total_batch40)
unique_batch41 = f7(total_batch41)
unique_batch42 = f7(total_batch42)
unique_batch43 = f7(total_batch43)
unique_batch44 = f7(total_batch44)
unique_batch45 = f7(total_batch45)
unique_batch46 = f7(total_batch46)
unique_batch47 = f7(total_batch47)
unique_batch48 = f7(total_batch48)
unique_batch49 = f7(total_batch49)
unique_batch50 = f7(total_batch50)
unique_batch51 = f7(total_batch51)
unique_batch52 = f7(total_batch52)
unique_batch53 = f7(total_batch53)
unique_batch54 = f7(total_batch54)







tbatch_list = 	[total_batch1, total_batch2, total_batch3, total_batch4, total_batch5, total_batch6, total_batch7, total_batch8,
				total_batch9, total_batch10, total_batch11, total_batch12, total_batch13, total_batch14, total_batch15, total_batch16,
				total_batch17, total_batch18, total_batch19,total_batch20, total_batch21, total_batch22,total_batch23, total_batch24,
				total_batch25, total_batch26,total_batch27, total_batch28, total_batch29, total_batch30,total_batch31, total_batch32,
				total_batch33, total_batch34, total_batch35, total_batch36, total_batch37,total_batch38, total_batch39, total_batch40,
				total_batch41, total_batch42, total_batch43, total_batch44, total_batch45, total_batch46, total_batch47, total_batch48,
				total_batch49, total_batch50, total_batch51, total_batch52, total_batch53, total_batch54]

final_tbatch_list = list(itertools.chain.from_iterable(tbatch_list))
tbatch_list = []
print(len(final_tbatch_list))

unique_list = f7(final_tbatch_list)
print(len(unique_list))

#for i in unique_list:
	#print(i)


final_tbatch_list = []

end_time = time.perf_counter()
print(end_time - start_time, " seconds to run this code")


