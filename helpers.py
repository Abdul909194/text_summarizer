def getTextFromFile(filepath):
    with open(filepath) as file:
        return file.readlines()


def saveTextToFile(text, filepath):
    with open(filepath, 'w') as file:
        file.write(text)


def logUsage():
    print('Usage: python3 main.py input-file [output-file]')
