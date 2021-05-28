import pandas as pd

path = "C:\\Users\\smaci\\Documents\\GitHub\\Stock_Buyer_App\\shares.csv"

def importer(path):
    return list(round(pd.read_csv(path)["Shares"],2))
    
def exporter(path,Shares):
 #   Old_Shares = list(pd.read_csv(path)["Shares"])
    out = pd.DataFrame({"Shares":Shares,"Old_Shares":list(pd.read_csv(path)["Shares"])})
    out.to_csv(path)

Shares = importer(path)
test = exporter(path,Shares)