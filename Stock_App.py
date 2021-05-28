from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import pandas as pd
import sys

class Stocks:
    """
    Symbols: The symbol of the share to look up
    Shares: The number of shares already in the account
    Alc: The decimal desired allocation
    """
    def __init__ (self,symbols,shares,alc):
        self.symbols = symbols
        self.shares = shares
        self.alc = alc
        
    def lengthexceps(self):
        if sum(self.alc) != 1:
            raise Exception("Allocation must sum to 1")
        if len(self.symbols) != len(self.shares):
            raise Exception("Must have the same number of shares and symbols")
        if len(self.alc) != len(self.shares):
            raise Exception("Must have the same number of shares and allocations")
        if len(self.alc) != len(self.symbols):
            raise Exception("Must have the same number of symbols and allocations")
    
    def buyer(self,cash,update=True):
        """        
        Parameters
        ----------
        cash : The amount of cash available to buy stocks
        update : True by defaut, when false does not update number of shares
        Returns : A list with the number of shares of each to buy
        -------
        None.

        """
        Stocks.lengthexceps(self)
        
        if cash < 0:
            raise Exception("Cash must be a positive number")
            
        URLS = []
        for i in range(0,len(self.symbols)):
            url = "https://finance.yahoo.com/quote/" + self.symbols[i]
            URLS.append(url)
        
        prices = []
        for i in range(0,len(URLS)): #in python the last element is exclusive
            uClient = uReq(URLS[i])
            html = uClient.read()
            uClient.close()
            stocksoup = BeautifulSoup(html,'html.parser')
            price = stocksoup.find("div",{"class":"My(6px) Pos(r) smartphone_Mt(6px)"})
            price = price.span.text
            price = float(price)
            prices.append(price)
            
        total = []
        for i in range(0,len(prices)):
            totprice = self.shares[i]*prices[i]
            total.append(totprice)
            
        for i in range(0,len(total)):
            total[i] = round(total[i],2)
            
        grandtot = sum(total) + cash
        
        aloc = []
        counter = []
        for i in range(0,len(prices)):
            aloc.append([])
            counter.append([])
            counter[i] = 0
            aloc[i] = total[i] / grandtot
            while aloc[i] < self.alc[i]:
                if cash < prices[i]:
                    break
                else:
                    self.shares[i] = self.shares[i] + 1
                    total[i] = self.shares[i] * prices[i]  
                    cash = cash - prices[i]
                    counter[i] = counter[i] + 1
                    aloc[i] = total[i] / grandtot
        if update == False:
            for i in range(0,len(counter)):
                self.shares[i] = self.shares[i] - counter[i]
                    
        outputdf = pd.DataFrame({"Fund":self.symbols,"New Shares to Buy":counter,"New Total Shares":self.shares})
        print(outputdf)
        return counter
    
    def seller(self,takeoutinput,cash,update=True):
        """
        Parameters
        ----------
        takeoutinput : The ammount of money to be taken out of the account
        cash : The amount of cash already in the account
        update : true by default, when false does not update the number of shares
        Returns A list with the number of shares of each to sell
        -------

        """
        Stocks.lengthexceps(self)
        
        if cash < 0:
            raise Exception("Cash must be a positive number")
            
        URLS = []
        for i in range(0,len(self.symbols)):
            url = "https://finance.yahoo.com/quote/" + self.symbols[i]
            URLS.append(url)
            
        prices = []
        for i in range(0,len(URLS)): #in python the last element is exclusive
            uClient = uReq(URLS[i])
            html = uClient.read()
            uClient.close()
            stocksoup = BeautifulSoup(html,'html.parser')
            price = stocksoup.find("div",{"class":"My(6px) Pos(r) smartphone_Mt(6px)"})
            price = price.span.text
            price = float(price)
            prices.append(price)
 
        takeout = takeoutinput - cash

        total = []
        for i in range(0,len(URLS)):
            totprice = self.shares[i]*prices[i]
            total.append(totprice)
    
        for i in range(0,len(total)):
                total[i] = round(total[i],2)

        fromeach = [i * takeout for i in self.alc]

        counter = [0 for i in range(0,len(total))]
        totalwith = [0 for i in range(0,len(total))]
        for i in range(0,len(total)):
            while (counter[i]*prices[i]) < fromeach[i]:
                if self.shares[i] < 1:
                    break
                self.shares[i] = self.shares[i] - 1
                counter[i] = counter[i] + 1
                totalwith[i] = counter[i] * prices[i]
                total[i] = self.shares[i] * prices[i] 
        totmon = sum(totalwith) + cash 
        
        for i in range(0,len(total)):
            while (totmon - takeoutinput) > prices[i]:
                self.shares[i] = self.shares[i] + 1
                counter[i] = counter[i] - 1
                totalwith[i] = counter[i] * prices[i]
                total = self.shares[i] * prices[i]
                totmon = sum(totalwith) + cash
                if counter[i] < 1:
                    break
                
        if update == False:
            for i in range(0,len(counter)):
                self.shares[i] = self.shares[i] - counter[i]
            
        outputdf = pd.DataFrame({"Fund":self.symbols,"Shares to Sell":counter,"Total Shares Remaining":self.shares})
        print(outputdf)
        return counter
    
    def updateshares(self,newshares):
        """
        Allows the user to manually update the number of shares they own (ie dividends)

        """
        #Stocks.lengthexcepts(self)
        if len(newshares) != len(self.shares):
            raise Exception("New Shares must be the same length as old shares")
        self.shares = newshares
    
    def updatealc(self,newalc):
        """
        Allows the user to manually update their alolcation

        """
        #self.lengthexcepts(self)
        if len(newalc) != len(self.alc):
            raise Exception("New allocation must be the same length as old allocation")
        self.alc = newalc