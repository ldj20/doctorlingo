import time
start_time = time.perf_counter()
import itertools

import json

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

zs = []
for i in lines:
	z = integers_batch(i)
	zs.append(z)

zs = dask.persist(*zs)  # trigger computation in the background

client.cluster.scale(10)  # ask for ten 4-thread workers

L = zs
while len(L) > 1:
    new_L = []
    for i in range(0, len(L), 2):
        lazy = add(L[i], L[i + 1])  # add neighbors
        new_L.append(lazy)
    L = new_L                       # swap old list for new

dask.compute(L)

'''Define function to run mutiple processors and pool the results together'''

print('creating unique lists')
end_time = time.perf_counter()
print(end_time - start_time, " seconds to run this code")


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


print('creating dictionary pickles')
end_time = time.perf_counter()
print(end_time - start_time, " seconds to run this code")

def create_file_unique_batch1(unique_batch1)
	CUIs = {}
	for i in unique_batch1:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch1_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch1_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)


def create_file_unique_batch2(unique_batch2)
	CUIs = {}
	for i in unique_batch2:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch2_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch2_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)

####################################################################################
def create_file_unique_batch3(unique_batch3)
	CUIs = {}
	for i in unique_batch3:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch3_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch3_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)

####################################################################################
def create_file_unique_batch4(unique_batch4)
	CUIs = {}
	for i in unique_batch4:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch4_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch4_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)

####################################################################################
def create_file_unique_batch5(unique_batch5)
	CUIs = {}
	for i in unique_batch5:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch5_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch5_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)

####################################################################################
def create_file_unique_batch6(unique_batch6)
	CUIs = {}
	for i in unique_batch6:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch6_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch6_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)

####################################################################################
def create_file_unique_batch7(unique_batch7)
	CUIs = {}
	for i in unique_batch7:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch7_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch7_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)

####################################################################################
def create_file_unique_batch8(unique_batch8)
	CUIs = {}
	for i in unique_batch8:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch8_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch8_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)

####################################################################################
def create_file_unique_batch9(unique_batch9)
	CUIs = {}
	for i in unique_batch9:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch9_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch9_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)

####################################################################################
def create_file_unique_batch10(unique_batch10)
	CUIs = {}
	for i in unique_batch10:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch10_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch10_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)

####################################################################################
def create_file_unique_batch11(unique_batch11)
	CUIs = {}
	for i in unique_batch11:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch11_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch11_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)

####################################################################################
def create_file_unique_batch12(unique_batch12)
	CUIs = {}
	for i in unique_batch12:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch12_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch12_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)

####################################################################################
def create_file_unique_batch13(unique_batch13)
	CUIs = {}
	for i in unique_batch13:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch13_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch13_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)

####################################################################################
def create_file_unique_batch14(unique_batch14)
	CUIs = {}
	for i in unique_batch14:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch14_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch14_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)

####################################################################################
def create_file_unique_batch15(unique_batch15)
	CUIs = {}
	for i in unique_batch15:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch15_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch15_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)

####################################################################################
def create_file_unique_batch16(unique_batch16)
	CUIs = {}
	for i in unique_batch16:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch16_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch16_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)

####################################################################################
def create_file_unique_batch17(unique_batch17)
	CUIs = {}
	for i in unique_batch17:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch17_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch17_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)

####################################################################################
def create_file_unique_batch18(unique_batch18)
	CUIs = {}
	for i in unique_batch18:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch18_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch18_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)

####################################################################################
def create_file_unique_batch19(unique_batch19)
	CUIs = {}
	for i in unique_batch19:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch19_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch19_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)

####################################################################################
def create_file_unique_batch20(unique_batch20)
	CUIs = {}
	for i in unique_batch20:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch20_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch20_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)

####################################################################################
def create_file_unique_batch21(unique_batch21)
	CUIs = {}
	for i in unique_batch21:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch21_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch21_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)

