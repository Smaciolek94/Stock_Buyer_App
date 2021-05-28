from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import pandas as pd
import sys
import Stock_App as sa

symbols = ["SCHB","SCHZ"]
shares = [2,1]
alc = [.5,.5]

p = sa.Stocks(symbols,shares,alc)
p.buyer(500)
p.shares
p.seller(500,20)