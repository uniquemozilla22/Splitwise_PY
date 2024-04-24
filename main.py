from Entry import Entry


def getUserCount():
    try:
        users = input("How many users are there? ")
        users = int(users)
        return users
    except:
        print("An error has occured. Please Try Again")
        return getUserCount()


def getUserNames(numberOfUsers: int):
    try:
        names = []
        for user in range(numberOfUsers):
            name = input(f"Name of the user {user+1}: ")
            names.append(name)
            print(name, "added to the list")
        return names
    except:
        print("An Error Has occured.")
        return getUserNames(numberOfUsers)


def getNumberOfEntries():
    try:
        entriesCount = input("How many entries are there? ")
        entriesCountInt = int(entriesCount)
        return entriesCountInt
    except:
        print("An error has occured. Please Try Again")
        return getNumberOfEntries()


def setEntriesToClass(entryInput:str):
    
def getEntries(entriesCount: int):
    print(
        "Please Enter the entries seperated with hiphens(-)\n For your reference distribution-type: \n C is for Common . User's First word can be used to classify the user distribution.\nFor eg : name_of_purchased_item-distribution_type-Price"
    )
    entries = {}
    for entryNumber in range(entriesCount):
        entries = input("Enter the entry.")
        entries = Entry(entries)


def main():
    numberOfUsers = getUserCount()
    users = getUserNames(numberOfUsers)
    entriesCount = getNumberOfEntries()


if __name__ == "__main__":
    main()
