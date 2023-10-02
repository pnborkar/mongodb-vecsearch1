# mongodb-vecsearch1
1. Make sure to install pymongo before executing the code (pip install pymongo)

<img width="534" alt="image" src="https://github.com/pnborkar/mongodb-vecsearch1/assets/1790943/68bcf54b-ca66-4b81-b373-83b5555f5a33">

2. Get the API from OpenAI or Huggingface in order to the vector embeddings to be stored in your document database

   <img width="834" alt="image" src="https://github.com/pnborkar/mongodb-vecsearch1/assets/1790943/6abc25f7-7119-4e31-ae4f-5665a14c6c55">

3. In your MongoDB database settings, create the Vector Search Index (follow the [Vector Search documentation](https://www.mongodb.com/docs/atlas/atlas-search/vector-search/))
 
<img width="449" alt="image" src="https://github.com/pnborkar/mongodb-vecsearch1/assets/1790943/85da0644-07cf-457b-8df3-67cba7f0f2ae">

4. Now get the Triggers (secret = OpenAI API key) on your MongoDB database. This basically triggers a function when the document is updated or inserted  (Connect to your Cluster-> Database-> AppServices -> Triggers -> Values)

   <img width="799" alt="image" src="https://github.com/pnborkar/mongodb-vecsearch1/assets/1790943/dd02cd21-2dda-41ba-acf9-44f1dfae7b82">

5. 
