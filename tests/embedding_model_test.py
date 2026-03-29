from models.embedding_model import embed_model

emb = embed_model.encode(["This is a test sentence"])

print('Embedding shape:', emb.shape)
