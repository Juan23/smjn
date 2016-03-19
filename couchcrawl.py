import urllib2
import os

#Ranierland.biz web searcher / crawler
#-XF

#clear screen and add header
def clearScreen(): #clears the screen
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

    print "Couchtuner Crawler v0.1"
    print "------------------------------"

def search(url):
    req = urllib2.Request('http://www.couchtuner.ag/?s=' + url, headers=hdr)

    try:
        page = urllib2.urlopen(req)
    except urllib2.HTTPError, e:
        print e.fp.read()
    
    content = page.read()
    print "Done"
    #html = response.read()

#main
def home():
    clearScreen()
    print "1 - Search Couchtuner"
    print "2 - About"
    r1 = input("Enter: ")

    if r1 == 1:
        clearScreen()
        print "What do you want to watch"
        r2 = raw_input("Search: ")
        search(r2.replace(" ","+"))

    elif r1 == 2:
        clearScreen()
        print ""
        print "Written by: Xing Fu"
        print ""
        home()
         #open pen.io webpage here for aboutme

    else:
        clearScreen()
        print ""
        print "Invalid command."
        print ""
        home()
        print "Invalid. Please try again."

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
home()