####################################################################################
def create_file_unique_batch22(unique_batch22)
	CUIs = {}
	for i in unique_batch22:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch22_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch22_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)

####################################################################################
def create_file_unique_batch23(unique_batch23)
	CUIs = {}
	for i in unique_batch23:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch23_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch23_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)

####################################################################################
def create_file_unique_batch24(unique_batch24)
	CUIs = {}
	for i in unique_batch24:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch24_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch24_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)

####################################################################################
def create_file_unique_batch25(unique_batch25)
	CUIs = {}
	for i in unique_batch25:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch25_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch25_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)

####################################################################################
def create_file_unique_batch26(unique_batch26)
	CUIs = {}
	for i in unique_batch26:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch26_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch26_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)

####################################################################################
def create_file_unique_batch27(unique_batch27)
	CUIs = {}
	for i in unique_batch27:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch27_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch27_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)

####################################################################################
def create_file_unique_batch28(unique_batch28)
	CUIs = {}
	for i in unique_batch28:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch28_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch28_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)

####################################################################################
def create_file_unique_batch29(unique_batch29)
	CUIs = {}
	for i in unique_batch29:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch29_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch29_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)

####################################################################################
def create_file_unique_batch30(unique_batch30)
	CUIs = {}
	for i in unique_batch30:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch30_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch30_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)

####################################################################################
def create_file_unique_batch31(unique_batch31)
	CUIs = {}
	for i in unique_batch31:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch31_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch31_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)

####################################################################################
def create_file_unique_batch32(unique_batch32)
	CUIs = {}
	for i in unique_batch32:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch32_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch32_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)

####################################################################################
def create_file_unique_batch33(unique_batch33)
	CUIs = {}
	for i in unique_batch33:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch33_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch33_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)

####################################################################################
def create_file_unique_batch34(unique_batch34)
	CUIs = {}
	for i in unique_batch34:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch34_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch34_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)

####################################################################################
def create_file_unique_batch35(unique_batch35)
	CUIs = {}
	for i in unique_batch35:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch35_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch35_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)

####################################################################################
def create_file_unique_batch36(unique_batch36)
	CUIs = {}
	for i in unique_batch36:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch36_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch36_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)

####################################################################################
def create_file_unique_batch37(unique_batch37)
	CUIs = {}
	for i in unique_batch37:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch37_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch37_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)

####################################################################################
def create_file_unique_batch38(unique_batch38)
	CUIs = {}
	for i in unique_batch38:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch38_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch38_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)

####################################################################################
def create_file_unique_batch39(unique_batch39)
	CUIs = {}
	for i in unique_batch39:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch39_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch39_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)

####################################################################################
def create_file_unique_batch40(unique_batch40)
	CUIs = {}
	for i in unique_batch40:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch40_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch40_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)

####################################################################################
def create_file_unique_batch41(unique_batch41)
	CUIs = {}
	for i in unique_batch41:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch41_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch41_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)

####################################################################################
def create_file_unique_batch42(unique_batch42)
	CUIs = {}
	for i in unique_batch42:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch42_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch42_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)

####################################################################################
def create_file_unique_batch43(unique_batch43)
	CUIs = {}
	for i in unique_batch43:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch43_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch43_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)

####################################################################################
def create_file_unique_batch44(unique_batch44)
	CUIs = {}
	for i in unique_batch44:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch44_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch44_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)

####################################################################################
def create_file_unique_batch45(unique_batch45)
	CUIs = {}
	for i in unique_batch45:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch45_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch45_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)

####################################################################################
def create_file_unique_batch46(unique_batch46)
	CUIs = {}
	for i in unique_batch46:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch46_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch46_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)

####################################################################################
def create_file_unique_batch47(unique_batch47)
	CUIs = {}
	for i in unique_batch47:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch47_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch47_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)

