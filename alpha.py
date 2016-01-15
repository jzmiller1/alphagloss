import re
from datetime import datetime
import pyperclip


def timestamp():
    """Generates a simple timestamp for text file naming."""
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


raw_glossary = pyperclip.paste()

# Find the glossary entries
glossary_items = {}
data = re.findall(r'\\(.*?),\n}\n\n',
                  raw_glossary,
                  re.MULTILINE|re.DOTALL)

entries = [(re.findall(r'{(.*?)}', entry)[0], "\\" + entry + ",\n}\n\n")
           for entry in data]

# Sort the entries and build a new glossary
entries.sort()
new_glossary = "".join([entry[1] for entry in entries])

# Write a textfile backup of the new glossary
f = open("glossary_{}.txt".format(timestamp()), 'w')
f.write(new_glossary)
f.close()

# Send the new glossary to the clipboard
pyperclip.copy(new_glossary)

