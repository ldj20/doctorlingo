import time
start_time = time.perf_counter()
import dask
from dask.distributed import Client, wait
cluster = LocalCUDACluster()
client = Client(cluster)
client
import cupy as cp
import pandas as pd
import cudf
import dask_cudf
from alive_progress import alive_bar



#with alive_bar(8) as bar:

ddcudf1 = dask_cudf.read_csv('./DL_UMLS_modified/MRCONSO.RRF',sep='|')
ddcudf1 = ddcudf1.compute()
g1_ddcudf = ddcudf1.groupby('AUI')['CUI'].agg(['unique']).to_pandas()
g2_ddcudf = ddcudf1.groupby('AUI')['STR'].agg(['unique']).to_pandas()


ddcudf2 = dask_cudf.read_csv('./DL_UMLS_modified/MRDEF.RRF',sep='|')
ddcudf2 = ddcudf2.compute()
g3_ddcudf = ddcudf2.groupby('AUI')['DEF'].agg(['unique']).to_pandas()
#print(g3_ddcudf)

df3 = g1_ddcudf.merge(g2_ddcudf, on='AUI', how='outer') ##.compute()

df3 = df3.rename(columns={"unique_x": "CUI", "unique_y": "DEFINITION"})
df3 df3.columns

#df4 = df3.merge(g3_ddcudf, on='CUI', how='outer')
#print(df4)
"""
#CUI|AUI|CXN|PAUI|SAB|RELA|PTR|HCD|CVF
ddcudf3 = dask_cudf.read_csv('./DL_UMLS_modified/MRDEF.RRF',sep='|')
ddcudf3 = ddcudf2.compute()
g3_ddcudf = ddcudf2.groupby('AUI')['DEF'].agg(['unique']).to_pandas()
#print(g3_ddcudf)

df3 = g1_ddcudf.merge(g2_ddcudf, on='CUI', how='outer') ##.compute()
df4 = df3.merge(g3_ddcudf, on='CUI', how='outer')
print(df4)
"""
#ddcudf3 = dask_cudf(g1_ddcudf, npartitions=10).compute()

#print(df3)

#print(g1_ddcudf)
#print(g2_ddcudf)


#df = ddcudf1.groupby('c')['l1','l2'].agg(['unique'])
#.loc[0:, ['CUI','AUI', 'STR']].groupby(['CUI'])
#df1 = df1.loc[0:, ['CUI','AUI', 'STR']].groupby(['CUI'])

#bar()
#df2 = dask_cudf.read_csv('./DL_UMLS_modified/MRDEF.RRF',sep='|', npartitions=6)
#bar()
#df2 = df2.loc[0:, ['CUI','DEF']].groupby(['CUI']) #.to_pandas()

#bar()
# ^, familiar right? if not you skipped ahead, go to block 1, sucka.
#df3 = df1.merge(df2, on='CUI', how='outer').compute()
#print(df3)



#bar()
#print(df3)
#df3 = df3.groupby('CUI').collect().reset_index(level=None, drop=False, inplace=False, col_level=0)

#bar()
#print(df3)

#dd1 = from_pandas(df3, npartitions=3).compute() #THE DASK DDF
#df4 = dask_cudf.DataFrame(df3)


#results = [df1, df2, df3, df4]
#results.compute()
#bar()


#df5 = cudf.read_csv('./DL_UMLS_modified/MRDEF.RRF',sep='|')

#FOR WHEN YOU NEED TO EXPORT TO CSV OR WHAT EVER FILE NEED TO CONVERT TO PANDAS
	#pd4 = df4.to_pandas()
	#bar()

# TO PRINT A SINGLE ITEM FROM A LIST W/IN DATAFRAME SERIES:
#for i in df4.AUI.to_pandas().get(4)[0]:
#	print(i)
	
#print(df3['STR'])
#print(df3['DEF'])

#THE ABOVE TAKES THE MRDEF CSV READS TO CUDF DF, MERGES W/ MRCONSO CUDF -> DASK TO TEST CSV EXPORT
# -> CUDF? PROBS BC I NEED TO PULL MOAR!

#print(dd1)


#rint(dd.from_pandas(df3, npartitions=8).repartition())

#pd.DataFrame.to_csv(df3, path_or_buf='./test.csv', sep='\t', header=0, index=False, line_terminator='\n', chunksize=None, encoding=None, compression=None)


#abc = df.loc[0:, ['CUI', 'DEF']].groupby(['CUI']).collect().reset_index()
#print(abc.add_column('CUI', CUI_Atom_String_dataframe['CUI']))
#print(CUI_Atom_String_dataframe.insert()

# On writing JSON
# https://docs.rapids.ai/api/cudf/stable/api.html
# cudf.io.json.read_json
# On reading JSON
#cudf.io.json.read_json(path_or_buf, engine='auto', dtype=True, lines=False, compression='infer', byte_range=None, *args, **kwargs)



