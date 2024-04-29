from typing import List
from Entry import Entry
from Users import Users


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
            names.append(Users(name.lower()))
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


def getEntriesClass():
    try:
        entries = input("Enter the entry: ")
        entries = Entry(entries.lower())
        return entries
    except Exception as e:
        print(f"Somthing with the entries went wrong. Please Try Again {e}")
        return getEntriesClass()


def getEntries(entriesCount: int):
    print(
        "Please Enter the entries seperated with hiphens(-)\n For your reference distribution-type: \n C is for Common . User's First word can be used to classify the user distribution.\nFor eg : name_of_purchased_item-distribution_type-Price"
    )
    entries = []
    for entryNumber in range(entriesCount):
        entries.insert(entryNumber, getEntriesClass())
    return entries


def splitBetweenUsers(users: list[Users], entries: list[Entry]):

    for entry in entries:
        if entry.splitBetween == "C":
            entry.setSplitBetween("")
            firstnameForUsers = map(lambda user: user.name[0], users)
            
        for firstName in entry.splitBetween:

            userClass = list(filter(lambda user: user.name[0] == firstName, users))[0]
            singleQuotaPrice = entry.price / len(entry.splitBetween)
            userClass.participates += singleQuotaPrice
            print(f"Added {singleQuotaPrice} for {userClass.name}")

    for user in users:
        print(f"{user.name} has to pay {user.participates}")


def main():
    numberOfUsers = getUserCount()
    users = getUserNames(numberOfUsers)
    entriesCount = getNumberOfEntries()
    entries = getEntries(entriesCount)
    splitBetweenUsers(users, entries)


if __name__ == "__main__":
    main()
