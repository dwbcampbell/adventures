import re
import numpy as np
import matplotlib.pyplot as plt
from gensim.models import Word2Vec
from sklearn.manifold import TSNE

# Load the book text
with open('book.txt', 'r') as file:
    book_text = file.read()

# Pre-process the text to remove punctuation and convert to lowercase
book_text = book_text.lower()
book_text = re.sub(r'[^a-zA-Z0-9\s]', '', book_text)

# Tokenize the text into a list of sentences
sentences = re.split(r'[.?!]', book_text)
sentences = [sentence.strip().split() for sentence in sentences]

# Train the Word2Vec model on the book text
model = Word2Vec(sentences, vector_size=100, window=5, min_count=5, workers=4)

# Extract the word embeddings
word_vectors = model.wv

# Select a subset of words to visualize
# words = ['logic', 'induction', 'deduction', 'inference', 'deductive', 'inductive', 'reasoning', 'truth', 'evidence', 'premise', 'conclusion', 'valid', 'invalid', 'probability', 'cause', 'effect', 'indicator', 'consequence', 'argument', 'fallacy',
#         'proposition', 'cognition', 'cognitivist', 'intuition', 'critical', 'analysis', 'method', 'science', 'systematic', 'explanation', 'know', 'knowledge', 'justification', 'correction', 'indeterminacy', 'hypothesis', 'test', 'observation']

words = ['true', 'false', 'valid', 'invalid', 'induction', 'premise', 'reason', 'reasoning', 'logic',
         'deduction', 'fallacy', 'truth', 'falsehood', 'cause', 'effect', 'evidence', 'conclusion']

# select words that are in the word embeddings
words = [word for word in words if word in word_vectors.key_to_index]
print(words)

word_embeddings = np.array([word_vectors[word] for word in words])

# Reduce the dimensions of the word embeddings using t-SNE
tsne = TSNE(n_components=2, perplexity=10)
word_embeddings_2d = tsne.fit_transform(word_embeddings)

# Plot the word embeddings in a scatter plot
plt.figure(figsize=(10, 8))
plt.scatter(word_embeddings_2d[:, 0], word_embeddings_2d[:, 1])

# Add labels to the points in the scatter plot
for i, word in enumerate(words):
    plt.annotate(word, xy=(word_embeddings_2d[i, 0], word_embeddings_2d[i, 1]))

# Show the scatter plot
plt.show()
