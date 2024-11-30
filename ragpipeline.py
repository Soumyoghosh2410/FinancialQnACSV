from sentence_transformers import SentenceTransformer
import faiss
import pandas as pd
import numpy as np

# Load cleaned data
data = pd.read_csv('cleaned_sales_data.csv')

# Prepare textual data for embedding (e.g., PRODUCTLINE, STATUS, CUSTOMERNAME)
data['Textual_Data'] = data['PRODUCTLINE'] + ' ' + data['STATUS'] + ' ' + data['CUSTOMERNAME']
textual_data = data['Textual_Data'].tolist()

# Initialize embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Create embeddings
embeddings = model.encode(textual_data)

# Initialize FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

# Define RAG-based query function
def rag_query(user_query):
    # Generate query embedding
    query_embedding = model.encode([user_query])
    # Search FAISS index
    distances, indices = index.search(query_embedding, k=5)
    # Retrieve relevant data
    results = data.iloc[indices[0]]
    return results

# Example query
if __name__ == "__main__":
    query_result = rag_query("Top customers in the USA")
    print(query_result)