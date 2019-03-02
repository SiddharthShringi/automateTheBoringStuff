import requests, webbrowser, sys, bs4

print('Googling.....')

res = requests.get(f'https://www.google.com/search?q={sys.argv[1:]}')
print(type(res))

# making res a beautifulSoup Object
soup = bs4.BeautifulSoup(res.text)

linkElems = soup.select('.r a')


numOpen = min(3, len(linkElems))

for i in range(numOpen):
    print(linkElems[i].get('href'))
    webbrowser.open(f'https://www.google.com/' + linkElems[i].get('href'))

