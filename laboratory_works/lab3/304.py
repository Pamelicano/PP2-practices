class StringHandler:
    def getString(self):
        self.s = input()
    
    def printString(self):
        print(self.s.upper())

str_handler = StringHandler()
str_handler.getString() 
str_handler.printString()   

