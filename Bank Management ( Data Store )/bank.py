import csv
import json
from pprint import pprint


class Bank:
    def __init__(self):
        self.__f_name = "bank.csv"
        self.__gen = self.infinite_generator()
        
        with open(self.__f_name, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(
                ["Accound id", " Name", " Phone", " Balance", " Transactions"]
            )
            
    def infinite_generator(self):
        i = 1
        while True:
            yield i
            i += 1

    def list_all_users(self):
        with open(self.__f_name, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)

    def add_users(self, name: str = "", phone: str = "xxx", balance: int = 2000):
        if not name.isalpha() or len(name) < 1:
            print(name)
            return "Accound Creation Denied!, Please provide a valid name"

        if not phone.isdigit() or len(phone) < 10:
            return "Account Creation Denied! Please provide a valid phone number."

        else:
            unid = next(self.__gen)
            transactions = [{"type": "credit", "amount": 2000, "newBalance": 2000}]

            with open(self.__f_name, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([unid, name, phone, balance, transactions])

        return f"Account Created Sucessfully for {name} with account id : {unid} "

    def deposit_funds(self, unid: int, amount: int = 0):
        rec = []
        user_found = False

        with open(self.__f_name, "r") as file:
            reader = csv.reader(file)
            header = next(reader)
            rec.append(header)

            for row in reader:
                if unid == int(row[0]):
                    user_found = True

                    if amount <= 0:
                        return "Invalid deposit amount"

                    if isinstance(unid, int) and isinstance(amount, int):
                        balance = int(row[3])
                        transactions = json.loads(row[4].replace("'", '"'))
                        print(transactions)
                        balance += amount
                        transactions.append(
                            {"type": "credit", "amount": amount, "newBalance": balance}
                        )

                        row[3] = str(balance)
                        row[4] = json.dumps(transactions)

                rec.append(row)

            if not user_found:
                return "User not Found!"

            with open(self.__f_name, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(rec)
                return f" Deposit {amount} Sucessuful, new balance is {balance} for {row[1]} , id {unid}"

    def withdraw_funds(self, unid: int, amount: int = 0):
        rec = []
        user_found = False

        with open(self.__f_name, "r") as file:
            reader = csv.reader(file)
            header = next(reader)
            rec.append(header)

            for row in reader:
                if unid == int(row[0]):
                    user_found = True

                    if amount <= 0:
                        return "Invalid withdrawal amount"

                    balance = int(row[3])
                    transactions = json.loads(row[4].replace("'", '"'))

                    if amount > balance:
                        return "Insufficient funds"

                    balance -= amount
                    transactions.append(
                        {"type": "debit", "amount": amount, "newBalance": balance}
                    )

                    row[3] = str(balance)
                    row[4] = json.dumps(transactions)

                rec.append(row)

        if not user_found:
            return "User not Found!"

        with open(self.__f_name, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rec)

        return f"Withdrawal {amount} Successful, new balance is {balance} for {row[1]}, id {unid}"

    def acc_stat(self, unid: int):
        user_found = False

        with open(self.__f_name, "r") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                if unid == int(row[0]):
                    user_found = True
                    print(f"Here is the record statement of {row[1]}")
                    print(
                        " Note: Here's the record statement of last 5 transactions or total transactions which is less"
                    )

                    transactions = json.loads(
                        row[4].replace("'", '"')
                    )  # convert into lists
                    last_5_transactions = transactions[-5:]
                    for trans in last_5_transactions:
                        pprint(trans)

        if not user_found:
            print("User not Found!")


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
print("***list users data")
b1.list_all_users()


print("*********** ACCOUNT STATEMENT (DEPOSIT FUNDS (ID3)) ********************")
b1.acc_stat(unid=3)
print("***list users data")
b1.list_all_users()
