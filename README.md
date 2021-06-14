# DoctorLingo Corpus

### This readme is under construction, in process of re-organizing, I suggest for more pointed docs - going into the directories themselves, which have their own readme files.

**Overview of project: Creating a pipeline that uses artificial intelligence (AI), specifically containing a model trained with machine learning and natural language processing, to store, process, and interpret medical words or even whole medical notes into a patient-readable interpretation. It was primarily developed in the programming language Python and with freely available data. Some licenses were required, i.e., for the United Medical Language System (UMLS) database from the NIH.**

*Jargon (ironically) in this README*
--"bootstrapping" = a type of way to prep a model for supervised machine learning
--"db" = database
--"Scraping" in NLP/big data jargon, means retrieving data from a source. 
--"Corpus" in NLP is a body of text. It can contain meta-data, or not, which we call a "bag of words."
-AI = artificial intelligence - I'm sure you are familiar with this term
-ML = Machine Learning - Probably still familiar, but if not - it is a form of AI that trains a computer to predict things
-NLP = natural language processing - Not as commonly used in common conversation - a specific subset of ML
So;
-NLP is a form of ML; ML is a form of AI. AI is the most general term

*Important concepts:*
--The immediately above phrase is actually an example of an informal logic representation of a linguistics concept that this project heavily relies upon, hypernymy.
--Both logic (computer logic/formal/symbolic logic) and areas of linguistics are very important to this project, but that is beyond the scope of a general discussion. Here are the core components needed to understand how the model we developed works.
--In brief, we had to think about how people explain things to one another.
--Simply defining a medical term by an official definition from whatever source is problematic because it often includes heavy jargon.
--In linguistics, two common themes are apparent when explaining a concept to someone - hypernymy and meronymy)
--Hypernymy is a linguistic concept that relates words in terms of specificity; orange is a type of color (color is the hypernym, less specific category to which orange, the hyponym, belongs; orange is also a fruit however, and our corpus is set up to handle multiple meanings, spellings, acronyms, etc, some medical slang is pending).
--Meronymy, which is a "part-whole" relationship, the atria are part of the heart. Here, the atria are the meronym (the part) and the heart is the holonym (the whole). This is the second most common relationship seen in wordnet and the second most important concept in linguistics when first explaining a new word to someone.

*Rationale:*
Mandatory open notes, whether some like it or not, seem to be the future for physicians/patients. Open notes are already rolled out in many EMRs. There is no real response to this, in terms of tools, for patients to understand what physicians are writing about them. Also, beneath that reasoning is the need to expand ML/NLP tools to both clinical researchers without coding experience and to computer science researchers without clinical experience. NLP opens a vast data source from patient notes for retrospective studies. So, in summary, we are building a corpus. 

For data scientists/programmers, it can be viewed as a fancy database for knowledge and all English relationships between these words and actual English words. For medicine, it's a very powerful thesaurus like UMLS but expanded and able to "learn" new words/concepts, both linguistic and scientific. For patients, it's a tool to understand medical text in plain English. That last sentence doesn't really do the justice for the upgrade that patient's will experience if they use this over say, a google search. So I will use some hyperbole to emphasize. 

*Hyperbolic example:* 
*Imagine you wake up in an unfamiliar place. You find a document with a specific set of instructions and realize it is written in another language. The only thing you can make out is that the length and quality of your life very likely depend on this. The exact length of time and quality of life are not specified, but you seem to think it's important because you can also make out some words that describe your organs getting injured or possibly failing. Not only are the stakes high knowing that but then you remember briefly being told that the instructions are written in short-hand and by an expert with at least over a decade of study and practice, in the one remarkably complex field that has the answer which your life depends on. You don't know which items in this document to use when. You are actually not even sure if this document is saying your life depends on doing something, keeping things the same, or changing something. You just know that your fate is somehow tied to this document.*

**The cherry on top is that the expert wrote it not with you or another non-expert in mind but as a quick and general reminder for themself, other experts in the field, or to bill companies that reimburse their services. In the field that the author studied, the wrong interpretation of his instructions, while seemingly dramatic, could kill the person.**


Now let's say you are the patient above, and you have to choose two resources to interpret that text. Your options are:
1. A natural-born, native tongue, local translator, who was trained specifically with the most advanced learning techniques and by incalculably many situations to perform their one job: understanding that expert and explain what he says in plain English. 
2. Or, alternatively, you have a hand-crafted tourist-guide translation pocketbook of word-to-word translations and a few phrases here and there. It also came with a downloadable app for quick searches.

*Which one do you pick?*

The way this project will contribute to data science/medicine is both by developing the application for patients and developing a much-needed friendly corpus and comprehensive medical corpus for future researchers that goes beyond the linguistic capabilities of UMLS/SNOMED/ICD classification systems. It uses a WordNet style hierarchy, meaning that the most common form relationships and the largest "tree" of terms is by way of hypernymy. 

It utilizes some state-of-the-art tech in NLP, which are not essential to understand, but if interested, specifically SpaCy, Prodigy and transformer models, seq2seq2 ML models, and abstractive text summarization, which is much harder to use than extractive, but if done right, more natural to the reader (see links below model development for more info on SpaCy and Prodigy, transformers are very complex and beyond scope of this).

*General description of the AI model:*
The artificial intelligence pipeline uses a type of machine learning called natural language processing. Essentially, I take examples of things I want to teach the computer. I then feed the computer this as "gold-standard" data. This has both positive and negative examples to learn from. 
Briefly, the statistical/mathematical way a computer learns with "machine learning" and "natural language processing" involves taking the data it is fed and passing it through an N-gram matrix and finding patterns. This creates "the model." The N-gram matrix can be thought of similar to an x, y axis plot, except it is "N" number of axises for any feature you want, instead of just two dimensional. Meaning the model can learn, at least in theory, infinite pattern associations for data fed to it, if a pattern for related concepts exists. 
While machine learning is quite complex from an algorithm development perspective, the best way to think of it in basic stats is infinity linear regressions to describe a relationship or find the best "fit" solution to a problem (any data that passes through the model). The machine predict outcomes from input by passing the problem through the model and seeing if the N-features are close enough to a threshold in the N-dimensions it considered significant, to be consider a positive; if not, its a negative.

*Model development (generally):* 
In this section, I describe just the development of the model portion of the pipeline. I do not include the whole pipeline in detail because it is quite involved. In short, I used python (a programming language) to scrape Wikipedia for all articles on all cancers listed per the NCI designation of cancer types. I then wrote python scripts to search the scraped text for all examples of hypernyms and meronyms with a linguistic pattern called Hearst Patterns (essentially phrases that we commonly find hypernyms in English [and actually any language given syntax/grammar correction] i.e. a pattern like, "common types of large domestic dogs include Pitbulls, retrievers and shepherds"). 

The amount of data required for Machine Learning is quite astounding. Just to bootstrap, not even fully train the model, I gathered a ~1 million words, ~50,000 sentences, about 5,000 unique examples of hypernyms/meronyms identified per a simple algorithmic pattern matcher that I wrote in SpaCy which does use some NLP, but just to tokenize and assign linguistic relationships to the tokens in the data. This algorithmic approach is only about 80% accurate, whereas the model hits >90% every time it runs - that's the power of transformer models). To get the model to 95-99% range it will require a massive amount more of data and with diminishing returns. However, I do have a massive amount of data, the corpus, which I will run against all of PUBMED since the beginning of its existence to find patterns for the model. 

Specifically to train the model, for both the new model and the first model I feed the hypernym/meronym patterns to two machine learning/natural language processing packages developed for python: SpaCy, and Prodigy.

SpaCy can be though of the master tool and is the actual package that includes ground-breaking, state-of-the-art AI/NLP algorithms to perform natural language processing on text in a very pythonic (concise and intuitive) way. SpaCy includes the ability to use recently developed breakthroughs in AI modeling like "transformers." 

Not only that, but the makers of SpaCy also developed Prodigy, a tool to annotate datasets for machine learning. For supervised machine learning (best for our purposes, especially given this may eventually have real impact on patients -- we want to know what the computer is learning from -- this will also help with anyone who believes our model fits the "AI black box" fear) specifically to reduce the time it takes to train/bootstrap a model. 