#
#CUI_series = df[df.columns[0]].unique().to_arrow().to_pylist()
#df2 = cudf.DataFrame(CUI_series, columns=['CUI'])
#print(df2)
#print(len(df2))

#for i in df.loc[0:7867273, ['CUI', 'AUI', 'STR']].to_arrow().to_pylist():
#	print(i)


#print(df.grouby(columns[0]))
	



# YOU WERE ABLE TO EXTRACT ALL UNIQUE CUIS FROM MRCONSO WITH CUDF DATA FRAME TO ANOTHER CUDF DATAFRAME TO STORE UNIQUE CUIS TO NEW COLUMN NOW NEED TO MAP AUIs + WORDS/PHRASES
#print(len(df[df.columns[0]]))
#print(len(df[df.columns[0]].unique()))
#print(df.loc[0:3489765, ['CUI', 'AUI', 'STR']])

#for i in df.loc[0:7867273, 'CUI', 'AUI', 'STR'].to_arrow():
#	print(i)

#print(df.columns[0].str.contains[])

#print(df.merge(df, left_on='AUI', right_on='STR', how='left'))


#unique_CUI_list = df[df.columns[0]].unique().to_arrow().to_pylist()





# the above was formatted per error code when attempting "tolist() methods:
# cuDF does not support conversion to host memory "
# TypeError: cuDF does not support conversion to host memory via `tolist()` method. Consider using `.to_arrow().to_pylist()` to construct a Python list.

# important NVIDIA document: https://images.nvidia.com/aem-dam/Solutions/ai-data-science/rapids-kit/accelerated-data-science-print-getting-started-cheat-sheets.pdf

#ddf = cudf.DataFrame()
#ddf['key'] = [x for x in range(len(df[df.columns[0]].unique()))]
#ddf['value'] = [x for x in unique_CUI_list]

#print(ddf)

#end_time = time.perf_counter()
#print("this script has run for", end_time - start_time,"seconds")


"""
final_df = cudf.DataFrame(
   	columns=["CUI"]
)

print(final_df)
"""

#dataframetolist https://www.kite.com/python/answers/how-to-return-a-column-of-a-pandas-dataframe-as-a-list-in-python

"""

end_time = time.perf_counter()
print("this script has run for", end_time - start_time,"seconds")

IMPORTANT:
import cudf

df = df.map_partitions(cudf.from_pandas)

"""
#print('Reading text file to dataframe aka a bag in dask')


# note your dbag is not a regular python list - thus has no length
# to create a list use: dbag_as_list = dbag.compute()
"""

with ProgressBar():
	print('iterating over the dask bag as a list for each line in text file')
	for i in dbag_as_list:
		item = ''
		dask.delayed(integers_batch)(i)

		print(item)
"""




#with ProgressBar():

"""

import pandas as pd
import dask 
import dask.dataframe as dd

 def to_lower(text):
        return text.lower()

df_2016 = pd.read_csv("2016_Cleaned_DroppedDup.csv")
df_2016['token2'] = df_2016['token2'].apply(lambda x: pr.to_lower(x))

shit version ^^^^


goodvesion ->

import pandas as pd
import dask.dataframe as dd

def to_lower(text):
    return text.lower()

# using pandas
df = pd.DataFrame({'token2':['HI']*100 + ['YOU']*100})
df = df_2016['token2'].str.lower()
df['token2_low_apply'] = df_2016['token2'].apply(to_lower)
df_2016

    token2 token2_low token2_low_apply
0       HI         hi               hi
1       HI         hi               hi
2       HI         hi               hi
3       HI         hi               hi
4       HI         hi               hi
..     ...        ...              ...
195    YOU        you              you
196    YOU        you              you
197    YOU        you              you
198    YOU        you              you
199    YOU        you              you

[200 rows x 3 columns]

# using dask
ddf_2016 = dd.from_pandas(df_2016[['token2']], npartitions=10)
ddf_2016['token2_low'] = ddf_2016['token2'].str.lower()
ddf_2016['token2_low_apply'] = ddf_2016['token2'].apply(to_lower, meta=('token2', 'object'))

ddf_2016.compute()"""





# Using cudf/dask we save a lot of time
# For example it takes about 70 seconds to read and print the MRCONSO.RRF
# with a simple for loop in python. With reading it into a dask datafram
# it take 17 seconds. Nearly a x4 speed up! With a cuda datafram "cudf"...
# 1 second, or a 70 fold reduction.

########################################################################################



# IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT
# How to find all information associated with a particular UMLS concept (CUI value)
# How to find all information associated with a particular UMLS concept (CUI value)
# YOU SHOULD INSERT THIS INTO EVERY CODE BLOCK AS A REMINDER OF GOAL
#
# 1. Find all atoms of a UMLS concept.
# 2. Find all source definitions associated with a UMLS concept.
# 3. Find all source contexts associated with a UMLS concept.
# 4. Find all attributes for a UMLS concept.
# 5. Find all semantic types for a UMLS concept.
# 6.a. Find all relationships for a UMLS concept.
# 6.b. Find all inverse relationships for a UMLS concept.
# 7. Find all relationships for a concept and the preferred (English) name of the CUI2.
#
# https://www.nlm.nih.gov/research/umls/implementation_resources/query_diagrams/er1.html
#
# 1. Find all atoms of a UMLS concept.
# 2. Find all source definitions associated with a UMLS concept.
# 3. Find all source contexts associated with a UMLS concept.
# 4. Find all attributes for a UMLS concept.
# 5. Find all semantic types for a UMLS concept.
# 6.a. Find all relationships for a UMLS concept.
# 6.b. Find all inverse relationships for a UMLS concept.
# 7. Find all relationships for a concept and the preferred (English) name of the CUI2.
#
# YOU SHOULD INSERT THIS INTO EVERY CODE BLOCK AS A REMINDER OF GOAL
# How to find all information associated with a particular UMLS concept (CUI value)
# How to find all information associated with a particular UMLS concept (CUI value)
# How to find all information associated with a particular UMLS concept (CUI value)
# IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT



########################################################################################
# Block #1
# This block of code opens the MRCONSO file to build base of UMLS structure for corpus
# MRCONSO is the base file for UMLS metathesaurus, it houses terms for every "atom" aka
# a synonym. Atoms are words/phrases linked to the "concept" CUI - the central, linking
# definition for these synonyms per UMLS. 
# Remember from 5th grade: synonyms = dif words w/ = meaning.
# In two lines of code (1/6th this doc for the two lines - the power of cudf), we will:
# We will sort this file to generate an index by unique CUIs as this is the building
# block for all other relationships for all medical words/phrases in UMLS, aka atoms.
# We will then assign all related atom IDs (AUIs) w/ their respective CUIs in the table,
# as well as the actual word the AUI represents. Keep in mind there is a "preferred" atom
# for every concept, the same way we all have preference for certain synonyms in our
# own diction to represent the concepts we use to speak. Okay, done with linguistics.
########################################################################################

# Opens file MRCONSO.RRF which is an ugly pipe-delimited file w/ lines that look like:
#
# C0000005|ENG|P||L0000005|PF|S0007492|PEP|D012711|(131)I-Macroaggregated Albumin|0|N|256.0
# ... (x 7.8 million more rows of this)
# This gets read into a cudf dataframe 'df', which is just the above in tabular table format
# But it is now entirely indexed, searchable and modifiable in under a second on my PC.
# Performing an action above also takes about one second per action for THE ENTIRE DF.
# As below:


#df1 = df1.to_pandas()

 # free up GPU memory
# This stores to a variable... lol literally all of the following, cudf is wild.
# So... with the pipe-delim file from above, sorted into a tabbed dataframe.
# With the cudf.loc() f(x), we return a new completely sorted df/table from the read file.
# Then you see can see the total syntax of the function is: 
# .loc[starting row index: end row index, ['Names', 'of', 'various','colums']]
# The "cudf.groupby(['clmn name'])" method - indexes the new cudf df by CUI and pulls 
# the three listed columns, and also is a prerequesite for the collect f(x).
# The .collect() function, while keeping primary index w/ CUI column, re-indexes by 
# the AUI column. So now in the first column we have an index of CUIs in order ascending to descending.
# The next column #2 has all returned AUIs, however sorted and binned to their respect CUI row.
# Finally the words/phrases associated with the CUI are in column #3 and if its the preferred AUI
# in is in column #4.

# In two lines of code, you did all of that to MRCONSO.RRF, a 7.8 million line and 18 column table
# file that is 1 GB in size - on my machine this takes ~1s to load the file. And ~1s to parse.

# Okay the rest of this codes documentation will be briefer but, I just wanted to point
# out how awesome cudf, dask, pandas etc are if you haven't used them. And give a thorough
# example in case you re-build or modify.

########################################################################################
# End block 1 
########################################################################################

########################################################################################
########################################################################################
# Block 2: now that we've got all the unique *active CUIs with some synonyms
# Let's extract some UMLS definitions and map them to the baby corpus, aw.
# You may be thinking, wait a minute there's only 3.5 million ish CUIs but 7.8 million
# AUIs? Remember - AUIs = synonyms = same definition = same CUI. So definitions belong to 
# CUIs and the *preferred AUI* term for the CUI - concept/definition is the "word/phrase"
# used in natural english language to refer to a CUI. Aight.
#
# (one exception: you will see repeated CUI/AUIs in this MRDEF for defs in other languages
# for version 1 I am just building out English)
