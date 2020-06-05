'''
 This will most likely blow your pc up, so use your brain, read the code and think of what can happen.
'''

import requests

file_name = input("File name of the ghostbin.co valid brutes: ")
f = open(file_name).read().split('\n')

def save_content(file, content):
    with open(file, 'a+', encoding='utf-8') as f:
         f.write(content)

for link in f:
   r = requests.get(link + '/raw')
   save_content(link.split('/')[4], r.text)
f.close()
print("Finished.")
