class string:
    def __init__(self, str):
        self.str = str
        
    def getString(self):
        self.str = input()
        
    def printString(self):
        print(self.str.upper())
        
x = string("Togzhan")
x.getString()
x.printString()