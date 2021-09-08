import wikipedia
import re

def setLang(pfx : str):
    if pfx in wikipedia.languages():
        wikipedia.set_lang(pfx)
    
def lookupTitles(query : str, resnum : int = -1):
    if resnum == -1:
        return wikipedia.search(query)
    else:
        return wikipedia.search(query, results=resnum)

def suggestTitles(query : str):
    sq = wikipedia.suggest(query)
    return sq

def getSummary(query : str, disambiguation : int = -1):
    try:
        return wikipedia.summary(query)
    except wikipedia.exceptions.DisambiguationError as excep:
        if disambiguation != -1:
            return getSummary(excep.options[disambiguation], disambiguation=disambiguation)
    except wikipedia.exceptions.PageError:
        print("No pages match the suggested name. Terminating...")

def getPage(query : str, disambiguation : int = -1):
    try:
        return wikipedia.page(query)
    except wikipedia.exceptions.DisambiguationError as excep:
        if disambiguation != -1:
            return getPage(excep.options[disambiguation], disambiguation=disambiguation)
    except wikipedia.exceptions.PageError:
        print("No pages match the suggested name. Terminating...")

def splitPage(pg : wikipedia.WikipediaPage):
    fmt = '====|===|=='
    match = re.split(fmt, pg.content)
    match.insert(0, 'Summary')
    nm = {}
    for x in range(0, len(match), 2):
        nm[match[x]] = match[x+1]
    return nm
      

def start():
    q = 'Donald Trump'
    setLang('en-us')
    #print(lookupTitles(q))
    #print(getSummary(q, 0))
    pg = getPage(q, 0)
    splitPage(pg)