import json
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

with open('output.json', 'r') as openfile:
    articles = json.load(openfile)

tokenizers = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

ratings = {}
for industry in articles:
    ratings[industry] = {}
    industry_articles = articles[industry]
    for i in range(1, 6):
        ratings[industry][i] = 0
    
    for article in industry_articles:
        title = article['title']
        tokens = tokenizers.encode(title, return_tensors='pt')
        result = model(tokens)
        score = int(torch.argmax(result.logits))+1
        ratings[industry][score] += 1

with open("ratings.json", "w") as outfile:
    json.dump(ratings, outfile)

