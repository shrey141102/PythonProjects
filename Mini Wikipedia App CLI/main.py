import wikipedia as wiki

page_title = input("ENTER THE TOPIC YOU WANNA SEARCH: ")
p = wiki.page(page_title)
print("-------------------------------------------------------------------------------------------------------------------------------")
print(p.title)
print ()
print("-------------------------------------------------------------------------------------------------------------------------------")
print(p.url)
print ()
print("-------------------------------------------------------------------------------------------------------------------------------")
print(p.content)
print ()
print("-------------------------------------------------------------------------------------------------------------------------------")

