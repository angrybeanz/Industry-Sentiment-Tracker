import cnbc
import json

api_key = '2e53850264msh693f75558afff58p10b08ejsnee185b9ae8da'

json_resp = cnbc.list_symbol_news(symbol='AAPL',
                                  api_key=api_key)



with open('output.json', 'r') as openfile:
    json_object = json.load(openfile)

with open("output.json", "w") as outfile:
    json.dump(json_resp, outfile)