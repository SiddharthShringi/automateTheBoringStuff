import bs4, requests, os

url = 'http://xkcd.com'

os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
    # TODO: Download the page.
    print(f'Downloading page {url}...')
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

    # TODO: Find the URL of the comic page.
    comicElem = soup.select('#comic img')

    # TODO: Download the image.
    if len(comicElem) == 0:
        print(f"couldn't download image")
    else:
        try:
            comicUrl = 'http:' + comicElem[0].get('src')
            print(f'Downloading image {comicUrl}')
            res = requests.get(comicUrl)
            res.raise_for_status()
        except requests.exceptions.MissingSchema:
            # skip the comic
            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'http://xkcd.com' + prevLink.get('href')
            continue

    # TODO: Save the image to ./xkcd folder
    imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

    # TODO: Get the previous button url
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

print('Done')