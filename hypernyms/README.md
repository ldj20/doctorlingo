
# Hypernym Usage:
## Getting started:
### Setting up environment


**Install Conda**
https://www.anaconda.com/
 very simple for any OS, go to website and install for your system specs

Open anaconda navigator 
 if linux must do this from command line ($ anacondanavigator)
 recommend doing this from the base directory you want your workspace if linux /home/username/
 if windows or mac they have gui install and shortcut launch for navigator (just search "anaconda navigator"  then see below)

Once in the navigator tab:
On the most left hand side columns  click Environments
After clicking it you will see a column appear with a "base" environment
At the bottom of that column (very bottom of window)  click the [+] create button
Enter the name you want for the environment
Keep python 3.8 selected, ignore R, leave unchecked

Now click your newly made environment in same colume that "base" environment was in
You will see an open in terminal window
This opens to the home folder of that environment


### Setting up SpaCy for Hypernym extraction

You can now start installing spaCy environments
Remember there are two spaCy environments needed, one for ScispaCy packages, and one without
It may be a good idea to create another environment at this point with a different name for the one with SciSpacy packages

Let's start building the hypernym extractor library first as its the easiest spaCy set up (for the most part):
open the environment you made for use WITHOUT scispaCy
make sure the environment is "activated", in front of the terminal entry line where your root directory is listed, you should see:
"(name of environment)"  actually in parenthesis, not in quotes lol

**Begin installing spaCy 3.0**
Go to https://spacy.io/usage
Go to the widget under the subheading "Install spaCy"

Fill in the details of your machine:

Operating system: I am on linux

Package manager: I use pip to install(despite being in Conda environment for a little more control per my familiarity with it)

**Hardware**
I will select GPU for a faster run time
make sure you have pip installed "cudatoolkit" for your GPU  check the version from terminal line afterwards w/ $ nvcc version

activate your conda environment and enter: nvcc version 

(hypernyms) karl@KarlKruncher:/home/karl$ nvcc version
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 20052019 NVIDIA Corporation
Built on Sun_Jul_28_19:07:16_PDT_2019
Cuda compilation tools, release 10.1, V10.1.243
Whatever your cuda model is  specify that for the spaCy web installer mine is (10.1), they default to 10.2
Configuration select: "train models"  this denotes which pretrained model they give you  if can work with transformers and what not etc
Trained pipelines: Ensure english is selected if you are working in english, or select languages otherwise (I don't know if this works with other languages  probs spaCy is good like that)
Select pipeline for: accuracy  this also helps select the mdoel it has you download  we need this


**The above input into spaCy's installer widget generates these install commands:**
$ pip install U pip setuptools wheel
$ pip install U spacy[cuda101,transformers,lookups]
$ python m spacy download en_core_web_sm


## Using python to extract hypernyms with spaCy


After we run those commands and now we are ready to go use our python scripts for hypernyms:
But first! We need text data to extract hypernyms from (often a bottleneck in production)
For our text run of hypernym prediction I scraped wikipedia for all of the hypernyms based on hearst patterns
(source citation: https://people.ischool.berkeley.edu/~hearst/papers/coling92.pdf)

### Scraping wikipedia to get text for hypernym extraction**

**pip install wikipedia**
(this installs the necessary modules for scraping wikipedia)
(if you try to run the below script and it errors with a Module error try just literally pip installing that module name)
(this shouldn't happen for this specific module but for future modules remember this advice)

**Wikipedia_text.py**
This script calls required modules, then has a very long list of wikipedia articles to scrape. This list is all of the article names for every listed cancer in the NCI database, you can edit this for any wikipedia article name. Under this massive list is the actual meat of the script which scrapes wikipedia with its respective module. 

Usage: $python wikipedia_text.py

requires the pip install above spaCy modules

Outputs articles as cleaned and processed text files to dir in script, which you can edit if needed

### Extracting hypernyms

There were a few hypernym extractors I tried out, notably, one I wrote and one from GitHub, the I won’t include the one from GitHub because its output is all crazy because it searches for patterns with Regex post-processing was more work than I wanted, and I just used it for testing. If you want this, see: https://github.com/abyssnlp/Hearst-Hypernym-Extractor its pretty good, than a little less sensitive the spaCy model/pattern matcher we use. You can also find this code in this repo, under the "repos_tests_scratch_old" directory.


**Running extractor: sp_trainer1.py**
(In brief this script again has a massive intro with dictionaries instead of a list, these dictionaries hold the actual hearst patterns written in a way that the spaCy pretrained models can understand [mostly identifying tokens as nouns and finding relational nouns surrounding, it based on the hearst patterns])
(It searches by iterating through the wikipedia output, which is stored as a text document for each article it scraped)
(It currently outputs examples with the token identified with hyponym, then more surrounding textual context, may modify this for trainer)

*Usage: $python sp_trainer1.py* 
The script requires output from wikipedia_text.py from above 

## Predicting hypernyms

Next up and in progress
To build the hypernymy model for the hem/onc subset and the full corpus w/ UMLS basis - need to extract all hypernym relationships from UMLS
These are stored in files relating AUIs in UMLS as is_a relationship - so we will need to generate the sentences in heart hypernym format to build the NER recognizer that will no longer rely on pattern matching. Pattern matching in general is about 85% accurate, the NER model should be much better. This will aid us in being to generate new entries to doctorlingo on the fly.

## Verify the extracted hypernyms by running the hypernym hyponym pairs against wordnet

Wordnet's original basis in PWN was developed by lexicographers, and linguists. Therefore that is gold standard for most hypernymy relationships/pairs. We can validate our NER model's accuracy if it can pick up hypernyms from examples that are shared between UMLS and Wordnet, i.e. atrial fibrillation.

The valid pairs with context can be used to further train the SpaCy model for improved accuracy and specificity of hypernymy detection

## Rel_component

This folder contains a full start to finish spaCy example of how to develop a custom NER model. I am including this here just FYI - there is an associated youtube video that walks you through this (see below). We use prodigy instead which is much more intuitive. The datafiles from the trained prodigy model are stored in the "train-data" directory and can be pickled, or used for further training, testing etc. This requires prodigy to be set up and is mostly run from the command line and the interactive prodigy browser which is launch in your html/web browser. See prodigy's website for full documentation. If you are on our dev team - just ask me to schedule a time to help you get set up with this. Alternatively, you can build a model straight from CLI with spaCy and python - as per the Rel_component example, or spaCy's official docs.