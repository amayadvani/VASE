
#import pandas as pd
#import numpy as np
#import seaborn as sns

#import nltk
#Generate dataset using web crawler from UCI Machine Learning Repository
#drugReviews = pd.read_csv('/mnt/c/data/drugsCom_raw/drugsComTest_raw.tsv', delimiter='\t',encoding='utf-8')
#print(drugReviews)

# Clean the data
# Remove unusable data such as html tags
# Replace nominal categorical data replaced with ordinal categorical data because we need to use classifiers
#dfClean['integerCondition'] = dfClean['condition'].map(condMapping)

# Remove stopwords
#words = stopwords.words()
#dfClean['cleanedReview'] = dfClean['review'].apply(lambda x: " ".join([stemmer.stem(i) for i in re.sub("[^a-zA-Z]", " ",x).split() if i not in words]).lower())
#dfClean

# TF-DF Vectorization

# Classification
#pipeline = Pipeline([('vect', vectorizer),
                     #('clf', SGDClassifier(loss='modified_huber', max_iter=5, tol=None))])
#model = pipeline.fit(X_train, y_train)
#with open('RandomForest.pickle', 'wb') as f:
    #pickle.dump(model, f)
#ytest = np.array(y_test)
#y_hat = model.predict(X_test)
#print(accuracy_score(y_test, y_hat))
#print(classification_report(ytest, y_hat ))
#print(confusion_matrix(ytest, y_hat))

#resultInteger = model.predict([
#"unable to sleep properly", 
#"pain in my abdomen", 
#"severe headache and nasuea", 
#"red, itchy and watery eyes", 
#"lose motions and stomach upset",
#"looking to reduce smoking and possibly quit",
#"concerned that i am pregnant and don't want to have this baby", 
#"pain in my forehead and temples, unable to sleep properly",
#"feeling bloated and like my food comes up to my throat like acid reflux", 
#"feeling weak and don't want to eat food. Feeling anxious about exams.", 
#"feeling stressed, been unable to sleep and spending too much time worrying", 
#"coughing violently and throat is sore",
#"my son is aggressive and violent does not listen, easily distracted", 
#"my daughter is having irregular periods and is suffering from pain",
#"i am unable to pass urine easily, i feel pain when going to the toilet",
#"i am feeling tired and anxious."
#])
#resultCond = [int_to_cond.get(r) for r in resultInteger]
#resultCond

