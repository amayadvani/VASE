import nltk

#Generate dataset using web crawler from UCI Machine Learning Repository
drugReviews = pd.read_csv('../data/drugReviews/drugsComTest_raw.tsv', delimiter='\t',encoding='utf-8')
drugReviews