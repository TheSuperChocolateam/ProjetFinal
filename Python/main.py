from flask import Flask, render_template, request, send_file, redirect, url_for, Response, redirect
import requests
import feedparser
import matplotlib.pyplot as plt

app = Flask(__name__)

# Récupération flux RSS des alertes sécurités NVD avec requests
response_info = requests.get(
    "https://services.nvd.nist.gov/rest/json/cves/2.0/?pubStartDate=2022-09-01T00:00:00.000-05:00&pubEndDate=2022-09-30T23:59:59.999-05:00").json()

cve_list = []

low = 0
medium = 0
high = 0
critical = 0
na = 0

for cve_info in response_info['vulnerabilities']:
    if ("cvssMetricV31" in cve_info["cve"]["metrics"]):
        id = cve_info['cve']['id']
        date = cve_info['cve']['published']
        score = cve_info["cve"]["metrics"]["cvssMetricV31"][0]["cvssData"]["baseScore"]
        level = cve_info["cve"]["metrics"]["cvssMetricV31"][0]["cvssData"]["baseSeverity"]
        if level == "LOW":
            low += 1
        elif level == "MEDIUM":
            medium += 1
        elif level == "HIGH":
            high += 1
        elif level == "CRITICAL":
            critical += 1
        cve_list.append({"id": cve_info['cve']['id'], "date": cve_info['cve']['published'], "score": cve_info["cve"]["metrics"]
                         ["cvssMetricV31"][0]["cvssData"]["baseScore"], "level": cve_info["cve"]["metrics"]["cvssMetricV31"][0]["cvssData"]["baseSeverity"]})
    else:
        id = cve_info['cve']['id']
        date = cve_info['cve']['published']
        cve_list.append(
            {"id": cve_info['cve']['id'], "date": cve_info['cve']['published']})
        na += 1

# Création du graphique avec matplotlib
names = ["Low", "Medium", "High", "Critical", "NA"]
data_group = [low, medium, high, critical, na]
plt.pie(data_group, labels=names, colors=['Gold', 'DarkOrange', 'DarkRed',
        'Black', 'CadetBlue'], wedgeprops={'linewidth': 2, 'edgecolor': 'white'})
my_circle = plt.Circle((0, 0), 0.4, color='white')
p = plt.gcf()
p.gca().add_artist(my_circle)
# plt.show()
plt.savefig('static/donut.png')


# Récupération flux RSS news NVD avec feedparser
NewsFeedNist = feedparser.parse(
    "https://www.nist.gov/news-events/cybersecurity/rss.xml")
tab_entries = []

j = 0
while j != 5:
    entry = NewsFeedNist.entries[j]
    date = entry.published
    title = entry.title
    description = entry.summary
    link = entry.link
    tab_entries.append({"date": date, "title": title,
                       "description": description, "link": link})
    j += 1

# Affichage en HTML
@app.route('/')
def menu():
    return render_template("index.html", lenAlertes=len(cve_list), securities=cve_list, low=low, medium=medium, high=high, critical=critical, na=na, len=len(tab_entries), entries=tab_entries)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5501)
