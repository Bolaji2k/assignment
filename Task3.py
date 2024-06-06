bank = {}

class Bank:
  def __init__(self, bank = bank):
    self.bank = bank

  def create_account(self,account_number,name):
   used = False
   for i in self.bank :
    if account_number==i:
     used=True
   if used==True:
     return "This account number has been taken"
   else:
      self.bank[account_number]= {"account name":name, "balance":0}
      return "Account created"

  def deposit_money(self,account_number,amount):
   check = False
   for i in self.bank:
     if account_number == i:
       check = True
   if check == True:
     self.bank[account_number]["balance"] = amount
     return "Your deposit was successful"
   else:
     return "This account does not exist! please check the account number provided"
   
  def withdraw_money(self,account_number,amount):
    check = False
    for i in self.bank:
     if account_number == i:
      check = True
    if check == True:
      if self.bank[account_number]["balance"] < amount:
        return "Insufficient balance"
      else:
        self.bank[account_number]["balance"] -= amount
        return "withdrawal successful"
    else:
        return "This account does not exist! please check the account number provided"

  def transfer_money(self,sender,receiver,amount):
    check1 = False
    check2 = False
    for i in self.bank:
      if sender == i:
        check1 = True
      if receiver == i:
        check2 = True
    if check1 and check2:
       if sender == receiver :
        return "You provided the same account for sender and receiver"
       elif self.bank[sender]["balance"] < amount:
        return "Insufficient balance"
       else:
        self.bank[sender]["balance"] -= amount
        self.bank[receiver]["balance"] += amount
        return "Transfer successful"
    elif check1 == False and check2:
     return f"Please double check the sender account number provided"
    elif check1 and check2 == False :
     return f"Please double check the receiver account number provided"
    else:
     return f"Please double check the account numbers provided"

  def check_balance(self,account_number):
    balance = self.bank[account_number]["balance"]
    return f"Your account balance is ${balance}"

  def list_all_accounts(self):
    list = []
    for i in self.bank:
      name = self.bank[i]["account name"]
      balance = self.bank[i]["balance"]
      list.append(f"account number:{i}, name:{name}, balance: {balance}")
    return "\n".join(list)

unity=Bank()

print(unity.create_account("2345","JP"))
print(unity.create_account("2346","JP"))
print(unity.create_account("2347","JPM"))
print(unity.create_account("2347","CHI"))
print(unity.deposit_money("2345",1200000))
print(unity.withdraw_money("2346",200000))
print(unity.transfer_money("2345","2346",700000))
print(unity.transfer_money("2345","2347",300000))
print(unity.check_balance("2346"))
print(unity.list_all_accounts())
#print(unity.bank)