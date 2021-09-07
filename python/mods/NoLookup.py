import wikipedia

class lookupbot:
    lang = 'en-us'
    @classmethod
    def setLang(pfx : str):
        if pfix in wikipedia.languages():
            wikipedia.set_lang(pfx)
            cls.lang = pfx
        
    @classmethod
    def lookupTitles(query : str, resnum : int = -1):
        if max == -1:
            return wikipedia.search(query)
        else:
            return wikipedia.search(query, results=resnum)

    @classmethod
    def suggestTitles(query : str):
        sq = wikipedia.suggest(query)
        return sq
    @classmethod
    def getSummary(query : str, disambiguation : int = -1):
        try:
            gq = wikipedia.summary(query)
        except wikipedia.exceptions.DisambiguationError as excep:
            if disambiguation != -1:
                gq = lookupbot.getSummary(excep.options[disambiguation], disambiguation=disambiguation)
        except wikipedia.exceptions.PageError:
            print("No pages match the suggested name. Terminating...")
        return gq
    @classmethod
    def getPage(query : str, disambiguation : int = -1):
        try:
            gq = wikipedia.page(query)
        except wikipedia.exceptions.DisambiguationError as excep:
            if disambiguation != -1:
                gq = lookupbot.getPage(excep.options[disambiguation], disambiguation=disambiguation)
        except wikipedia.exceptions.PageError:
            print("No pages match the suggested name. Terminating...")
        return gq

def start():
    lookupbot.setLang('en-us')
    print(lookupbot.suggestTitles('Peru'))