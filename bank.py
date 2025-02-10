from pprint import pprint

class Bank: 
    def __init__(self):
        self.name = ""
        self.users = {}
        self.ungen = 0
        
    def listAllUsers(self):
        pprint(self.users)

    def addUsers(self,name: str ="",phone :str ="xxx",balance:int = 2000):
        if not name.isalpha() or len(name)<1:
            print(name)
            return "Accound Creation Denied!, Please provide a valid name"
        else:
            self.ungen += 1
            unid =  self.ungen
            self.users[unid] = ({"name": name, "phone": phone, "balance" : balance, "transaction": []})
            transactions = self.users[unid].get("transaction")
            transactions.append({"type":"credit","amount":2000,"newBalance" : 2000})
        return f"Account Created Sucessfully for {name} with account id : {unid} "
    
    def depositFunds(self,unid:int, amount:int = 0):
        rec = self.users.get(unid)
        if rec is None:
            return ("User Not Found")
        if isinstance(unid, int) and isinstance(amount,int):
            rec["balance"] = rec["balance"]+amount
            transactions = self.users[unid].get("transaction")
            transactions.append({"type":"credit","amount":amount,"newBalance" : rec["balance"]})
            return (f" Deposit {amount} Sucessuful, new balance is {rec['balance']} for {rec['name']} , id { unid }")
            
        return "Deposit Failed"
    
    def withdrwaFunds(self,unid:int, amount:int = 0):
        rec = self.users.get(unid)
        if rec is None:
            return ("User Not Found")
        if isinstance(unid, int) and isinstance(amount,int):
            if rec["balance"]<amount:
                return f"Insufficient Balance to withdraw {amount} for {rec['name']}, id {unid}"
            rec["balance"] = rec["balance"]-amount
            transactions = self.users[unid].get("transaction")
            transactions.append({"type":"debit","amount":amount,"newBalance" : rec["balance"]})
            return (f" Withdraw {amount} Sucessuful, new balance is {rec['balance']} for account {rec['name']} id {unid} ")
            
        return "Withdraw Failed"
    
    def accStat(self,unid):
        rec = self.users.get(unid)
        if rec is None:
            return ("User Not Found")
        
        print(f"Here is the record statement of {rec['name']}")
        print(" Note: Here's the record statement of last 5 transactions or total transactions which is less")
        
        last_5_transactions = rec["transaction"][-5:]
        for trans in last_5_transactions:
            print(trans)
        
        
b1 = Bank()

# Add few users with unid and deposit of 2000
print(b1.addUsers("Vishal","9390365005"))
print(b1.addUsers("Tessa","123456789"))
print(b1.addUsers("Aakansha","9987654321"))

print("************* LIST THE RECORDS ******************")
b1.listAllUsers()

# deposit funds 
print("*************** LIST THE RECORDS (DEPOSIT FUNDS (ID1)) ****************")
print (b1.depositFunds(unid=1,amount = 1000))
print(f"***list users data")
b1.listAllUsers()

# withdraw funds 
print("************** LIST THE RECORDS (WITHDRAW FUNDS (ID1)) *****************")
print (b1.withdrwaFunds(unid=1,amount = 500))
print(f"***list users data")
b1.listAllUsers()

print("************* LIST THE RECORDS (DEPOSIT FUNDS (ID3)) ******************")
print (b1.withdrwaFunds(unid=3,amount = 1500))
print(f"***list users data")
b1.listAllUsers()


print("************** LIST THE RECORDS (DEPOSIT FUNDS (ID3)) *****************")
print (b1.withdrwaFunds(unid=3,amount = 2500))
# print(f"***list users data")
# b1.listAllUsers()


print("*********** ACCOUNT STATEMENT (DEPOSIT FUNDS (ID3)) ********************")
b1.accStat(unid=3)
# print(f"***list users data")
# b1.listAllUsers()

