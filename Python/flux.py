import feedparser

print ("FLUX RSS CERT")
NewsFeed = feedparser.parse("https://www.cert.ssi.gouv.fr/alerte/feed/")
print ('Number of RSS posts :', len(NewsFeed.entries))

i=0
while i != 6:
    entry = NewsFeed.entries[i] 
    print (entry.published) 
    print ("******")
    print ("Titre :", entry.title)
    print ("Description :", entry.summary) 
    print ("------News Link--------")
    print (entry.link) 
    i+=1

print ("FLUX RSS NVD")
NewsFeed = feedparser.parse("https://www.nist.gov/news-events/news/rss.xml")
print ('Number of RSS posts :', len(NewsFeed.entries))

j=0
while j != 6:
    entry = NewsFeed.entries[i] 
    print (entry.published) 
    print ("******")
    print ("Titre :", entry.title)
    print ("Description :", entry.summary) 
    print ("------News Link--------")
    print (entry.link) 
    j+=1