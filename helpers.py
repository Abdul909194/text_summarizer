def getTextFromFile(filepath):
    with open(filepath) as file:
        return file.readlines()


def saveTextToFile(text, filepath):
    with open(filepath, 'w') as file:
        file.write(text)
