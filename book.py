class Book:
    __id = ""
    __name = ""
    __author = ""
    __price = ""

    def __init__(self, id, name, author, price):
        self.__id = id
        self.__name = name
        self.__author = author
        self.__price = price

    def setId(self, newid):
        self.__id = newid

    def getId(self):
        return self.__id

# //////////////-----------------///////////////////-------------------////////////////////----------------////////////////////////

    def setName(self, newName):
        self.__name = newName

    def getName(self):
        return self.__name

# //////////////-----------------///////////////////-------------------////////////////////----------------////////////////////////

    def setAuthor(self, newAuthor):
        self.__author = newAuthor

    def getAuthor(self):
        return self.__author

# //////////////-----------------///////////////////-------------------////////////////////----------------////////////////////////

    def setPrice(self, newPrice):
        self.__price = newPrice

    def getPrice(self):
        return self.__price
