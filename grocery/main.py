AvailableProductDict = {}

#welcome message for the customer
CustomerName = input("Enter your name: ")
WelcomeMessage = f"welcome to our store {CustomerName}"
LenMsg = len(WelcomeMessage)
print("*"*LenMsg)
print(WelcomeMessage)
print("*"*LenMsg)

#reading data from text file

Product_file = open("/home/sahilnayak/Desktop/works/PythonProjects/grocery/AvailableProduct.txt ")
file_lines = Product_file.readlines()
# print(file_lines)

Product_file.close()

#iterate one by one all products present in the text file
print("*************** items present in the store ******************")

for i in file_lines:
    item_name = i.split()[0]
    item_price = i.split()[1]
    print(f"{item_name} : {item_price}")
    AvailableProductDict.update({item_name : item_price})

# print(AvailableProductDict)
    

print("*************** items present in the store ******************")


#getting permission from the user whether they want to proceed or not

ProceedMsg = input("Do you want to proceed? (Y/N)")

if ProceedMsg.lower() == "yes":
    itemEntered = input("Enter the item that you want to add to your cart: ")
    if itemEntered.title() in AvailableProductDict:

else:
    print("Please come back again!!!")
