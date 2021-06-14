import time
start_time = time.perf_counter()

f = open('./DL_UMLS_modified/MRCONSO.RRF', 'r')

for line in f:
	print(line.strip('\n'))

end_time = time.perf_counter()
print(end_time - start_time, " seconds to run this code")
"""

for j in array:
	f2.write(j)
	print(j)

end_time = time.perf_counter()

print(end_time - start_time, " seconds to run this code")
"""
"""
j = 0
k = 150000
for i in range(0, 100):

	l = int(i) + 1
	print("@dask.delayed")
	print("def integers_batch%s(line, total_batch%s):" % (l,l))
	print("\tinteger = 0")
	print("\titem = ''")
	print("\tsplitline = str(line).strip().split('|')")
	print("\tCUI = splitline[0]")
	print("\tISPREF = splitline[6]")
	print("\tAUI = splitline[7]")
	print("\tword = splitline[14]")
	print("\titem = CUI")
	print("\tprint(item)")
	print("\tinteger = int(CUI[1:])")
	print("\tif %s < integer < %s:" % (j,k))
	print("\t\ttotal_batch%s.append(item)" % l)
	print("\treturn total_batch%s" % l)

	j = j + 150000
	k = k + 150000
"""

"""
for i in range(0, 100):

	l = int(i) + 1

	print("integers_batch%s(line, total_batch%s)" % (l,l))
"""