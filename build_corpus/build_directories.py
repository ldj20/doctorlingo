import os

os.mkdir('./dynamic_corpus')

os.mkdir('./dynamic_corpus/UMLS')

os.mkdir('./dynamic_corpus/UMLS/dictionary_lookups')

os.mkdir('./dynamic_corpus/UMLS/UMLS_file_descriptions')

os.mkdir('./dynamic_corpus/UMLS/UMLS_organized')

os.mkdir('./dynamic_corpus/UMLS/UMLS_organized/unique_batches')

os.mkdir('./dynamic_corpus/UMLS/UMLS_organized/MRCONSO_batched')

os.mkdir('./dynamic_corpus/UMLS/UMLS_organized/MRDEF_batched')

os.mkdir('./dynamic_corpus/UMLS/UMLS_organized/MRHIER_batched')

os.mkdir('./dynamic_corpus/UMLS/UMLS_organized/MRSAT_batched')

os.mkdir('./dynamic_corpus/UMLS/UMLS_organized/MRSTY_batched')

os.mkdir('./dynamic_corpus/UMLS/UMLS_organized/MRREL_batched')


for i in range(1, 55): # 55 as we are indexing from zero with range fx
    # makeadir('') evaluates your condition
   os.mkdir('./dynamic_corpus/UMLS/UMLS_organized/unique_batches/batch%s' % str(i))


   