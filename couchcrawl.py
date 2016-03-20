import urllib2
import os
import webbrowser

ver = "Couchtuner v0.1"

#Ranierland.biz web searcher / crawler
#-XF


def clearScreen():#clear screen and add header
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

    print ver
    print "------------------------------"

def searchEpisode(url):
    clearScreen()

    #connect
    req = urllib2.Request(url,headers=hdr)
    page = urllib2.urlopen(req)
    content = page.read()

    #variables
    countEpisode = content.count('<li><strong>')
    n = 0
    linkStart = 0
    tStart = 0
    linkEpisodes = [] #list of episodes


    while n != countEpisode:

        #find start and end of link
        linkStart = 21 + content.find('<li><strong>',linkStart)
        linkEnd = -2 + content.find('>',linkStart)

        #find start and end of title
        tStart = 3 + linkEnd
        tEnd = -2 + content.find('a>',tStart)

        linkEpisodes.append(content[linkStart:linkEnd]) #append link

        print countEpisode - n, " -  " + content[tStart:tEnd]

        linkStart = tEnd #append next search
        n = n + 1

    print "0 - Home"

    r1 = input("Enter: ")

    if r1 == 0:
        home()
    else:
        webbrowser.open(linkEpisodes[countEpisode - n])
        #run program here

def searchSeries(url): #send search request then list all links
    clearScreen()

    #send request and connect
    req = urllib2.Request('http://www.couchtuner.ag/?s=' + url, headers=hdr)
    page = urllib2.urlopen(req)
    content = page.read()

    #grab series names and links
    #only one series for now
    linkSeries = []
    linkStart = 6 + content.find('href=',content.find('Search Results :')) #get first link after actual results
    linkEnd = -2 +content.find('rel=',linkStart)
    linkSeries.append(content[linkStart:linkEnd])

    titleStart = 1 + content.find('>',linkEnd)
    titleEnd = -2 + content.find('a>',titleStart)
    print "1 - " + content[titleStart:titleEnd]
    print ""
    print "0 - Home"

    #fix this part, use while
    r1 = input("Enter: ")

    if r1 == 1:
        searchEpisode(linkSeries[0])
    elif r1 == 0:
        home()


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
        searchSeries(r2.replace(" ","+"))

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

#user-agent
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}



home() #start
