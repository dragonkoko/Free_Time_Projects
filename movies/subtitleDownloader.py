import urllib
import urllib2
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
values = {'name': 'Anonymous',
          'location': 'Anonymous',
          'language': 'Anonymous'}
headers = {'User-Agent': user_agent}

def getSubtitles(name):
    try:
        movieName = name.replace("\n", "").lower().replace(" ", "-")
        languages = ["english", "german"]
        print movieName
        for language in languages:
            url = 'https://isubtitles.net/'+movieName+'/'+language+'-subtitles'
            downloadCheck = "/download/"+movieName+"/"+language
            data = urllib.urlencode(values)
            req = urllib2.Request(url, data, headers)
            response = urllib2.urlopen(req)
            page = response.read()
            soup = BeautifulSoup(page)
            for a in soup.find_all('a', href=True):
                if downloadCheck in a['href']:
                    if language == "english":
                        urllib.urlretrieve("https://isubtitles.net" + a['href'], "/"+movieName+".zip")
                    if language == "german":
                        urllib.urlretrieve("https://isubtitles.net" + a['href'], "/"+movieName+".zip")
                    print a['href']
                    break
    except:
        print "Exception" + str(name)
        return
def main():
    for line in open("listOfMovies.txt", 'r+').readlines():
        if "(" not in line:
            getSubtitles(line)

if __name__ == "__main__":
    main()
