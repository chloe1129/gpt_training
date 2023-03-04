import re
from pprint import pprint


file1 = open('Hiccup_Unparsed_Training_Data.txt', 'r')
data = file1.read().splitlines()
file1.close()

data = '\n'.join(data)
print(data)
