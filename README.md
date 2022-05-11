# Automatter
Automatter is an automation tool to sorts a series of texts into groups based on subject matter.



## Datasets
Uses data from [ArXiv's Kaggle Dataset](https://www.kaggle.com/datasets/Cornell-University/arxiv) containing abstracts and full-texts.



## Code

### Text Cleaning
Before any similarity functions are used, the texts are cleaned using NLTK's Stopwords corpus and Lemmatiser function.
Then, one of several methods are used:
1. **Self-built Cosine Similarity**
2. **Google's Word2Vec Cosine Similarity**

Once the text's word embeddings are obtained, they can be clustered using one of several clustering algorithms.
1. **K-Means Clustering**
2. **Artificial Neural Network**
