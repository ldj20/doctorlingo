import time
start_time = time.perf_counter()
import dask
import dask.dataframe as dd
import cudf
import dask.multiprocessing
dask.config.set(scheduler='processes')
df = dd.read_csv('./DL_UMLS_modified/MRCONSO.RRF',sep='|')
df
#CUI_Atom_String_dataframe = df.loc[0:, ['CUI', 'AUI', 'STR']].groupby(['CUI']).collect()
#print(CUI_Atom_String_dataframe)
print(df)
CID = (df['CUI']).compute()
print(CID)
end_time = time.perf_counter()
print("this script has run for", end_time - start_time,"seconds")

