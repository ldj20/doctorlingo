

====================================================================================================================================================
====================================================================================================================================================
Welcome to DoctorLingo!

This is the README for experienced devs, preferably, with python experience
if you are new to coding please see the README appropriately labeled
"README_for_noobs." Experienced devs, this is just a suggestion on how to
proceed with install, feel free to hack away as well.

Let's begin.

I hope you installed the main "karlscripts" folder to your home directory.
You don't have to install it in the home directory, but if it doesn't work,
then don't blame me. =P

====================================================================================================================================================
====================================================================================================================================================
Introduction:

This pipleline uses SpaCy v3.0.6 SciSpaCy v0.4.0 these are the newest versions
at the time of writing.

As the above were built on mostly python 3.7, that's the python version we use.

For these reasons, you should install this pipeline in a virtual environment.

Use a completely clean and new env. 

I use anaconda/conda. See official docs for install on your system (briefly below)

====================================================================================================================================================
====================================================================================================================================================
Install miniconda

Briefly:

install miniconda for your specific PC
https://docs.conda.io/en/latest/miniconda.html
Read the docs and if you run into trouble literally Google:
"How to install miniconda on X" where X is your Operating System/specs.

====================================================================================================================================================
====================================================================================================================================================
Set up conda environment

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

====================================================================================================================================================
====================================================================================================================================================
SpaCy install options:

Now it is time to install SpaCy, I built from source.

Try to do the source install if you are in a conda env, you should be largely 
protected from destroying your machine. If that doesn't work, then do the pip
install. Both are options are below.

~To Note: in the source install I also use multithreading 
If you don't want to use multithread install or cannot, then switch
the lines with '*#' before the comment and not just '#' as below.

~To Note: These docs were created when SpaCy 3.0.5 and 3.0.6 were the newest versions.
This install guide depends on "pip install." I included local copies of all the necessary
files in /karlscripts/SpaCy_Setup and /karlscripts/SciSpaCy_Setup.

pip install scispacy

becomes:

pip install ~/karlscripts/scispacy-main

====================================================================================================================================================
Option 1a: For building from source, on your terminal, one at a time, copy and paste the following commands:

===================COMMAND==========================||===========COMMENTS ABOUT COMMAND - DO NOT INCLUDE THIS IN TERMINAL===========================
cd ~/												# cd to home directory (you don't have to install here, but if it breaks don't blame me)
python -m pip install -U pip setuptools wheel 		# install/update build tools -  flibrary to facilitate packaging Python projects
git clone https://github.com/explosion/spaCy 		# clone spaCy from GitHub
cd spaCy                                      		# navigate into dir to where you installed SpaCy (don't worry conda will handle paths)
pip install -r requirements.txt               		# install required dependencies for SpaCy
python setup.py build_ext --inplace -j N	  		*# Build in parallel with N CPUs to speed up compilation and then install in editable mode, see alternative 1 in Option 1b below
python setup.py develop						  		*# the "develop" command is only used if compiling from source, see alternative 1 in Option 1b below
pip install -U pip install '.[cuda112,transformers,lookups,ja]'	# Finally pip install the NVIDIA cuda library (this must be specific to your videocard, where: cudaxyz
													# xyz are integers per your cuda version (can see this w/ nvcc --version) mine is 11.2, so cuda112
													# if you do not have an NVIDIA GPU do not worry about this and you can remove the "cudaxyz" from the
													# command, however, still install the transformers and lookups libraries, this pipeline was developed
													# with a GPU, but a lot of it is written with threading in mind for CPUs, so you shouldn't suffer that much.
													
													if not using GPU - i.e. $pip install -U pip install '.[cuda112,transformers,lookups,ja]' #don't include $ sign in terminal


THE BELOW PACKAGES ARE FOR DIFFERENT LANGUAGES THESE ARE OPTIONAL
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


====================================================================================================================================================
Option 1b: For building from source, but without multithreading compiler (slower;easier) 
====================================================================================================================================================
YOU STILL NEED TO PERFORM COMMANDS 1-4 above from Option 1a -- then replace last two commands with the following below:

===================COMMAND==========================||===========COMMENTS ABOUT COMMAND - DO NOT INCLUDE THIS IN TERMINAL===========================
pip install --no-build-isolation --editable . # compile and install spaCy (YOU DO NEED TO INCLUDE THAT PERIOD AT END OF COMMAND)




====================================================================================================================================================
Option 3: Do not compile from source, use a pre-compiled wheel from the Explosion developers:

===================COMMAND==========================||===========COMMENTS ABOUT COMMAND - DO NOT INCLUDE THIS IN TERMINAL===========================
cd ~/												# cd to home directory (you don't have to install here, but if it breaks don't blame me)
pip install -U pip setuptools wheel					# python -m pip install -U pip setuptools wheel 		# install/update build tools -  flibrary to facilitate packaging Python projects
pip install -U spacy[cuda102,transformers,lookups] 	#Finally pip install the NVIDIA cuda library (this must be specific to your videocard, where: cudaxyz
													# xyz are integers per your cuda version (can see this w/ nvcc --version) mine is 10.1, so cuda101
													# if you do not have an NVIDIA GPU do not worry about this and you can remove the "cudaxxx" from the
													# command, however, still install the transformers and lookups libraries, this pipeline was developed
													# with a GPU, but a lot of it is written with threading in mind for CPUs, so you shouldn't suffer that much.

python -m spacy download en_core_web_sm


Then use pip install on the terminal to install the following packages
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

