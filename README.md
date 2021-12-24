# hyperskill_key_terms_extraction
The project that extracts the most important words in given xml (using NLP)

The importance of the words is calculated with TfidfVectorizer().

The algorythm:

Read an XML-file containing stories and headlines.
Extract the headers and the text.
Tokenize each text.
Lemmatize each word in the story.
Get rid of punctuation, stopwords, and non-nouns with the help of NLTK.
Count the TF-IDF metric for each word in all stories.
Pick the five best scoring words.
Print each story's headline and the five most frequent words in descending order. Take a look at the sample output below. Display the titles and keywords in the same order they are presented in the file.
