from tfidf import ExtractiveSummarizer_tfidf
from bayes import ExtractiveSummarizer_bayes
import random
import pickle

space = "---" * 72 + "--"

if __name__ == "__main__":
    article, actual_summary = None, None
    with open("dataset.pkl", "rb") as fp:
        x, y = pickle.load(fp)
    seed = random.randrange(len(x))

    print("TLDR\n")
    choice = input("Choose one of the following\n1. New article\n2. Random article from dataset\nYour choice : ")
    if choice == "1":
        f = open("article_file.txt", "r")
        article = f.read()
        f.close()
        article = " ".join(article.split())
    elif choice == "2":
        article = x[seed]
        actual_summary = y[seed]
    else:
        print("Invalid choice")
        quit()

    bayes_summarizer = ExtractiveSummarizer_bayes(corpus="clean_dataset")
    bayes_summary = bayes_summarizer.bayes_summarizer(article)

    tfidf_summarizer = ExtractiveSummarizer_tfidf(corpus="clean_dataset")
    tfidf_summary = tfidf_summarizer.tf_idf_summarizer(article)

    print(space)
    print("ARTICLE", article, sep="\n")
    print()
    print(space)
    if choice == "2":
        print("ACTUAL SUMMARY\n", actual_summary, sep="\n")
        print(space)
    print("EXTRACTIVE SUMMARY USING BAYES\n", bayes_summary, sep="\n")

    print(space)
    print("EXTRACTIVE SUMMARY USING TFIDF\n", tfidf_summary, sep="\n")
    print(space)
