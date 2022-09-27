import feedparser

def flux():
    print ("-------")
    print ("FLUX RSS CERT")
    NewsFeedCert = feedparser.parse("https://www.cert.ssi.gouv.fr/alerte/feed/")
    print ('Number of RSS posts :', len(NewsFeedCert.entries))

    i=0
    while i != 3:
        print ("******")
        entry = NewsFeedCert.entries[i] 
        print (entry.published) 
        print ("Titre :", entry.title)
        print ("Description :", entry.summary) 
        print ("News Link :", entry.link)
        i+=1

    print ("-------")
    print ("FLUX RSS NVD")
    NewsFeedNist = feedparser.parse("https://www.nist.gov/news-events/news/rss.xml")
    print ('Number of RSS posts :', len(NewsFeedNist.entries))

    j=0
    while j != 3:
        print ("******")
        entry = NewsFeedNist.entries[j] 
        print (entry.published)  
        print ("Titre :", entry.title)
        print ("Description :", entry.summary) 
        print ("News Link :", entry.link)
        j+=1
    
    return len(NewsFeedNist.entries), entry.published, entry.title,  entry.summary, entry.link


if __name__ == "__main__":
    print(flux())