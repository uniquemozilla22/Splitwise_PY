class Entry:

    def __init__(self, input: str) -> None:
        inputData = input.split("-")
        if len(inputData) != 3:
            raise Exception("Format is not correct.")
        

