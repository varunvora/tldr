# tldr
## Extractive Text Summarization

Report: https://drive.google.com/open?id=1rAOeshfeoWcK6LjFw5X8-nwRlIa_f-Gy

Dataset : https://www.kaggle.com/sunnysai12345/news-summary/data (Inshorts News Summary)

## Description
This repository contains the code to summarise news articles using classical information retrieval techniques. This is done in 2 ways
1. TfIdf (see tfidf.py)
2. Bayes Theorem (see bayes.py)

news_summary.csv : The dataset from Kaggle containing news articles and summaries. (among some other attributes)

csv_to_dataset.py: Reads the above CSV file and saves it in a pickled format (dataset.pkl)

dataset_tokenize.py: Reads dataset.pkl using dataset_loader.py and stores it in clean_dataset.pkl

demo.py: Contains a demo of summarising

 

