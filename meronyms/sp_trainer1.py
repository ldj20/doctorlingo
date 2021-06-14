import spacy
spacy.prefer_gpu()
from spacy.matcher import Matcher
import os





patterns = [
[{"POS": "NOUN"}, {"TEXT": "is part of"}, {"POS": "NOUN"}],
[{"POS": "NOUN"}, {"TEXT": "made of"}, {"POS": "NOUN"}],
[{"POS": "NOUN"}, {"TEXT": "to make"}, {"POS": "NOUN"}],
[{"POS": "NOUN"}, {"TEXT": "made from"}, {"POS": "NOUN"}],
[{"POS": "NOUN"}, {"TEXT": "'s"}, {"POS": "NOUN"}],
[{"POS": "NOUN"}, {"TEXT": "of the"}, {"POS": "NOUN"}],
[{"POS": "NOUN"}, {"TEXT": "of"}, {"POS": "NOUN"}],
[{"POS": "NOUN"},{"POS": "VERB"}, {"TEXT": "has"}, {"POS": "NOUN"}],
[{"POS": "NOUN"},{"POS": "VERB"}, {"TEXT": "has"}, {"POS": "NOUN"}],
[{"TEXT": "is a"}, {"POS": "NOUN"}, {"TEXT": "of"}, {"POS": "NOUN"}],
[{"TEXT": "the"}, {"POS": "NOUN"}, {"TEXT": "'s"}, {"POS": "NOUN"}],
[{"POS": "NOUN"}, {"TEXT": "component of"}, {"POS": "NOUN"}],
[{"POS": "NOUN"}, {"TEXT": "consists of"}, {"POS": "NOUN"}],
[{"POS": "NOUN"}, {"TEXT": "member of"}, {"POS": "NOUN"}],
[{"POS": "NOUN"}, {"TEXT": "portion of"}, {"POS": "NOUN"}],
[{"POS": "NOUN"}, {"TEXT": "stuff of"}, {"POS": "NOUN"}],
[{"POS": "NOUN"}, {"TEXT": "located in"}, {"POS": "NOUN"}],
[{"POS": "NOUN"}, {"TEXT": "contained in of"}, {"POS": "NOUN"}],
[{"POS": "NOUN"}, {"TEXT": "phase of"}, {"POS": "NOUN"}],
[{"POS": "NOUN"}, {"TEXT": "participates in"}, {"POS": "NOUN"}],
[{"POS": "NOUN"}, {"TEXT": "component"}, {"TEXT": "of"}, {"POS": "NOUN"}],
[{"POS": "NOUN"}, {"TEXT": "consists"}, {"TEXT": "of"}, {"POS": "NOUN"}],
[{"POS": "NOUN"}, {"TEXT": "member"}, {"TEXT": "of"}, {"POS": "NOUN"}],
[{"POS": "NOUN"}, {"TEXT": "portion"}, {"TEXT": "of"}, {"POS": "NOUN"}],
[{"POS": "NOUN"}, {"TEXT": "stuff"}, {"TEXT": "of"}, {"POS": "NOUN"}],
[{"POS": "NOUN"}, {"TEXT": "located"}, {"TEXT": "in"}, {"POS": "NOUN"}],
[{"POS": "NOUN"}, {"TEXT": "contained"}, {"TEXT": "in"}, {"POS": "NOUN"}],
[{"POS": "NOUN"}, {"TEXT": "phase"}, {"TEXT": "of"}, {"POS": "NOUN"}],
[{"POS": "NOUN"}, {"TEXT": "participates"}, {"TEXT": "in"}, {"POS": "NOUN"}]
]



for file in os.listdir("./wiki_output/"):
	try:
		if file.endswith(".txt"):
			filename = os.path.join("./wiki_output/", file)
			with open(filename) as f:
				nlp = spacy.load("en_core_web_trf")
				matcher = Matcher(nlp.vocab)
				nlp.max_length = 300000
				TEXTS = f.read()
				#print(TEXTS[0:100])
				matcher.add("MERONYM", patterns)
				doc = nlp(TEXTS)
				matches = matcher(doc)
				for match_id, start, end in matches:

					string_id = nlp.vocab.strings[match_id]  # Get string representation
					extended_start = int(start)-25
					extended_end = int(end)+25
					span = doc[start:end]
					extended_span = doc[extended_start:extended_end]  # The matched span
					span_text = extended_span.text
					match_text = span.text
					results = string_id, start, end, span.text, extended_start, extended_end, extended_span.text
					span_index_token_start = span_text.find(match_text)
					span_index_token_end = span_index_token_start + len(match_text.split(' ')[0])
					#print(results)
					print(span_text)
					resultfile = "./pattern_output_data.txt"
					#print(nlp.pipe_names)
					with open(resultfile, "a") as new_text_file:
						string_results = str(results)
						new_text_file.write(span_text+'\n')
			doc = None
			nlp = None

		else:
			print("error while reading directory in line 16 of script")

	except RuntimeError:
		print (str(file))
"""

			for match_id, start, end in matches:
				string_id = nlp.vocab.strings[match_id]  # Get string representation
				extended_start = int(start)-25
				extended_end = int(end)+25
				span = doc[start:end]
				extended_span = doc[extended_start:extended_end]  # The matched span
				results = match_id, string_id, start, end, span.text, extended_start, extended_end, extended_span.text
				print(results)
				resultfile = "./real_MERONYM_output.txt"
				print(nlp.pipe_names)
				with open(resultfile, "a") as new_text_file:
					string_results = str(results)
					new_text_file.write(string_results)
		doc = None
		nlp = None

	else:
		print("error while reading directory in line 16 of script")

except RuntimeError:
	print (str(file))


'"{text": ' extended_span.text, ', '"spans": [{"text":'span.text[0:int(end)-int(start), ', "start":'str(span.text[0:int(end)-int(start))[0]}

{"text": "Furthermore, Smad-phosphorylation was followed by upregulation of Id1 mRNA and Id1 protein, whereas Id2 and Id3 expression was not affected.", 
"spans": [{"text": "Smad", "start": 13, "token_start": 2, "token_end": 2, "end": 17, "type": "span", "label": "GGP"}

{"text": "the text", "spans": [{"text": "Token text", "start": Int index of tokens first letter in string of text, "token_start": the int index of token in all tokens, 
"token_end": same as before - same as start if one token, if noun phrase then end on last token, "end": index of tokens last letter, "type": "span", label "MERONYM"}
"""

#[(token.text,token.idx) for token in parsed_sentence]

# Create a Doc object for each text in TEXTS

	# Match on the doc and create a list of matched spans
	#spans = [doc[start:end]
	# Get (start character, end character, label) tuples of matches
	#entities = [(span.start_char, span.end_char, "MERONYM") for span in spans]
	# Format the matches as a (doc.text, entities) tuple
	#training_example = (doc.text, {"entities": entities})
	# Append the example to the training data
	#TRAINING_DATA.append(training_example)

#print(*TRAINING_DATA, sep="\n")

# grade this against the hearst patterns as 1/2 patterns for just hyponyms with inference of downstream hyponyms
# to find in parse tree to suite SpaCy
