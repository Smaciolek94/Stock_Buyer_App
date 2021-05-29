# Stock Allocation App:
## Introduction:  
When holding a diversified portfolio of stocks, bonds, and funds, one usually wishes to maintain a certain asset allocation. With the prices constantly changing,
it can become very difficult to figure out how many shares of each to buy when one wishes to add money to the account, or sell when one wishes to withdraw money,
while maintaining their desired allocation. This project is a continuation of an idea I had several years ago - it takes user input stock ticker symbols, desired allocation,
shares already held, scrapes the web for current stock prices, and 
calculates how many shares of each they should buy or sell when depositing or withdrawaing funds.  The project is designed to be modular, with the Stock_App
program containing a Stocks class with attirbutes and methods that are used to do the calcuations behind the scenes. It can be imported into other programs, or used with 
the App.py command line like program designed to walk a programming-naive user through the process. 
## Stock App.py
This program can be used  as a standalone module or in conjunction with the other programs for ease of use. It creates a class called **Stocks** that has the following atributes:<ul>  
<li> Symbols: A list of string stock ticker symbols
<li> Shares: A list of shares already held in the account
<li> Allocation: A list of decimal proportions corresponding to the desired allocation of each security. It must sum to 1!
</ul>

All attributes must be lists of the same length!    
It has the following methods:  <ul>
<li> buyer(cash,update): The user inputs the amount of cash they wish to deposit into the account, and this function returns the number of shares of each to buy, as well as prints
some useful information. By default, it automatically updates the number of shares unless update = False  
<li> seller(takeout,cash,update): The user inputs the amount of money they with to withdrawl, the amount of cash already in the account, and this function returns the number of 
shares of each to sell, as well as prints some useful information. By default, it automatically updates the number of shares unless update=False 
<li> updateshares(shares): changes the shares attribute to a new user inputted list of shares - The length of the new shares list must be the same as the old!   
<li> updatealc(allocation): changes the allocation attribute to a user user inputted list of allocations - The length of the new allocation list must be the same as the old, 
and it must sum to 1!
</ul>

## ImpExp.py:
The program is intended to be used with the command line application and defines input and output functions: <ul>
<li> importer(path, which): This function imports a csv at path. Which must be set to either "symbol", "alc", or "shares" to return the corresponding attribute. In the Application,
it is called once for each, with a csv file containing each list as a column with headers "symbol", "alc" and "shares"
<li> exporter(path,symbol,allocation,shares): This function exports all of the information once it has been updated to a csv at path
</ul>

## App.py:
This program asks the user for the file location of their input csv, then walks them through checking if the number of shares and desired allocation is correct, asks if they wish 
to buy or sell, and then updates the input csv with the new information
