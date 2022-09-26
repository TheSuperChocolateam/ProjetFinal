import feedparser

NewsFeed = feedparser.parse("https://www.cert.ssi.gouv.fr/")
print ('Number of RSS posts :', len(NewsFeed.entries))
entry = NewsFeed.entries[1]
print ('Post Title :', entry.title)