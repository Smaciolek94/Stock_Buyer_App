import pandas as pd

#path = "C:\\Users\\smaci\\Documents\\GitHub\\Stock_Buyer_App\\shares.csv"

#path = "input_taxable.csv"

def importer(path, which):
    if which == "symbol":
        symbol = list(pd.read_csv(path)["symbol"])
        return symbol
    if which == "alc":
        allocation = list(pd.read_csv(path)["allocation"])
        return allocation
    if which == "shares":
        shares = round(pd.read_csv(path)["shares"])
        return shares
#symbol = importer(path,"symbol")
#alc = importer(path,"alc")
#shares = importer(path,"shares")
    
def exporter(path,symbol,allocation,shares):
 #   Old_Shares = list(pd.read_csv(path)["Shares"])
    out = pd.DataFrame({"symbol":symbol,"allocation":allocation,"shares":shares})
    out.to_csv(path)

#exporter(path,symbol,allocation,shares)