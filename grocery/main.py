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

for i in file_lines:
    print(i)