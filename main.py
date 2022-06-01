from helpers import logUsage, getTextFromFile, saveTextToFile
from summarizer import summarize
import sys


args = sys.argv

if len(args) >= 2:
    input_file = args[1]
    text = getTextFromFile(input_file)
    summary = summarize(text, 0.5)

    if(len(args) > 2):
        output_file = args[2]
        saveTextToFile(summary, output_file)
    else:
        print(summary)

else:
    logUsage()
    exit(1)
