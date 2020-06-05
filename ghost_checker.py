'''
 This will most likely blow your pc up, so use your brain, read the code and think of what can happen.
'''

import requests

f = open('hit.txt').read().split('\n')

def save_content(file, content):
    with open(file, 'a+') as f:
         f.write(content)

for link in f:
   r = requests.get(link + '/raw')
   save_content(link.split('/')[4], r.text)
print("Finished.")
