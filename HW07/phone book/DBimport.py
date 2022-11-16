

def importPhoneBook():
    importlist = []
    with open("export.txt", "r") as file:
        for i in file:
            importlist.append(i)
            importstr = str(importlist)
            importstr.remove('Фамилия - ')

    return importstr

importlist = importPhoneBook()
print(importlist)

