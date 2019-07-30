import getopt
from sys import exit as SYSEXIT

class EasyFlag:
    def __init__(self, short, action, *, long = None, needsArg = False, isHelpCommand = False):
        self.short = short # single letter call e.g. h
        self.long = long # string calls e.g. help
        self.needsArg = needsArg # if flag needs arg e.g. --inputfile ./foo.txt
        self.isHelpCommand = isHelpCommand
        self.action = action # function to call if flag is present and used correctly

class EasyArgHandler:
    def __init__(self, flags):
        self.getoptShort = ""
        self.getoptLong = []
        self.flagTuples = []
        self.flagDict = {}
        self.helpFlag = None
        for flag in flags:
            self.getoptShort += flag.short
            self.flagDict[f"-{flag.short}"] = flag.action
            if flag.needsArg:
                self.getoptShort += ":"
            if flag.long:
                tempStr = f"--{flag.long}"
                self.flagDict[tempStr] = flag.action
                if flag.needsArg:
                    tempStr += "="
                self.getoptLong.append(tempStr)
            if flag.isHelpCommand:
                self.helpFlag = flag
    
    def handleArgs(self, args):
        try:
            optList, args = getopt.getopt(args, self.getoptShort, self.getoptLong)
        except getopt.GetoptError:
            if self.helpFlag:
                print(f"Invalid args, use -{self.helpFlag.short} or --{self.helpFlag.long} for help")
            else:
                print("Invalid args")
            SYSEXIT(2)

        # noinspection PyUnboundLocalVariable
        for opt, arg in optList:
            if arg == "":
                self.flagDict[opt]() # shouldn't need error checking as getopt.GetoptError would've caught it
            else:
                self.flagDict[opt](arg)
            