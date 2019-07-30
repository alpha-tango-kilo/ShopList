import getopt
from sys import exit as SYSEXIT

class EasyFlag:
    def __init__(self, short, action, long = None, needsArg = False):
        self.short = short # single letter call e.g. h
        self.long = long # string calls e.g. help
        self.needsArg = needsArg # if flag needs arg e.g. --inputfile ./foo.txt
        self.action = action # function to call if flag is present and used correctly

class EasyArgHandler:
    def __init__(self, flags):
        self.getoptShort = ""
        self.getoptLong = []
        self.flagTuples = []
        self.flagDict = {}
        for flag in flags:
            self.getoptShort += flag.short
            self.flagDict[("-" + flag.short)] = flag.action
            if flag.needsArg:
                self.getoptShort += ":"
            if flag.long:
                tempStr = "-" + flag.long
                if flag.needsArg:
                    tempStr += "="
                self.getoptLong.append(tempStr)
                self.flagDict["--" + flag.long] = flag.action
    
    def handleArgs(self, args):
        try:
            optList, args = getopt.getopt(args, self.getoptShort, self.getoptLong)
        except getopt.GetoptError:
            if "--help" in self.flagDict.keys():
                print("Invalid args, use --help for help")
            else:
                print("Invalid args")
            SYSEXIT(2)

        # noinspection PyUnboundLocalVariable
        for opt, arg in optList:
            if arg == "":
                self.flagDict[opt]() # shouldn't need error checking as getopt.GetoptError would've caught it
            else:
                self.flagDict[opt](arg)
            