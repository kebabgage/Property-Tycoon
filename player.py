class Player:

    def __init__(self, name, token):
        self.playerName = name
        self.tokenName = token
        self.bankBalance = 1500

        self.position = 0

        self.propertiesOwned = []
        self.propertiesMortgaged = []

        self.hasWon = False
        self.isBankrupt = False
        self.inJail = False
        self.jail_card = False

        self._passed_go_once = False
        self._double_counter = 0

        self._ai = False
        self.jailTimeCount = 0

    def getPlayerName(self):
        return self.playerName

    def setPlayerName(self, pname):
        self.playerName = pname

    def getTokenName(self):
        return self.tokenName

    def setTokenName(self, tname):
        self.tokenName = tname

    def getBankBalance(self):
        return self.bankBalance

    def setBankBalance(self, balance):
        self.bankBalance = balance

    def addBankBalance(self, amount):
        self.bankBalance += amount

    def removeBankBalance(self, amount):
        self.bankBalance -= amount

    def getPosition(self):
        return self.position

    def setPosition(self, position):
        self.position = position

    def getJailTimeCount(self):
        return self.jailTimeCount

    def setJailTimeCount(self, jailTime):
        self.jailTimeCount = jailTime

    def getHasWon(self):
        return self.hasWon

    def setHasWon(self):
        self.hasWon = True

    def getInJail(self):
        return self.inJail

    #sets a players jail status; true means in jail, false means not in jail
    def setInJail(self, inJail):
        self.inJail = inJail

    #pass true if player received a 'Get Out of Jail Free' card, pass false if the player used it
    def setGetOOJailFreeCard(self, hasCard):
        self.hasGetOOJailFreeCard = hasCard

    #return the array of properties owned
    def getPropertiesOwned(self):
        # Changed this so that we could get the names ofo the properties owned
        return self.propertiesOwned

    def setPropertiesOwned(self):
        return True

    def getPropertiesMortgaged(self):
        return self.propertiesMortgaged

    def setPropertiesMortgaged(self):
        return True

    def has_no_cash(self):
        return self.getBankBalance() < 0

    def add_jail_free_card(self):
        self.jail_card = True


    #add a property to the array of properties owned
    def addPropertyOwned(self, prop):
        self.propertiesOwned.append(prop)

    #should be called in GameManager after initial go-around?
    def passedGoOnce(self):
        self.passedGoOnce = True

    def calculate_assets(self):
        total_assets = 0
        # cash
        total_assets += self.getBankBalance()
        # properties and houses
        for prop in self.getPropertiesOwned():
            total_assets += prop.property_value()

        return int(total_assets)

    #returns true if successful, false if they dont have enough money
    #this is dependent on implementation of the Property class and how that will deal
    #with houses and hotels
    def buyHouseOrHotel(property):
        bankBalance = self.getBankBalance
        price = property.getPrice
        if price > bankBalance:
            return false
        else:
            self.subtractFromBankBalance(price)
            property.addHotel()
            return true
