import urllib
import re

symbolfile = open("symbol.txt")
symbolslist = symbolfile.read()

newsymbolslist = symbolslist.split("\n") # somehow include a space at the end

i = 0
while i < len(newsymbolslist) - 1:
    url = "http://finance.yahoo.com/q?s=" + newsymbolslist[i] + "&ql=1"
    htmlfile = urllib.urlopen(url)
    htmltext = htmlfile.read()

    regex = "<span id=\"yfs_l84_[^.]*\">(.+?)</span>"
    pattern = re.compile(regex)

    price = re.findall(pattern,htmltext)
    print "the price of", newsymbolslist[i], " is ",  price 
    i += 1
