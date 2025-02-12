import csv
from pprint import pprint


class Bank:
    def __init__(self):
        self.name = ""
        self.__users = {}  # user detail private
        self.__gen = self.infinite_generator()
  
    def infinite_generator(self):
        i = 1
        while True:
            yield i
            i += 1

    def list_all_users(self):
        pprint(self.__users)

    def add_users(
            self,
            name: str = "",
            phone: str = "xxx",
            balance: int = 2000):
        if not name.isalpha() or len(name) < 1:
            print(name)
            return "Accound Creation Denied!, Please provide a valid name"

        if not phone.isdigit() or len(phone) < 10:
            return "Account Creation Denied! Please provide a valid phone number."

        else:
            unid = next(self.__gen)
            self.__users[unid] = {
                "name": name,
                "phone": phone,
                "balance": balance,
                "transaction": [],
            }
            transactions = self.__users[unid].get("transaction")

            transactions.append(
                {"type": "credit", "amount": 2000, "newBalance": 2000})
        return f"Account Created Sucessfully for {name} with account id : {unid} "

    def deposit_funds(self, unid: int, amount: int = 0):
        rec = self.__users.get(unid)
        if rec is None:
            return "User Not Found"

        if amount <= 0:
            return "Invalid deposit amount"

        if isinstance(unid, int) and isinstance(amount, int):
            rec["balance"] = rec["balance"] + amount
            transactions = self.__users[unid].get("transaction")
            transactions.append(
                {"type": "credit", "amount": amount, "newBalance": rec["balance"]}
            )
            return f" Deposit {amount} Sucessuful, new balance is {rec['balance']} for {rec['name']} , id {unid}"

        return "Deposit Failed"

    def withdraw_funds(self, unid: int, amount: int = 0):
        rec = self.__users.get(unid)
        if rec is None:
            return "User Not Found"
        if amount <= 0:
            return "Invalid withdraw amount"

        if isinstance(unid, int) and isinstance(amount, int):
            if rec["balance"] < amount:
                return f"Insufficient Balance to withdraw {amount} for {rec['name']}, id {unid}"

            rec["balance"] = rec["balance"] - amount
            transactions = self.__users[unid].get("transaction")
            transactions.append(
                {"type": "debit", "amount": amount, "newBalance": rec["balance"]}
            )
            return f" Withdraw {amount} Sucessuful, new balance is {rec['balance']} for account {rec['name']} id {unid} "

        return "Withdraw Failed"

    def acc_stat(self, unid):
        rec = self.__users.get(unid)
        if rec is None:
            return "User Not Found"

        print(f"Here is the record statement of {rec['name']}")
        print(
            " Note: Here's the record statement of last 5 transactions or total transactions which is less"
        )

        last_5_transactions = rec["transaction"][-5:]
        for trans in last_5_transactions:
            print(trans)


b1 = Bank()

# Add few users with unid and deposit of 2000
print(b1.add_users("Vishal", "9390365005"))
print(b1.add_users("Tessa", "1234567890"))
print(b1.add_users("Aakansha", "9987654321"))

print("************* LIST THE RECORDS ******************")
b1.list_all_users()

# deposit funds
print("*************** LIST THE RECORDS (DEPOSIT FUNDS (ID1)) ****************")
print(b1.deposit_funds(unid=1, amount=1000))
print("***list users data")
b1.list_all_users()

# withdraw funds
print("************** LIST THE RECORDS (WITHDRAW FUNDS (ID1)) *****************")
print(b1.withdraw_funds(unid=1, amount=500))
print("***list users data")
b1.list_all_users()

print("************* LIST THE RECORDS (DEPOSIT FUNDS (ID3)) ******************")
print(b1.withdraw_funds(unid=3, amount=1500))
print("***list users data")
b1.list_all_users()


print("************** LIST THE RECORDS (DEPOSIT FUNDS (ID3)) *****************")
print(b1.withdraw_funds(unid=3, amount=2500))
# print(f"***list users data")
# b1.list_all_users()


print("*********** ACCOUNT STATEMENT (DEPOSIT FUNDS (ID3)) ********************")
b1.acc_stat(unid=3)
# print(f"***list users data")
# b1.list_all_users()
