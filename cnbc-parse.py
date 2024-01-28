import json
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

with open('output.json', 'r') as openfile:
    json_object = json.load(openfile)

tokenizers = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

for key in json_object['data']['symbolEntries']['results']:
    print('Title:', key['title'])
    print('Description:', key['description'])

