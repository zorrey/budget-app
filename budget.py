def create_spend_chart(categories):
  print("cat:",categories[0].name)
  list_perce = []
  w_total=0
  myOrder=  "{0:>3}|"
  percent=100
  cat=[]
  dash="    "
  forPrint="Percentage spent by category\n"
  for category in categories: 
    cat.append(category.name)
    w_total+= category.get_withdrawal() 
    dash+="---"
    #print(category.get_withdrawal()) 
  while percent>=0:
    pattern = ""
    for category in categories:        
      if((category.get_withdrawal()/w_total)*100 > percent):
        pattern+=" o "        
      else:
        pattern+="   "
    forPrint+= (myOrder.format(percent) + pattern)+" "+"\n"
    percent-=10
  forPrint+= (dash) +"-"+"\n"
  max_cat=max(enumerate(cat), key=lambda x: len(x[1]))
  #print(len(max_cat[1]))
  #print(cat)
  
  for i in range(len(max_cat[1])):
    cat_print="     "
    for el in cat:       
      if(len(el ) < i+1) : 
        letter = " "
      else:
        letter = el[i]
      
      cat_print+= letter +"  "
    forPrint+=cat_print + "\n"
  forPrint=forPrint[0:-1]
    
  return forPrint
  
class Category:
 
  def __init__(self , name=""):
    self.name = name
    self.ledger = []
  def __str__(self):
    header  = self.name.center(30,"*")
    record = ""
    total = 0
    for el in self.ledger:
      text_length = len(el["description"])
      num_length = len(str("{:.2f}".format(el["amount"])))
      total+=el["amount"]
      if(text_length + num_length > 30):
        limit = 30 - num_length -1
        text = el["description"][0:limit]
      else :
        limit=text_length
        text = el["description"]
      record+= "\n"
      record+= str(text).ljust(limit)
      record+= str("{:.2f}".format(el["amount"])).rjust(30-limit)
    return header + record +"\n"+"Total: " + str(total)
    
  def deposit(self, amount, description=""):
    self.ledger.append({"amount":amount,"description":description})
  def withdraw(self, amount, description=""):
    if self.check_funds(amount):      
      self.ledger.append({"amount":-1*amount,"description":description})
      return True
    else:
      return False
  def get_balance(self)   : 
    total=0
    for el in self.ledger:
      total+= el["amount"]
    return total
  def check_funds(self, amount):
    if(self.get_balance()>=amount):
      return True
    else:
      return False
  def transfer(self, amount, budget_cat) :
    if(self.check_funds(amount)):
      self.withdraw(amount,f"Transfer to {budget_cat.name}")
      budget_cat.deposit(amount, f"Transfer from {self.name}")
      return True
    else:
      return False
  def get_withdrawal(self):
    withdraw_total=0
    for el in self.ledger:
      if(el["amount"]<0):
        withdraw_total+=el["amount"]
    return withdraw_total
      


