from textblob import TextBlob

text = "I had a really horrible day. It was the worst day ever! But every now and then I have a really good day that makes me happy."
blob = TextBlob(text)

print(blob.sentiment_assessments.polarity)
# -0.125

print(blob.sentiment_assessments.subjectivity)
# 0.9

print(blob.sentiment_assessments.assessments)
# [(['really', 'horrible'], -1.0, 1.0, None), (['worst', '!'], -1.0, 1.0, None), (['really', 'good'], 0.7, 0.6000000000000001, None), (['happy'], 0.8, 1.0, None)]

print(blob.ngrams())
# [WordList(['I', 'had', 'a']), WordList(['had', 'a', 'really']), WordList(['a', 'really', 'horrible']), WordList(['really', 'horrible', 'day']), WordList(['horrible', 'day', 'It']), WordList(['day', 'It', 'was']), WordList(['It', 'was', 'the']), WordList(['was', 'the', 'worst']), WordList(['the', 'worst', 'day']), WordList(['worst', 'day', 'ever']), WordList(['day', 'ever', 'But']), WordList(['ever', 'But', 'every']), WordList(['But', 'every', 'now']), WordList(['every', 'now', 'and']), WordList(['now', 'and', 'then']), WordList(['and', 'then', 'I']), WordList(['then', 'I', 'have']), WordList(['I', 'have', 'a']), WordList(['have', 'a', 'really']), WordList(['a', 'really', 'good']), WordList(['really', 'good', 'day']), WordList(['good', 'day', 'that']), WordList(['day', 'that', 'makes']), WordList(['that', 'makes', 'me']), WordList(['makes', 'me', 'happy'])]