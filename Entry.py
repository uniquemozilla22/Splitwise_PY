class Entry:

    def __init__(self, input: str) -> None:
        inputData = input.split("-")
        if len(inputData) != 3:
            raise Exception("Format is not correct.")
        nameOfProduct, distributionClassification, price = inputData
        self.setName(nameOfProduct)
        self.setSplitBetween(distributionClassification)
        self.setPrice(price)

    def setName(self, name):
        self.name = name

    def setSplitBetween(self, splitBetween):
        self.splitBetween = splitBetween

    def setPrice(self, price):
        try:
            self.price = float(price)
        except TypeError:
            print("Price type is not in correct format. please enter again. Setting the ")
            self.price = 0.00
