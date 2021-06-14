# Building the Corpus

This is in progress. In short me and Saadh are using dask-cudf to generate a dataframe of all UMLS entries for every language. We are then going to extract all the hypernym relationships from this. We will then switch focus to build the hypernymy model. The original hypernymy model was developed on a test wikipedia corpus. Using the UMLS is_a relationship we can actually find all hypernym relationships in the UMLS both from immediate parent child and all descendents. After this is done we will use the related words and generate sentences with the hypernyms use in natural language. This will be done be essentially reverse hearst-hypernym pattern matching. Meaning we already have the words, we just need to generate the context around them. Hearst hypernymy patterns can be used to generate such context.

We then can train the model for both the hem/onc corpus - by filtering MeSH terms in UMLS for hematology oncology, as well as the full model for all relationships.

**The files you see in this folder are all tests that Saadh and I are using locally - or parts of these scripts on SaturnCloud within a jupyter notebook for the final - prod scripts that we will keep to build corpuses / update at will.**