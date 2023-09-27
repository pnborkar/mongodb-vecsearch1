
import pymongo
import os
import openai

client = pymongo.MongoClient("mongodb+srv://<user>:<password>@cluster0.vtuioyd.mongodb.net/")
db = client.sample_mflix
collection = db.embedded_movies

openai.api_key = "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"

model = "text-embedding-ada-002"

def generate_embedding(text: str) -> list[float]:
	resp = openai.Embedding.create(
		input=[text], 
		model=model)

	return resp["data"][0]["embedding"] 

query = "imaginary characters from outer space at war"
print('\nLooking for movies with the following plot —> \"' + query + "\"" )
print(">\n")
results = collection.aggregate([
    {
        '$search': {
            "index": "PlotSearch",
            "knnBeta": {
                "vector": generate_embedding(query),
                "k": 10,
                "path": "plot_embedding"}
        }
    }
])

for document in results:
    print(f'Movie Name: {document["title"]},\nMovie Plot: {document["plot"]}\n')