####################################################################################
def create_file_unique_batch48(unique_batch48)
	CUIs = {}
	for i in unique_batch48:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch48_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch48_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)

####################################################################################
def create_file_unique_batch49(unique_batch49)
	CUIs = {}
	for i in unique_batch49:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch49_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch49_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)

####################################################################################
def create_file_unique_batch50(unique_batch50)
	CUIs = {}
	for i in unique_batch50:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch50_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch50_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)

####################################################################################
def create_file_unique_batch51(unique_batch51)
	CUIs = {}
	for i in unique_batch51:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch51_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch51_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)

####################################################################################
def create_file_unique_batch52(unique_batch52)
	CUIs = {}
	for i in unique_batch52:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch52_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch52_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)

####################################################################################
def create_file_unique_batch53(unique_batch53)
	CUIs = {}
	for i in unique_batch53:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch53_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch53_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)

####################################################################################
def create_file_unique_batch54(unique_batch54)
	CUIs = {}
	for i in unique_batch54:
		if not i in CUIs:
			CUIs[i] = []
	name = 'batch54_dictionary'
	file = './dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch54_dictionary.json'
	with open(file, 'w') as o:
		json.dump(CUIs,o)

####################################################################################

CUIs = {}
name = ''
file = ''


create_file_unique_batch1(unique_batch1)
create_file_unique_batch2(unique_batch2)
create_file_unique_batch3(unique_batch3)
create_file_unique_batch4(unique_batch4)
create_file_unique_batch5(unique_batch5)
create_file_unique_batch6(unique_batch6)
create_file_unique_batch7(unique_batch7)
create_file_unique_batch8(unique_batch8)
create_file_unique_batch9(unique_batch9)
create_file_unique_batch10(unique_batch10)
create_file_unique_batch11(unique_batch11)
create_file_unique_batch12(unique_batch12)
create_file_unique_batch13(unique_batch13)
create_file_unique_batch14(unique_batch14)
create_file_unique_batch15(unique_batch15)
create_file_unique_batch16(unique_batch16)
create_file_unique_batch17(unique_batch17)
create_file_unique_batch18(unique_batch18)
create_file_unique_batch19(unique_batch19)
create_file_unique_batch20(unique_batch20)
create_file_unique_batch21(unique_batch21)
create_file_unique_batch22(unique_batch22)
create_file_unique_batch23(unique_batch23)
create_file_unique_batch24(unique_batch24)
create_file_unique_batch25(unique_batch25)
create_file_unique_batch26(unique_batch26)
create_file_unique_batch27(unique_batch27)
create_file_unique_batch28(unique_batch28)
create_file_unique_batch29(unique_batch29)
create_file_unique_batch30(unique_batch30)
create_file_unique_batch31(unique_batch31)
create_file_unique_batch32(unique_batch32)
create_file_unique_batch33(unique_batch33)
create_file_unique_batch34(unique_batch34)
create_file_unique_batch35(unique_batch35)
create_file_unique_batch36(unique_batch36)
create_file_unique_batch37(unique_batch37)
create_file_unique_batch38(unique_batch38)
create_file_unique_batch39(unique_batch39)
create_file_unique_batch40(unique_batch40)
create_file_unique_batch41(unique_batch41)
create_file_unique_batch42(unique_batch42)
create_file_unique_batch43(unique_batch43)
create_file_unique_batch44(unique_batch44)
create_file_unique_batch45(unique_batch45)
create_file_unique_batch46(unique_batch46)
create_file_unique_batch47(unique_batch47)
create_file_unique_batch48(unique_batch48)
create_file_unique_batch49(unique_batch49)
create_file_unique_batch50(unique_batch50)
create_file_unique_batch51(unique_batch51)
create_file_unique_batch52(unique_batch52)
create_file_unique_batch53(unique_batch53)
create_file_unique_batch54(unique_batch54)


end_time = time.perf_counter()
print(end_time - start_time, " seconds to run this code")


