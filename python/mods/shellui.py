class shellui:
    @staticmethod
    def createMargin(txt):
        return "\n" + "+" + "-" * len(txt) + "+" + "\n" + "|" + txt + "|" + "\n" + "+" + "-" * len(txt) + "+"


