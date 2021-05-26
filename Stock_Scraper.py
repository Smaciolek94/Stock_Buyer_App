#! /usr/bin/env python3

from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import pandas as pd
import sys
print(sys.argv)

symbols = ["SCHB","SCHZ"]
shares = [2,1]
cash = 500
alc = [.5,.5]

class Stocks:
    def __init__ (self,symbols,shares,cash,alc):
        self.symbols = symbols
        self.shares = shares
        self.cash = cash
        self.alc = alc
        
    def buyer(self):
        if sum(self.alc) != 1:
            raise Exception("Allocation must sum to 1")
        if self.cash <= 0:
                raise Exception("Cash must be a positive number")
        if len(self.symbols) != len(self.shares):
            raise Exception("Must have the same number of shares and symbols")
        if len(self.alc) != len(self.shares):
            raise Exception("Must have the same number of shares and allocations")
        if len(self.alc) != len(self.symbols):
            raise Exception("Must have the same number of symbols and allocations")
    
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
                    self.cash = self.cash - prices[i]
                    counter[i] = counter[i] + 1
                    aloc[i] = total[i] / grandtot
                    
        return counter

#print(Stocks.buyer(symbols, shares, cash, alc))
t = Stocks(symbols, shares, cash, alc)
print(t.buyer())