Prodigy is essentially a program that allows rapid manual notation of new gold-standard datasets. So for example if I scrape 1 million examples of hypernyms from PUBMED, to code a program to annotate each example as positive or negative for all possibilities, or to do it manually would take quite some time and effort. Prodigy creates a GUI that loads all of the scraped data with all linguistic concepts available that would create a relationship in English. You just then click on the words that are associated and name that link the relationship you want to train the model for. This is presented in a way that can be done very rapidly, I can annotate in a couple clicks hundreds to thousands of relationships in just a few minutes. You could have an annotated bootstrapping dataset in a few hours, or a full dataset for completely supervised learning in just a day. Normally in ML this takes months. I just want to emphasize the power of that for future projects. With this pipeline developed it can be applied to pretty much any NLP answerable question with results in like a week to two weeks tops. This took me a few months because I was teaching myself NLP from scratch.

https://spacy.io/usage
https://prodi.gy/

*Pipeline development for test corpus and NER model development specifically (some more details):*
--I "scraped" all unique words from my licensed copy of UMLS to obtain about 3,623,742 unique words 
*--It is important to note that I did not scrape concepts or entries, but literally any string of text/data from the UMLS database.*
--WE WILL NOT BE USING THIS IN PRODUCTION BECAUSE SCRAPING MANUALLY CREATES A LOT OF ROOM FOR ERRORS, for details on prod pipeline development see section on SQL (can ctrl+F to find)
--I re-ran those words with a python script against UMLS, SNOMEDCT db, and ICD10 db to extract official terms/concepts/entries from all those db's.
--To add flexibility to this corpus it will include all of wordnet, which is one of the most powerful and commonly used corpuses to date for all of NLP.
--So our corpus hosts all concepts and data from UMLS, SNOMED, ICD10, and wordnet, making it possibly the most comprehensive source of medical terms to date.
--I also trained it to identify hypernyms and meronyms. I did this by bootstrapping the model to get it to about 90% accuracy on most runs.
--I then format the raw final first version of the corpus data to a JSON format so it can be used with SpaCy's built-in NER model (very powerful and very scalable).
--This is the corpus framework - then we format the corpus for our DL website into another database.
--The modifiable SpaCy (dynamic) corpus and DL website (static/official) corpus will talk to one another. Crowdsourcing will still be implemented by users being allowed to "verify a definition." If a term or (word or short noun phrase) is searched and it has a result that is not in the official corpus, and a user who is has the privileges to verify it does it, it signals the dynamic corpus to flag it for updating the static corpus at a specific time interval yet to be determined.
--If the word does not exist in either the official as an official term or in the dynamic corpus at all, then it activates a python script that uses SpaCy, our trained custom model on scraped data to see if it can generate a suitable term to add to the dynamic corpus to await verification.
--There are many millions of more tokens for medical concepts/terms in our final corpus.
--For the SpaCy model currently, in a given text with context, the model recognizes all general linguistic concepts (parts of speech, synonyms/antonyms, syntax, grammar, etc in English)

*Usage for the public in production:* 
The model will be used by patients, as follows, in the pipeline for production. 
--If a patient enters a single word, it will pull the word from our corpus if we have it as a token in our corpus, it will return a definition of the word and using hypernyms and meronyms to "translates" the definition into "plain English." This involves complexity scoring of words passages that are returned in the definition, also beyond scope. If not it will scrape data for use context of said word, in English, to generate an entry to our corpus. 
--If a patient enters a body of text, it will parse the text and translate similarly to how it does for a single word definition above. Except it scores the complexity of the passage by each part by the complexity of the words in said part. It returns the complex words substituted for hypernyms/meronyms. If a patient wants the word to be more specific or less specific, or see if its a part of something else, a type of something else, or any English linguistic concept such as part of speech, function in a sentence (including all grammar and syntax concepts) it will return that in simpler terms as well. 
--For example, a sentence like "The patient should take amlodipine 5mg daily." It will score the sentence for complexity. recognize that the latter portion of the sentence is complex and it will interpret that. It will recognize that amlodipine is an entity type "medication" and then return a definition of that medication that is in plain English, such as "Amlodipine is a medication for high blood pressure." It includes a disclaimer that this is not a substitute for a physician's explanation of the written text of a medical plan for themself.

## Conceptual principles for project

**Overview:**
This document is for a conceptual understanding of corpus and medical lexicon auto-interpreter.

This project is a weird intersection of medicine, linguistics, computer science, and artificial intelligence, more specifically natural language
processing, a field and type of machine learning artificial intelligence. To clarify the intersection of these fields and why this project
is important I explain very briefly the overarching and finally uniting principles of these fields in the context of this project.

*Briefly (and very practically) let's define some things in simple terms (oh the irony!):*

-Artificial intelligence (AI) = teaching computers to learn things

