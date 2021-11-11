import gensim.downloader as api
info = api.info()
model = api.load("word2vec-google-news-300")
