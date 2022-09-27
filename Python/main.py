from flask import Flask, render_template, request, send_file, redirect, url_for, Response, redirect
import feedparser

app = Flask(__name__)

NewsFeedNist = feedparser.parse("https://www.nist.gov/news-events/news/rss.xml")
tab_entries= []

print(type(tab_entries))

j=0
while j != 3:
    entry = NewsFeedNist.entries[j] 
    date = entry.published
    title = entry.title  
    description = entry.summary
    link = entry.link
    tab_entries.append({"date":date, "title":title, "description":description, "link":link})
    j+=1

print(tab_entries[0])

@app.route('/')
def menu():    
    return render_template("index.html", len= len(tab_entries), entries=tab_entries)
    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5501)