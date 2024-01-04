

itemAvailableDict ={}
shoppingDict={}
# shoppingDict={"eggs":{"quantity":2,"subtotal":itemAvailableDict["egg"]*2}}
#welcome User

userName=input("Please enter your name: ")
welcomeMessage=f"Welcome to my store {userName}"
lenWCMsg=len(welcomeMessage)
print("*"*lenWCMsg)
print(welcomeMessage)
print("*"*lenWCMsg)

#read data from text file 
my_file=open("/home/sahilnayak/Desktop/works/PythonProjects/grocery/AvailableProduct.txt ")
file_line=my_file.readline()
itemsAvailable=my_file.readlines()
# print(itemsAvailable)
my_file.close()

#fetch items from list and add to a dictionary
print("***********Items Available in Our Store****************")
for item in itemsAvailable:
   item_name=item.split()[0]
   item_price=item.split()[1]
   print(f"{item_name}: {item_price}")
   itemAvailableDict.update({item_name: float(item_price)})
print("*"*20)
print(itemAvailableDict)
#prompt user to add items
proceedShopping=input("Do you wish to proceed (yes/no): ")
while proceedShopping.lower()=="yes":
  item_added=input("Add an item: ")
  if item_added.title() in itemAvailableDict:
    item_qty=int(input("Add quantity: "))
    shoppingDict.update({item_added:{"quantity":item_qty,"subtotal":itemAvailableDict[item_added.title()]*item_qty}})
    print(shoppingDict)
  else:
    print("unable to add unavailable item")
  proceedShopping=input("Do you wish to add more items (yes/no): ")
else:
  print("\n")
  print("****Bill Summary***** ")
  print("\n")
  print("Item    Quantity    SubTotal")
  total=0
  for key in shoppingDict:
    print(f"{key}    {shoppingDict[key]['quantity']}        {shoppingDict[key]['subtotal']}")
    total=shoppingDict[key]['subtotal']+total
    print(f"Total: {total}")
  print("***********Thank You********")
  print("Hope to see you back soon!")
