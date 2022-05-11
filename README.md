# ReplicAIt
Text Plagiarism Checker

---

## Datasets
Uses data from [ArXiv's Kaggle Dataset](https://www.kaggle.com/datasets/Cornell-University/arxiv) containing abstracts and full-texts.

---

## Code

### Text Cleaning
Before any similarity functions are used, the texts are cleaned using NLTK's Stopwords corpus and Lemmatiser function.
Then, one of several methods are used:
1. **Self-built Cosine Similarity**
2. **Google's Word2Vec Cosine Similarity**
