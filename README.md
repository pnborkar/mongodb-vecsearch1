# mongodb-vecsearch1
1. Make sure to install pymongo before executing the code (pip install pymongo)

 <img width="420" alt="image" src="https://drive.google.com/uc?export=view&id=1U7YzEQD2Aj0uC2_vrn_6miqohIn9UZH8">

2. Get the API from OpenAI or Huggingface in order to generate the vector embeddings to be stored in your document database

   <img width="834" alt="image" src="https://github.com/pnborkar/mongodb-vecsearch1/assets/1790943/6abc25f7-7119-4e31-ae4f-5665a14c6c55">

3. In your MongoDB database settings, create the Vector Search Index (follow the [Vector Search documentation](https://www.mongodb.com/docs/atlas/atlas-search/vector-search/))
 
<img width="449" alt="image" src="https://github.com/pnborkar/mongodb-vecsearch1/assets/1790943/85da0644-07cf-457b-8df3-67cba7f0f2ae">

4. Now get the Triggers (secret = OpenAI API key) on your MongoDB database. This basically triggers a function when the document is updated or inserted  (Connect to your Cluster-> Database-> AppServices -> Triggers -> Values)

<img width="899" alt="image" src="https://github.com/pnborkar/mongodb-vecsearch1/assets/1790943/4d8bf2ab-b9f0-4ccd-94de-4634e486022e">

5. Get the function as triggers for insert and update as follows. (see trigger function)

 <img width="890" alt="image" src="https://github.com/pnborkar/mongodb-vecsearch1/assets/1790943/2ad4f11d-3b6d-4d6d-a245-c61a93bf3445">

6. Import the sample database data
   
7. You are set to run the script on the MongoDB database to do a vector search! 
