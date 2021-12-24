from lxml import etree
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import string

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()

root = etree.parse("news.xml").getroot()

dataset = []

lemmatizer = WordNetLemmatizer()

titles = []

for elem_news in root[0]:
    title = elem_news[0].text
    text = elem_news[1].text

    titles.append(title)

    tokens = nltk.tokenize.word_tokenize(text.lower())

    list_of_words = []
    for token in tokens:
        lem_token = lemmatizer.lemmatize(token)
        if lem_token in (stopwords.words("english")) \
                or lem_token in list(string.punctuation):
            continue
        if nltk.pos_tag([lem_token])[0][1] != "NN":
            continue
        list_of_words.append(lem_token)

    res = ""
    for i in list_of_words:
        res += i + " "
    dataset.append(res.strip())

tfidf_matrix = vectorizer.fit_transform(dataset)

tfidf_matrix = tfidf_matrix.toarray()

terms = vectorizer.get_feature_names_out()

i = 0
for row in tfidf_matrix:
    print(titles[i] + ":")
    data = zip(row, terms)
    sorted_data = sorted(data, key=lambda x: (x[0], x[1]), reverse=True)
    # print(sorted_data)
    j = 0
    for elem in sorted_data:
        print(elem[1], end=" ")
        j += 1
        if j == 5:
            break
    print("\n")
    i += 1