-Machine Learning (ML) = a specific type of AI that teaches a computer to learn things by having it find patterns in examples
this can supervised (you tell the machine the output you'd expect for a given input and potentially bootstrap it with examples),
or unsupervised (you do not know what the output should look like and the computer just finds the patterns on its own).

-Natural language processing (NLP) = a specific type of ML/data science that looks to find patterns in literally the natural/day-to-day 
language used by humans.

-Neural models = types of AI models that are similar to how people think, I'll keep it simple, do some googling though. Interesting!

-Corpus = a body of text that you can feed to a natural language processing component

-Token = a word that is identified by a Natural Language Processing pipeline as a specific entity with specific properties

We will not review what medicine and computer science are because these are more commonly understood fields, at least superficially.


**A brief note on linguistics:**
*Let's pause for a second and recall some linguistic concepts we all already know:*

-Definition - the meaning of a word
-Part of speech (POS) - nouns, verbs, adjectives, adverbs, etc.
-Synonym - two different words with the same meaning
-Antonym - two different words with opposite meaning


*Now let's discuss some concepts that are probably less familiar:*

-Lemma = a lemma is a form of a word/token that is the most basic form of the word (similar to Lexemes)

Or more elegantly,

"The lemma is the base form under which the word is entered [in a dictionary] and assigned its place:
typically, the 'stem,' or simplest form (singular noun, present/infinitive verb, etc.). 

i.e. the Lemma of running is run; coded -> code; written -> write; etc.

-Hypernyms = are a relationship of specificity, a hypernym is a less specific form of a hyponym
i.e. a greyhound is a type of dog, a computer is a type of machine
greyhound = the hypernym (less specific) of the hyponym (more specific) dog

-Holonyms/Meronyms = a relationship of things that are part-whole relationships
i.e. a chair has legs; the holonym is the whole - the chair, the meronym is the part of the whole - the legs
(note holonyms are not the same thing as homonyms - as described below)



*It is important to note that this corpus was formatted with similar hierarchies as a corpus called wordnet, and many from the United
Medical Language Services (UMLS) of the National Library of Medicine (NLM) of the National Institute of health (NIH) -- wow... anyways.*

**To truly understand this corpus you must therefore understand the linguistic concepts used in both Wordnet and UMLS.**
The corpus and NLP pipeline developed from this project also use WordNet and UMLS as independently searchable corpi apart from the
Doctor Lingo Corpus.

Wordnet hierarchies

This is a huge corpus that is an organized corpus (not a "bag of words") by a hierarchy of concepts.

It is at its most basic unit -- organized into synsets meaning sets of all words that are synonyms.
Or another way, these synonyms, sharing the same definition, are a part of a unit, called synsets.
(clever name! -- synonym + set = synset)

These sets aka synsets are then related throughout the hierarchy of the corpus with other linguistic concepts.

An example adjective synset is:
good, right, ripe – (most suitable or right for a particular purpose; "a good time to plant tomatoes"; "the right time to act"; "the time is ripe for great sociological changes").


*Of note:*
Words/tokens can occur in different synsets if they have different meanings in particular context.
From 5th grade remember: Homonyms, that's what these are!


**Now onto the description of the WordNet hierarchy.**

The most commonly shared relationship in WordNet is hypernymy it makes up like 80+% of the net.

*Relationships in the overall hierarchy vary based on parts of speech, to clarify that, read below:*

For POS:
-If a word is a noun - Most frequently related by hypernymy (~80% of nouns) and meronymy (~20% of nouns). Wordnet distinguishes b/w common nouns and instance nouns (proper, i.e. Obama is an instance of a president), instance nodes are always terminal.

-Since nouns are much more common in languages than are verbs, WordNet terms are mostly related by hypernymy links in the overall hierarchy.

-If a word is a verb - most common relation is troponymy - hierarchy of types of events in terms of specificity, like hypernyms - to communicate can be to talk or to whisper. The specific manner expressed depends on the semantic field; volume (as in the example above)

-If a word is an adjective - the most common relation is antonomy - pairs of “direct” antonyms like wet-dry and young-old reflect the strong semantic contract of their members. Each of these polar adjectives in turn is linked to a number of “semantically similar” ones: dry is linked to parched, arid, dessicated and bone-dry and wet to soggy, waterlogged, etc. Semantically similar adjectives are “indirect antonyms” of the contral member of the opposite pole. Relational adjectives ("pertainyms") point to the nouns they are derived from (criminal-crime). 

-Adverb - there are only few adverbs in WordNet (hardly, mostly, really, etc.) as the majority of English adverbs are straightforwardly derived from adjectives via morphological affixation (surprisingly, strangely, etc.)


*Because hypernymy is so important in relating words we will briefly review it again with a bit more detail:*
-Hypernymy/hoponym/ = broader/narrower category and has a "IS A" relationship - mostly used for nouns.
Impoortany to note that hyponymy is transitive, but not hypernymy. This means that german shepherds and pitbulls share the hypernymy relationship of dog
However, hypernyms do not always share hyponyms (maybe not ever, honestly not sure about that -- ask a linguist - I'm a physician with too much time on my hands)

*Again review meronyms as it is the second most important relation in WordNet and the corpus we built:*
-Meronyms (part-whole relation, legs, chair; a chair has legs, not inherited upward through the hypernym tree, chairs have legs but not all furniture does)


**Thus, WordNet really consists of four sub-nets, one each for nouns, verbs, adjectives and adverbs, with few cross-POS pointers.**
Cross-POS relations include the “morphosemantic” links that hold among semantically similar words sharing a stem with the same meaning: observe (verb), observant (adjective) observation, observatory (nouns). In many of the noun-verb pairs the semantic role of the noun with respect to the verb has been specified: {sleeper, sleeping_car} is the LOCATION for {sleep} and {painter}is the AGENT of {paint}, while {painting, picture} is its RESULT.

*Cross-POS relations*
Cross-POS relations include the “morphosemantic” links that hold among semantically similar words sharing a stem with the same meaning: observe (verb), observant (adjective) observation, observatory (nouns). In many of the noun-verb pairs the semantic role of the noun with respect to the verb has been specified: {sleeper, sleeping_car} is the LOCATION for {sleep} and {painter}is the AGENT of {paint}, while {painting, picture} is its RESULT.

**To do's for linguistic concepts**
Hypernym/hyponym - remake for hem/onc and re-train for production
Holonym/Meronym - remake for hem/onc and re-train for production
Tropnonym - steal wordnets
See Alsos - steal UMLS / Wordnet
Synonym - built in to spacy
Antonym - built in to spacy
Pertainym - ???
Participle - built in to spacy


##Overview of Directory Hierarchy and Basic Dependencies: 

###Installing Conda

*(SpaCy and Prodigy setup are detailed in the next sections)*

-I highly recommend setting everything up in virtual/conda environments, because, you know... dependencies, ugh.
-I use Conda and within it, PIP for most packages. Miniconda or full anaconda work fine.
- https://anaconda.org/

###Installing UMLS
-UMLS does require a license, it takes about a day to get back, I would apply for this now (not a difficult process)
- https://uts.nlm.nih.gov/uts/signup-login
- https://www.nlm.nih.gov/research/umls/index.html

-Keep in mind, I am currently in the process as discussed of converting UMLS to a MySQL db with their native scripts. -This was because custom extraction of all data from UMLS has a lot of room for error.. -As discussed I will convert the MySQL database to a CUDA blazingSQL db and then finally that will be used to create the cudf/dask/pandas dataframe. -Below are official docs for the tools needed to do this and in general for the project:. 
-UMLS official ebook 
- https://www.ncbi.nlm.nih.gov/books/NBK9676/. 
-MySQL docs for UMLS 
- https://www.nlm.nih.gov/research/umls/implementation_resources/scripts/README_ORF_MySQL_Output_Stream.html
-Less important, but their GUI docs for MetamorphoSys: https://www.nlm.nih.gov/research/umls/implementation_resources/scripts/index.html
-BlazingSQL docs 
- https://blazingsql.com/. 
-(below this line, these links become more important and understandable for the next bullet points following these links)

###Installing PUBMED
*Holding on this for now until we get the new NER model up and running*

###Installing RAPIDS, Dask
**RAPIDS cudf and Dask are multithreading and multiprocessing libraries for dataframes**
*Cudf dataframe documentation*
- https://docs.rapids.ai/api/cudf/stable/10min.html
-Cudf cheatsheet 
- https://rapids.ai/assets/files/cheatsheet.pdf

*Official dask docs (similar to spark)*
- https://docs.dask.org/en/latest/
-Pandas dataframe docs (the OG, non-parallelized dataframes that dask/cudf model themselves after) 
- https://pandas.pydata.org/docs/

-I still think it is pertinent to go through the scripts specifically see "/karlscripts/Build_database/extract_CUIs.py". -This is because the final version of the corpus will be in the form of a cudf/dask/pandas dataframe for speed. -Dask, cudf, and pandas all have interoperability and their own particular usefulness for dataframe management. -I would recommend familiarizing yourself with pandas if not already, then read on RAPIDS'. udf, and dask (to further complicate, there is a dask-cudf. ataframe, you can find the docs on RAPIDS website as above)

### Directory. Organization:

**Directory: documentation**
Self explanatory and good starting point, you can also dive right into the scripts below as each folder has docs and documentation within most of the scripts
This directory also contains explanations of some of the general principles that make up the rationale for the project/approach, including linguistic features.

**Directory: "build_database"** 
This is the main directory that houses the scripts which build out the corpus. Currently within that you will see scripts that utilize dask and cudf(see below for download and official docs).

*Within Build_database:*
So this is most of the stuff used to build the corpus (some WordNet stuff excluded for now - not as important but I would google and read on the structure/schema/hierarchy of WordNet)
Also an interesting history lesson and why I decided I needed to read more on linguistics, which is actually quite important for NLP. The dudes who started the basis of WordNet were like lexicographers from the 1970s lol, not programmers, then some dudes at Princeton who could program finally realized their dreams for them -- also a great movie similar to this, called The Professor and the Madman. My roommate/bf4eva->. showed me this when I told him what I was doing blasting my keyboard at 3am. 
*He told me I am the madman and Josh is the professor, but I suspect we are all kind of the madman a little bit... anywho*

**Directory: /Build_database/DL_UMLS_modified**
This directory has all of the UMLS datafiles from my custom extraction scripts (not included - for a reason, the reason: we are not using this method - see above regarding SQL)
Again: UMLS does require a license, it takes about a day to get back, I would apply for this now (not a difficult process) if you are working on this part of the project

**Directory: Hypernyms**
Since currently, my focus is getting the friggin' corpus to prod, I am less worried about you reading this stuff right away, but a general review/skim would be a good idea. I am in the process of rebuilding the NER model and the final script that will call from the corpus to do any interpreting - but I need to figure out what that looks like in prod before I can write it. Once you are familiar with the material in this email/karlscript -- we will go over the game plan currently of getting it deployed to Amazon SageMaker. Additionally Cubby and I discussed potentially getting a test prod model onto his preferred platform with Heroku. I need to circle back with Cubby to discuss what I have been doing, but this email is a good start, Cubby if you read this far haha.. Cubby, once the MySQL stuff is done I will send a dataframe your way. Anywho:. This is the directory that houses the scripts/data for the first Hypernymy. ER model I built.. Briefly this uses SpaCy and Prodigy. - https://spacy.io/usage. - https://prodi.gy/demo. 
-Both SpaCy and Prodigy are from the company Explosion AI. -SpaCy is the main package and is free, it is a suite of NLP tools, and has many pre-trained models, built-in components and is expandable with other packages i.e. SciSpaCy from AllenAI. -Prodigy is a custom pre-processing and NLP model training library - it is a really cool concept and cuts down time for manually curating data for training significantly. -Prodigy is not free and not required to train a SpaCy model, I just like it, you can still automate gold standard data or do it manually through the command line or programming language of choice. -If you decide you want to try this, I will give you my login, and we can look into purchasing a company license, or getting you an individual license.. -Additionally within this script is a test script for the actual basics part of the autointerpreter. we will review full interpreter after you get through all of this, lol sorry =P). -In short the autointerpreter works with word complexity scoring and substituting hypernyms/meronyms for complex words. -Within the script "test_readability.py" there are different modes of scoring from mathematical models, I suggest googling the names of these models to familiarize yourself. -Again happy to discuss any of this over the phone if you are working on this part of the project


**Directories: SciSpacy_Setup and Spacy_Setup**
Finally the directory SciSpacy_Setup just houses tar files for all the SciSpaCy models, you do not really need to use this, I am just collecting packages because I'm paranoid that in the event they get taken down for a new model, there may be dependency issues in the future, so I am saving local copies of all repositories/packages etc.


## Installation of SpaCy environment for experienced devs

This is the README for experienced devs, preferably, with python experience
if you are new to coding please see the README appropriately labeled
"README_for_noobs." Experienced devs, this is just a suggestion on how to
proceed with install, feel free to hack away as well.

Let's begin.

I hope you installed the main "karlscripts" folder to your home directory.
You don't have to install it in the home directory, but if it doesn't work,
then don't blame me. =P

Introduction:

This pipleline uses SpaCy v3.0.4 SciSpaCy v0.4.0 these are the newest versions
at the time of writing.

As the above were built on mostly python 3.7, that's the python version we use.

For these reasons, you should install this pipeline in a virtual environment.

Use a completely clean and new env. 

If you already installed as above in the first section, ignore this section.
I use anaconda/conda. See official docs for install on your system (briefly below)


*Install miniconda*

Briefly:
install miniconda for your specific PC
https://docs.conda.io/en/latest/miniconda.html
Read the docs and if you run into trouble literally Google:
"How to install miniconda on X" where X is your Operating System/specs.

Set up conda environment - *you can also use command line or the anaconda GUI here*
In your home dir create a text file with the following lines:
name: doctorlingo_corpus (or whatever you want)
dependencies:
  - python=3.7
  - pip


Save that as "environment.yml"

Then in your terminal - enter:
conda env create -f environment.yml

This creates your miniconda virtual environment called "doctorlingo_corpus"  
(appropriately named) I would use this virutal environment for scispacy alone, 
if you need to try to use it with other packagesthen dependencies may vary for
the several packages that SciSpaCy/SpaCy depend on, this may break this 
environment setup. This environment will have python 3.7 and pip (an installer)
set up at ready to go.

Then in your terminal - enter:
conda activate doctorlingo_corpus
This activates the virtual env - you must do this every time you close
and re-open your terminal, unless you have a terminal that saves your
last work environment (beyond scope of this).

SpaCy install options:

Now it is time to install SpaCy, I built from source.

Try to do the source install if you are in a conda env, you should be largely 
protected from destroying your machine. If that doesn't work, then do the pip
install. Both are options are below.

To Note: in the source install I also use multithreading 
If you don't want to use multithread install or cannot, then switch that particular command


To Note: These docs were created when SpaCy 3.0.5 and 3.0.6 were the newest versions.
This install guide depends on "pip install." I included local copies of all the necessary
files in /karlscripts/SpaCy_Setup and /karlscripts/SciSpaCy_Setup.

pip install scispacy

becomes:

pip install '/karlscripts/scispacy-main

**There are many options for SpaCy install**

|---------------------COMMAND---------------------------|--------COMMENTS ABOUT COMMAND - DO NOT INCLUDE COMMENTS IN TERMINAL-------|
|=======================================================|===========================================================================|
|=======================================================|===========================================================================|
|Option 1a: For building from source, on your terminal, one at a time, copy and paste the following commands:|
|=======================================================|===========================================================================|
|cd ~|cd to home directory (you don't have to install here, but if it breaks don't blame me)                                        |
|python -m pip install -U pip setuptools wheel|install/update build tools -  flibrary to facilitate packaging Python projects       |
|git clone https://github.com/explosion/spaCy      |clone spaCy from GitHub                                                         |
|cd spaCy                                          |navigate into dir to where you installed SpaCy (don't worry conda handles paths)|
|pip install -r requirements.txt                   |install required dependencies for SpaCy                                         |
|python setup.py build_ext --inplace -j N          |Build in parallel with N CPUs for speed compilation and install in editable mode|
|                                                  |see alternative 1 in Option 1b below                                            |
|python setup.py develop                           |the "develop" command is only used if compiling from source                     |
|                                                  |see alternative 1 in Option 1b below                                            |
|pip install -U spacy[cuda112,transformers,lookups]|Finally pip install the NVIDIA cuda library

**For the above on CUDA**
*This must be specific to your videocard, where: cudaxyz; xyz are integers per your cuda version (can see this w/ nvcc --version) mine is 11.2, so cuda112*
If you do not have an NVIDIA GPU do not worry about this and you can remove the "cudaxyz" from the
command, however, still install the transformers and lookups libraries, this pipeline was developed
with a GPU, but a lot of it is written with threading in mind for CPUs, so you shouldn't suffer that much.
if not using GPU - i.e. $pip install -U pip install '.[cuda112,transformers,lookups,ja]' #don't include $ sign in terminal


*THE BELOW PACKAGES OF PRETRAINED MODELS ARE FOR DIFFERENT LANGUAGES THESE ARE OPTIONAL WITH THE EXCEPTION OF ENGLISH*
python -m spacy download zh_core_web_trf
python -m spacy download da_core_news_lg
python -m spacy download nl_core_news_lg
python -m spacy download en_core_web_trf
python -m spacy download fr_dep_news_trf
python -m spacy download de_dep_news_trf
python -m spacy download el_core_news_lg
python -m spacy download it_core_news_lg
python -m spacy download ja_core_news_lg
python -m spacy download lt_core_news_lg
python -m spacy download xx_sent_ud_sm
python -m spacy download nb_core_news_lg
python -m spacy download pl_core_news_lg
python -m spacy download pt_core_news_lg
python -m spacy download ro_core_news_lg
python -m spacy download ru_core_news_lg
python -m spacy download es_dep_news_trf


Option 1b: For building from source, but without multithreading compiler (slower;easier) 
YOU STILL NEED TO PERFORM COMMANDS 1-4 above from Option 1a -- then replace last two commands with the following below:

|---------------------COMMAND---------------------------|--------COMMENTS ABOUT COMMAND - DO NOT INCLUDE COMMENTS IN TERMINAL-------|
|=======================================================|===========================================================================|
|=======================================================|===========================================================================|
|pip install --no-build-isolation --editable|compile and install spaCy (YOU DO NEED TO INCLUDE THAT PERIOD AT END OF COMMAND)|
|Option 3: Do not compile from source, use a pre-compiled wheel from the Explosion developers:
|=======================================================|===========================================================================|
|COMMAND|COMMENTS ABOUT COMMAND - DO NOT INCLUDE COMMENTS IN TERMINAL|
|cd ~/|cd to home directory|(you don't have to install here, but if it breaks don't blame me)|
|pip install -U pip setuptools wheel|python -m pip install -U pip setuptools wheel; install/update build tools, flibrary facilitate pypkgs|
|pip install -U spacy[cuda102,transformers,lookups]|Finally pip install the NVIDIA cuda library (this must be specific to your videocard, where: cudaxyz|

**For the above on CUDA**
*This must be specific to your videocard, where: cudaxyz; xyz are integers per your cuda version (can see this w/ nvcc --version) mine is 11.2, so cuda112*
If you do not have an NVIDIA GPU do not worry about this and you can remove the "cudaxyz" from the
command, however, still install the transformers and lookups libraries, this pipeline was developed
with a GPU, but a lot of it is written with threading in mind for CPUs, so you shouldn't suffer that much.
if not using GPU - i.e. $pip install -U pip install '.[cuda112,transformers,lookups,ja]' #don't include $ sign in terminal

This is the main pre-trained model that I use to test small programs:
python -m spacy download en_core_web_sm


To obtain scispacy models, use pip install on the terminal to install the following packages
that contain SciSpaCy itself and the models for SpaCy/SciSpaCy:

pip install scispacy
pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.4.0/en_core_sci_sm-0.4.0.tar.gz
pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.4.0/en_core_sci_md-0.4.0.tar.gz
pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.4.0/en_core_sci_lg-0.4.0.tar.gz
pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.4.0/en_ner_bc5cdr_md-0.4.0.tar.gz
pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.4.0/en_ner_jnlpba_md-0.4.0.tar.gz
pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.4.0/en_core_sci_scibert-0.4.0.tar.gz
pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.4.0/en_ner_bionlp13cg_md-0.4.0.tar.gz

As noted previously

The above are html links so if they become deprecated, I will include
the tar files in the base folder "karlscripts" in the "SciSpacy_Setup"
folder. You can pip install as above, but instead of the link give the
path to the file w/ the filename at end of path. For me it should look like:
"pip install /home/karl/karlscripts/SciSpaCy_Setup/en_ner_jnlpba_md-0.4.0.tar.gz"

After doing this, on the terminal, check the command: spacy info
you should see output like this:

spaCy version    3.0.5                         
Location         YOUR_OWN_HOME_DIRECTORY/anaconda3/envs/scispacy/lib/python3.6/site-packages/spacy
Platform         YOUR_OWN_PLATFORM_AKA_OS mine is: "Linux-5.8.0-50-generic-x86_64-with-debian-bullseye-sid"
Python version   3.6.13                        
Pipelines        en_ner_bc5cdr_md (0.4.0), en_core_sci_md (0.4.0), en_core_sci_sm (0.4.0), en_ner_bionlp13cg_md (0.4.0), en_core_sci_lg (0.4.0), en_ner_jnlpba_md (0.4.0), en_core_sci_scibert (0.4.0)


This environment using python 3.7 it may be compatible with 3.8+
but given the difficulty with env as a whole I didn't mess with it

If you have followed these instructions it should work provided
your OS is compatible (see official docs for this).




## Installation of SpaCy environment for newbie devs

This is the README for newbie developers, so if you are an experience dev,
please see the README appropriately labeled.

Let's begin.

I hope you installed the main folder to your home directory, if it is in your
downloads, go ahead and move it to your home directory. If you don't know what
your home directory is, now is a good time to google search: 
"How do I find my home directory in X" where X is terminal, command line, etc.
depending on your machine (PC [Windows or Linux], or Mac).

You don't have to install it in the home directory, but if it doesn't work,
then don't blame me. =P

In general, if you are new to programming/coding/scripting/whatever the kids
are calling it nowadays, then google/StackOverflow are your friends. That is
like 99% of how I learned, that and one course on algorithms during time in my
MS in computational biology. (Real programmers will probably notice this, sorry!)

So, newbies, it is possible! Learning to code is very important, for the future
of medicine. So especially for the physician/scientists who are just starting,
or students, who want to work in medical data science in the future, keep trying!

Also, one last note before posting for help online, for any error, read your code
check for any spelling / syntax errors. I learned it is usually my fault, but not
always. For python with packages, I always look at the error output in terminal
then look at my code, if I can't find anything, then I google around, starting
with copy and pasting the error message to google and looking for threads on
dependency issues first. If it isn't one of those two things, then its going
to take a while to troubleshoot. But don't give up!

Introduction:

This pipleline uses SpaCy v3.0.6 SciSpaCy v0.4.0 this is the newest SciSpaCy. 
Dependencies are in general, difficult to deal with, but for SciSpaCy especially,
they are, for lack of better terms, all jacked up. That isn't to fault those devs,
as their own work has many of their own depencies they must rely on, we bend to
the first devs on scence, not the other way around.

As these were built on mostly python 3.7, that's the python version we use.

For these reasons, you should install this pipeline in a virtual environment.
Use a completely clean and new env. 


I use anaconda/conda. See official docs for
install on your system.

*Install miniconda*
Briefly:

install miniconda for your specific PC
https://docs.conda.io/en/latest/miniconda.html
Read the docs and if you run into trouble literally Google:
"How to install miniconda on X" where X is your Operating System/specs.

Set up conda environment - you can also use command line or the anaconda GUI here

In your home director (folder) open a text file with the following lines: 
(literally copy and paste the next four lines of this doc to the file):
name: doctorlingo_corpus (or whatever you want)
dependencies:
  - python=3.7
  - pip


Save that as "environment.yml"

Then in your terminal - enter:
conda env create -f environment.yml

This creates your miniconda virtual environment called "doctorlingo_corpus"  
(appropriately named) I would use this virutal environment for scispacy alone, 
if you need to try to use it with other packagesthen dependencies may vary for
the several packages that SciSpaCy/SpaCy depend on, this may break this 
environment setup. This environment will have python 3.7 and pip (an installer)
set up at ready to go.

Then in your terminal - enter:
conda activate doctorlingo_corpus
This activates the virtual env - you must do this every time you close
and re-open your terminal, unless you have a terminal that saves your
last work environment (beyond scope of this).

SpaCy install options:

Now it is time to install SpaCy, I built from source, which can be complicated
if you are a Noob, like myself, you can alternatively pip install these packages
but it will not be optimized for run time performance, aka SpaCy can still work 
with pip install, it just may run a bit slower. 

Try to do the source install if you are in a conda env, you should be largely 
protected from destroying your machine. If that doesn't work, then do the pip
install. Both are options are below.

To Note: in the source install I also use multithreading (if you do not know what
that is, google it, but its again not necessary to run, just may compile more
slowly). If you don't want to use multithread install or cannot, then switch
the relevant command below

To Note: DO NOT INCLUDE THE STAR '*' or '#' IN YOUR TERMINAL COMMANDS
'*' is a wildcard variable and '#' is a many variables to the shell/terminal/BASH.

*To Note: These docs were created when SpaCy 3.0.5 and 3.0.6 were the newest versions.*
This install guide depends on "pip install" which will by default if installing a 
package by name i.e. "pip install spacy" will just search an online repository for
the files to install. In time, these name searches will point to newer versions
and if we haven't updated the pipeline these new versions may break the pipeline
for this reason see the folders "scispacy_setup" and "spacy_setup." They contain
local (downloaded) copies of all the necessary files and in the install guide you
can replace the "name" with the file. For example:

pip install scispacy

becomes:

pip install /karlscripts/scispacy-main

note the "/karlscripts" portion of the above is the path to my folder on my own
machine, this may be differentfor your, so you must know where you installed the main
pipeline folder as noted in the Welcome Statement at the beginning of this document

Option 1a: For building from source, on your terminal, one at a time, copy and paste the following commands:

|---------------------COMMAND---------------------------|--------COMMENTS ABOUT COMMAND - DO NOT INCLUDE COMMENTS IN TERMINAL-------|
|=======================================================|===========================================================================|
|=======================================================|===========================================================================|
|Option 1a: For building from source, on your terminal, one at a time, copy and paste the following commands:                       |
|=======================================================|===========================================================================|
|cd ~|cd to home directory (you don't have to install here, but if it breaks don't blame me)                                        |
|python -m pip install -U pip setuptools wheel|install/update build tools -  flibrary to facilitate packaging Python projects       |
|git clone https://github.com/explosion/spaCy      |clone spaCy from GitHub                                                         |
|cd spaCy                                          |navigate into dir to where you installed SpaCy (don't worry conda handles paths)|
|pip install -r requirements.txt                   |install required dependencies for SpaCy                                         |
|python setup.py build_ext --inplace -j N          |Build in parallel with N CPUs for speed compilation and install in editable mode|
|                                                  |see alternative 1 in Option 1b below                                            |
|python setup.py develop                           |the "develop" command is only used if compiling from source                     |
|                                                  |see alternative 1 in Option 1b below                                            |
|pip install -U spacy[cuda112,transformers,lookups]|Finally pip install the NVIDIA cuda library                                     |

**For the above on CUDA**
*This must be specific to your videocard, where: cudaxyz; xyz are integers per your cuda version (can see this w/ nvcc --version) mine is 11.2, so cuda112*
If you do not have an NVIDIA GPU do not worry about this and you can remove the "cudaxyz" from the
command, however, still install the transformers and lookups libraries, this pipeline was developed
with a GPU, but a lot of it is written with threading in mind for CPUs, so you shouldn't suffer that much.
if not using GPU - i.e. $pip install -U pip install '.[cuda112,transformers,lookups,ja]' #don't include $ sign in terminal


														
THE BELOW PACKAGES OF PRETRAINED MODELS ARE FOR DIFFERENT LANGUAGES THESE ARE OPTIONAL WITH THE EXCEPTION OF ENGLISH
python -m spacy download zh_core_web_trf
python -m spacy download da_core_news_lg
python -m spacy download nl_core_news_lg
python -m spacy download en_core_web_trf
python -m spacy download fr_dep_news_trf
python -m spacy download de_dep_news_trf
python -m spacy download el_core_news_lg
python -m spacy download it_core_news_lg
python -m spacy download ja_core_news_lg
python -m spacy download lt_core_news_lg
python -m spacy download xx_sent_ud_sm
python -m spacy download nb_core_news_lg
python -m spacy download pl_core_news_lg
python -m spacy download pt_core_news_lg
python -m spacy download ro_core_news_lg
python -m spacy download ru_core_news_lg
python -m spacy download es_dep_news_trf

Option 1b: For building from source, but without multithreading compiler (slower;easier) 
YOU STILL NEED TO PERFORM COMMANDS 1-4 above from Option 1a -- then replace last two commands with the following below:

|---------------------COMMAND---------------------------|--------COMMENTS ABOUT COMMAND - DO NOT INCLUDE COMMENTS IN TERMINAL-------|
|=======================================================|===========================================================================|
|=======================================================|===========================================================================|
|pip install --no-build-isolation --editable|compile and install spaCy (YOU DO NEED TO INCLUDE THAT PERIOD AT END OF COMMAND)|
|Option 3: Do not compile from source, use a pre-compiled wheel from the Explosion developers:
|=======================================================|===========================================================================|
|COMMAND|COMMENTS ABOUT COMMAND - DO NOT INCLUDE COMMENTS IN TERMINAL|
|cd ~/|cd to home directory|(you don't have to install here, but if it breaks don't blame me)|
|pip install -U pip setuptools wheel|python -m pip install -U pip setuptools wheel; install/update build tools, flibrary facilitate pypkgs|
|pip install -U spacy[cuda102,transformers,lookups]|Finally pip install the NVIDIA cuda library (this must be specific to your videocard, where: cudaxyz|

**For the above on CUDA**
*This must be specific to your videocard, where: cudaxyz; xyz are integers per your cuda version (can see this w/ nvcc --version) mine is 11.2, so cuda112*
If you do not have an NVIDIA GPU do not worry about this and you can remove the "cudaxyz" from the
command, however, still install the transformers and lookups libraries, this pipeline was developed
with a GPU, but a lot of it is written with threading in mind for CPUs, so you shouldn't suffer that much.
if not using GPU - i.e. $pip install -U pip install '.[cuda112,transformers,lookups,ja]' don't include $ sign in terminal

This is the main pre-trained model that I use to test small programs:
python -m spacy download en_core_web_sm


To obtain scispacy models, use pip install on the terminal to install the following packages
that contain SciSpaCy itself and the models for SpaCy/SciSpaCy:

pip install scispacy
pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.4.0/en_core_sci_sm-0.4.0.tar.gz
pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.4.0/en_core_sci_md-0.4.0.tar.gz
pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.4.0/en_core_sci_lg-0.4.0.tar.gz
pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.4.0/en_ner_bc5cdr_md-0.4.0.tar.gz
pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.4.0/en_ner_jnlpba_md-0.4.0.tar.gz
pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.4.0/en_core_sci_scibert-0.4.0.tar.gz
pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.4.0/en_ner_bionlp13cg_md-0.4.0.tar.gz


As noted previously

The above are html links so if they become deprecated, I will include
the tar files in the base folder "karlscripts" in the "SciSpacy_Setup"
folder. You can pip install as above, but instead of the link give the
path to the file w/ the filename at end of path. For me it should look like:
"pip install /home/karl/karlscripts/SciSpaCy_Setup/en_ner_jnlpba_md-0.4.0.tar.gz"

After doing this, on the terminal, check the command: spacy info
you should see output like this:

spaCy version    3.0.6                         
Location         YOUR_OWN_HOME_DIRECTORY/anaconda3/envs/scispacy/lib/python3.6/site-packages/spacy
Platform         YOUR_OWN_PLATFORM_AKA_OS mine is: "Linux-5.8.0-50-generic-x86_64-with-debian-bullseye-sid"
Python version   3.6.13                        
Pipelines        en_ner_bc5cdr_md (0.4.0), en_core_sci_md (0.4.0), en_core_sci_sm (0.4.0), en_ner_bionlp13cg_md (0.4.0), en_core_sci_lg (0.4.0), en_ner_jnlpba_md (0.4.0), en_core_sci_scibert (0.4.0)


This environment using python 3.7 it may be compatible with 3.8+
but given the difficulty with env as a whole I didn't mess with it

If you have followed these instructions it should work provided
your OS is compatible (see official docs for this).


###Format for a tokens with all linguistic relationships within our corpus:

-Key:
-PWN = PWN properties
-GWN = GWN properties
-UMLS = UMLS properties

-The corpus' ideal final form will be a dataframe (a pandas styled, but dask/cudf object for multi-threading/multi-processing)
-The corpus will be housed apart from the DoctorLingo website on AmazonSageMaker
-If a searched term, or terms in a note are not available in the DL website postgres db, it will send a call to the corpus to search
-If the corpus has the term/concepts it will return the data for such but in a cleaner way than below
-If the corpus does not have the terms/concepts it will run a script to try and scrape data from UMLS, PUBMED, the interwebz etc to generate an entry
-This entry will be stored in the "for review" dynamic version of the corpus as a separate dataframe
-Approved users/admin on the website (this functionality to be added) can approve a term from the corpus the DL postgres db, and from the dynamic corpus to the main static corpus
-Each row will be a unique entry w/ associated unique ID with columns that organize all of the words/relations for that concept/token.
-Entries will have a preferred term, which can be a word, noun phrases, entities (i.e. Hulk Hogan, Princeton, Clifford the Big Red Dog), etc. 
-Basically any conceptual thing that we use in natural medical language - eventually maybe in other fields / all of English / the world / the friggin' universe?

--In order, these properties were properties used in PWN, UMLS, GWN as these are in decreasing order of necessity for syntactic and semantic relations for this corpus to work well.
--Many of the categories from GWN may not be filled into because low yield overall for meaning.
--The highest yield properties are from TKN_ID to TKN_UMLS_WRD:


--If TKN is preceded by something, it means it is a relation derived from that specific abbreviations source (see below for abbrv details)
--If TKN is not preceded by something, it means it is a relation that is used amongst many NLP corpora / databases
--If a relation for a word existed in its original source, it should exist here, meaning if you don't see for example a gender property associated w/ UMLS, but you know that UMLS has a gender property, its because that was also a shared wordnet property, since it is unique to neither, we consider it a general property so it will not be preceded by a source.
--If two databases had repeat properties, they were not repeated and concantinated

--Wordnet relation info - for info on semantic/syntantic properties from wordnets see -- GWA schemas page (https://globalwordnet.github.io/schemas/)
--UMLS relation info - for info on TKN_UMLS semantic/syntantic properties from metathesaurus see -- TKN_UMLS Reference Manual (https://www.ncbi.nlm.nih.gov/books/NBK9676/)
--If the relation abbreviation is three capital letters this signifies it is from PWN / TKN_UMLS - the most fundamentally important concepts for our corpus (i.e. hypernyms and meronyms, being the top two most important). Some exceptions are if that category is included in another source, but a subcategory of that category is not and therefore would lose data from said source an example of this is the UMLS_TKN_SCA - or the syntactic category from UMLS. The SCA from UMLS includes parts of speech, which is in many databases, but it also have "complementizers" which are specific relations, but miscellaneous enough to keep this category despite POS redundancy.

-----------------------FILE WOULD START HERE AND BE IN PYTHON DICT FORMAT (SEE EXAMPLE)--------------------------------------
TKN_ID: Unique integer ID of this token (also the file name)
TKN: The lemma token string (must be lemmatized, nominalized, stemmed, etc. appropriately, essentially, the basis of your token)
TKN_POS: as per Universal POS tags for English (https://universaldependencies.org/docs/u/pos/)
TKN_FET: as per Universal Feature tags (not covered in POS) for Enlish (https://universaldependencies.org/docs/u/feat/index.html)
TKN_FOR: Forms of token: string of form:formform definitition a/w this token. For example if a verb the lemma is infinitive, form is tense
TKN_SEN: Use the token in the specified form returned in a sentence, use a sentence that can accept all forms as string variable
TKN_GEN: TKN gender
TKN_HPE: TKN hypernym -  tkn A in relation between two concepts where tkn B is a type of tkn A.
TKN_HPO: TKN hyponym - tkn B in relation between two concepts where tkn B is a type of tkn B.
TKN_HOL: TKN holonyms - tkn A in relation between two concepts where tkn B is a member/ element of tkn A.
TKN_MER: TKN meronyms - tkn B in relation between two concepts where tkn B is a member/ element of tkn A.
TKN_ENL: TKN entails - A verb X entails Y if X cannot be done unles Y is, or has been done.
TKN_CUZ: A relation between two concepts where B (related TKN:TKN_ID) comes into existence as a result of (token) A.
TKM_SIM: TKN similar - closely related in meaning
TKN_SEE: TKN see also - 
TKN_ATB: A relation between nominal and adjectival concepts where the concept A is an attribute of concept B.
TKN_VBG: TKN verb group - Verb senses that similar in meaning and have been manually grouped together.
TKN_DMT: TKN domain topic - tkn B in a relation between two tkns where B is a a scientific domain (e.g. computing, sport, biology, etc.) of concept A.
TKN_HDT: TKN has domain topic - tkn A in a relation between two concepts where B is a a scientific domain (e.g. computing, sport, biology, etc.) of concept A.
TKN_DMR: TKN domain region - tkn B in a relation between two concepts where B is a geographical / cultural domain of concept A.
TKN_HDR: TKN has domain region: tkn A in relation between two concepts where B is a geographical / cultural domain of concept A.
TKN_EXF: TKN exemplifies - Indicates the usage of this word
TKN_IEX: TKN is exemplified by - Indicates a word involved in the usage described by this word
TKN_agent: A relation between two concepts where concept A is typically the agent of the action expressed by concept B.
TKN_UMLS_EUI: Unique Identifier Number for Entries
TKN_UMLS_CUI: Unique Identifier Number for Concepts
TKN_UMLS_BAS: (saved as the TKN, as its already a lemma)
TKN_UMLS_ABR: Abbreviation of relation
TKN_UMLS_STR: Boolean expression string values
TKN_UMLS_SCA: Syntactic category (noun, adj, adv, pronoun, verbs, determiners, preposition, conjunction, auxil, modals, complementizers)
TKN_UMLS_AGR: Agreement/Inflection Code
TKN_UMLS_CIT: Citation Form
TKN_UMLS_COM: Complements
TKN_UMLS_PSN: Position for adjectives (1st, 2nd, 3rd, complement, pre-, post-)
TKN_UMLS_MOD: Modification Type for Adverbs (intensifier, particle, sentence modifier, verb modifier)
TKN_UMLS_FEA: Features
TKN_UMLS_NUM: 1st, 2nd, or 3rd person pronoun
TKN_UMLS_GND: Gender
TKN_UMLS_CAS: Case
TKN_UMLS_POS: Possession
TKN_UMLS_QNT: Quantification
TKN_UMLS_SPV: Spelling variant
TKN_UMLS_GEN: Generic term
TKN_UMLS_TYP: Inflection type
TKN_UMLS_WRD: Word
TKN_antonym: An opposite and inherently incompatible word
TKN_be_in_state: A relation between two concepts where concept A is qualified by concept B.
TKN_classified_by: A relation between concept B and a classifier concept A.
TKN_classifies: A relation between a classifier concept A and concept B.
TKN_co_agent_instrument: A relation between two concepts where concept B is the instrument used by concept A in a certain action.
TKN_co_agent_patient: A relation between two concepts where concept B is the patient undergoing an action carried out by concept A.
TKN_co_agent_result: A relation between two concepts where concept B is the result of an action carried out by concept A.
TKN_co_instrument_agent: A relation between two concepts where concept A is the instrument used by concept B for a certain action.
TKN_co_instrument_patient: A relation between two concepts where concept B undergoes an action for which the instrument expressed by concept A is used.
TKN_co_instrument_result: A relation between two concepts where concept B is the result of an action carried out by the instrument expressed by concept A.
TKN_co_patient_agent: A relation between two concepts where concept B undergoes an action carried out by concept A.
TKN_co_patient_instrument: A relation between two concepts where concept A undergoes an action for which the instrument expressed by concept A is used.
TKN_co_result_agent: A relation between two concepts where concept A is the result of an action carried out by concept B.
TKN_co_result_instrument: A relation between two concepts where concept A is the result of an action for which the instrument expressed by concept B is used.
TKN_co_role: A relation between two concepts where one concept undergoes an action in which the other concept is involved (bidirectional).
TKN_direction: A relation between two concepts where concept A is typically the direction or location of the action or event expressed by concept B.
TKN_eq_synonym: A relation between two concepts where A and B are equivalent concepts but their nature requires that they remain separate (e.g. Exemplifies)
TKN_holo_location: A relation between two concepts where concept B is a place located in concept A.
TKN_holo_portion: A relation between two concepts where concept B is an amount/piece/portion of concept A.
TKN_holonym: A relation between two concepts where concept A makes up a part of concept B.
TKN_in_manner: A relation between two concepts where concept B qualifies the manner in which an action or event expressed by concept A takes place.
TKN_instrument: A relation between two concepts where concept A is the instrument necessary for the action or event expressed by concept B.
TKN_involved_agent: A relation between two concepts where concept B is typically the agent of the action expressed by concept A.
TKN_involved_direction: A relation between two concepts where concept B is typically the direction or location of the action or event expressed by concept A.
TKN_involved_instrument: A relation between two concepts where concept B is typically the instrument necessary for the action or event expressed by concept A.
TKN_involved_location: A relation between two concepts where concept B is typically the location where the action or event expressed by concept A takes place.
TKN_involved_patient: A relation between two concepts where concept B is typically the patient un-dergoing an action or event expressed by concept A.
TKN_involved_result: A relation between two concepts where concept B comes into existence as a result of concept A.
TKN_involved_source_direction: A relation between two concepts where concept B is the place from where the action or event expressed by concept A begins/starts/happens.
TKN_involved_target_direction: A relation between two concepts where concept B is the place where the action or event expressed by concept A leads to.
TKN_involved: A relation between two concepts where concept B is typically involved in the action or event expressed by concept A.
TKN_is_caused_by: A relation between two concepts where concept A comes into existence as a result of concept B.
TKN_is_entailed_by: Opposite of entails
TKN_is_subevent_of: A relation between two concepts where concept A takes place during or as part of concept B, and whenever concept A takes place, concept B takes place.
TKN_location: A relation between two concepts where concept A is the location where the action or event expressed by concept B takes place.
TKN_manner_of: A relation between two concepts where concept A qualifies the manner in which an action or event expressed by concept B takes place.
TKN_mero_location: A relation between two concepts where concept A is a place located in concept B.
TKN_mero_portion: A relation between two concepts where concept A is an amount/piece/portion of concept B.
TKN_meronym: A relation between two concepts where concept B makes up a part of concept A.
TKN_other: Any relation not otherwise specified, please use dc:type attribute to give the name of exact relation.
TKN_patient: A relation between two concepts where concept A is the patient undergoing an action or event expressed by concept B.
TKN_pertainym: usually an adjective, which can be defined as "of or pertaining to" another word.
TKN_restricted_by: A relation between nominal (pronominal) concept B and an adjectival concept A (quantifier/determiner).
TKN_restricts: A relation between an adjectival concept A (quantifier/determiner) and a nominal (pronominal) concept B.
TKN_result: A relation between two concepts where concept A comes into existence as a result of concept B.
TKN_role: A relation between two concepts where concept A is typically involved in the action or event expressed by concept B.
TKN_source_direction: A relation between two concepts where concept A is the place from where the action or event expressed by concept B begins/starts/happens.
TKN_state_of: A relation between two concepts where concept B is qualified by concept A.
TKN_subevent: A relation between two concepts where concept B takes place during or as part of concept A, and whenever concept B takes place, concept A takes place.
TKN_target_direction: A relation between two concepts where concept A is the place where the action or event expressed by concept B leads to.
------------------------------------------------------------------------------------------------------------------------------
End file here - that is all the data possible so far for an entry into the corpus. Below are relations from each of their corresponding sources with a description
------------------------------------------------------------------------------------------------------------------------------
PWN_Hypernym: A relation between two concepts where concept A is a type of concept B.
PWN_Hyponym: A relation between two concepts where concept B is a type of concept A.
PWN_instance_hyponym: A relation between two concepts where concept A is a type of concept B, and where B is a terminal node in the hierchy.
PWN_instance_hypernym: A relation between two concepts where concept B is a type of concept A, and where B is a terminal node in the hierchy.
PWN_mero_member: A relation between two concepts where concept B is a member/ element of concept A.
PWN_holo_member: A relation between two concepts where concept A is a member/ element of concept B.
PWN_mero_part: A relation between two concepts where concept B is a component of concept A.
PWN_holo_part: A relation between two concepts where concept A is a component of concept B.
PWN_mero_substance: A relation between two concepts where concept A is made of concept B.
PWN_holo_substance: A relation between two concepts where concept B is made of concept A.
PWN_entails: A verb X entails Y if X cannot be done unles Y is, or has been done.
PWN_causes: A relation between two concepts where concept B comes into existence as a result of concept A.
PWN_similar: A relation between two concepts where concept A and concept B are closely related in meaning but are not in the same synset.
PWN_also: See also, a reference of weak meaning
PWN_attribute: A relation between nominal and adjectival concepts where the concept A is an attribute of concept B.
PWN_verb_group: Verb senses that similar in meaning and have been manually grouped together.
PWN_domain_topic: A relation between two concepts where B is a a scientific domain (e.g. computing, sport, biology, etc.) of concept A.
PWN_has_domain_topic: A relation between two concepts where A is a a scientific domain (e.g. computing, sport, biology, etc.) of concept B.
PWN_domain_region: A relation between two concepts where B is a geographical / cultural domain of concept A.
PWN_has_domain_region: A relation between two concepts where A is a geographical / cultural domain of concept B.
PWN_exemplifies: Indicates the usage of this word
PWN_is_exemplified_by: Indicates a word involved in the usage described by this word
------------------------------------------------------------------------------------------------------------------------------
agent: A relation between two concepts where concept A is typically the agent of the action expressed by concept B.
TKN_antonym: An opposite and inherently incompatible word
TKN_be_in_state: A relation between two concepts where concept A is qualified by concept B.
TKN_classified_by: A relation between concept B and a classifier concept A.
TKN_classifies: A relation between a classifier concept A and concept B.
TKN_co_agent_instrument: A relation between two concepts where concept B is the instrument used by concept A in a certain action.
TKN_co_agent_patient: A relation between two concepts where concept B is the patient undergoing an action carried out by concept A.
TKN_co_agent_result: A relation between two concepts where concept B is the result of an action carried out by concept A.
TKN_co_instrument_agent: A relation between two concepts where concept A is the instrument used by concept B for a certain action.
TKN_co_instrument_patient: A relation between two concepts where concept B undergoes an action for which the instrument expressed by concept A is used.
TKN_co_instrument_result: A relation between two concepts where concept B is the result of an action carried out by the instrument expressed by concept A.
TKN_co_patient_agent: A relation between two concepts where concept B undergoes an action carried out by concept A.
TKN_co_patient_instrument: A relation between two concepts where concept A undergoes an action for which the instrument expressed by concept A is used.
TKN_co_result_agent: A relation between two concepts where concept A is the result of an action carried out by concept B.
TKN_co_result_instrument: A relation between two concepts where concept A is the result of an action for which the instrument expressed by concept B is used.
TKN_co_role: A relation between two concepts where one concept undergoes an action in which the other concept is involved (bidirectional).
TKN_direction: A relation between two concepts where concept A is typically the direction or location of the action or event expressed by concept B.
TKN_eq_synonym: A relation between two concepts where A and B are equivalent concepts but their nature requires that they remain separate (e.g. Exemplifies)
TKN_holo_location: A relation between two concepts where concept B is a place located in concept A.
TKN_holo_portion: A relation between two concepts where concept B is an amount/piece/portion of concept A.
TKN_holonym: A relation between two concepts where concept A makes up a part of concept B.
TKN_in_manner: A relation between two concepts where concept B qualifies the manner in which an action or event expressed by concept A takes place.
TKN_instrument: A relation between two concepts where concept A is the instrument necessary for the action or event expressed by concept B.
TKN_involved_agent: A relation between two concepts where concept B is typically the agent of the action expressed by concept A.
TKN_involved_direction: A relation between two concepts where concept B is typically the direction or location of the action or event expressed by concept A.
TKN_involved_instrument: A relation between two concepts where concept B is typically the instrument necessary for the action or event expressed by concept A.
TKN_involved_location: A relation between two concepts where concept B is typically the location where the action or event expressed by concept A takes place.
TKN_involved_patient: A relation between two concepts where concept B is typically the patient un-dergoing an action or event expressed by concept A.
TKN_involved_result: A relation between two concepts where concept B comes into existence as a result of concept A.
TKN_involved_source_direction: A relation between two concepts where concept B is the place from where the action or event expressed by concept A begins/starts/happens.
TKN_involved_target_direction: A relation between two concepts where concept B is the place where the action or event expressed by concept A leads to.
TKN_involved: A relation between two concepts where concept B is typically involved in the action or event expressed by concept A.
TKN_is_caused_by: A relation between two concepts where concept A comes into existence as a result of concept B.
TKN_is_entailed_by: Opposite of entails
TKN_is_subevent_of: A relation between two concepts where concept A takes place during or as part of concept B, and whenever concept A takes place, concept B takes place.
TKN_location: A relation between two concepts where concept A is the location where the action or event expressed by concept B takes place.
TKN_manner_of: A relation between two concepts where concept A qualifies the manner in which an action or event expressed by concept B takes place.
TKN_mero_location: A relation between two concepts where concept A is a place located in concept B.
TKN_mero_portion: A relation between two concepts where concept A is an amount/piece/portion of concept B.
TKN_meronym: A relation between two concepts where concept B makes up a part of concept A.
TKN_other: Any relation not otherwise specified, please use dc:type attribute to give the name of exact relation.
TKN_patient: A relation between two concepts where concept A is the patient undergoing an action or event expressed by concept B.
TKN_pertainym: usually an adjective, which can be defined as "of or pertaining to" another word.
TKN_restricted_by: A relation between nominal (pronominal) concept B and an adjectival concept A (quantifier/determiner).
TKN_restricts: A relation between an adjectival concept A (quantifier/determiner) and a nominal (pronominal) concept B.
TKN_result: A relation between two concepts where concept A comes into existence as a result of concept B.
TKN_role: A relation between two concepts where concept A is typically involved in the action or event expressed by concept B.
TKN_source_direction: A relation between two concepts where concept A is the place from where the action or event expressed by concept B begins/starts/happens.
TKN_state_of: A relation between two concepts where concept B is qualified by concept A.
TKN_subevent: A relation between two concepts where concept B takes place during or as part of concept A, and whenever concept B takes place, concept A takes place.
TKN_target_direction: A relation between two concepts where concept A is the place where the action or event expressed by concept B leads to.
------------------------------------------------------------------------------------------------------------------------------     










## Usage

TO DO

## Contributing

TO DO

## License
TO DO