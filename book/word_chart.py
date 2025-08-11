import re
import numpy as np
import matplotlib.pyplot as plt
from gensim.models import Word2Vec
from sklearn.manifold import TSNE

# create a Word2Vec model
model = gensim.models.Word2Vec()