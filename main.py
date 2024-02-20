import requests
from bs4 import BeautifulSoup

def analyze_head(url):
    results = {}
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")
    title = soup.find('title').get_text()
    if title:
        results['title'] = 1
        results['title_length'] = len(title)
    else:
        results['title'] = 0
    
    description = soup.find('meta', attrs={'name': 'description'})['content']
    if description:
        results['description'] = 1
    else:
        results['description'] = 0

    return results

def analyze_body(url):
    results = {}
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")
    h1 = soup.find('h1')
    if h1:
        results['h1'] = 1
    else:
        results['h1'] = 0
    
    hs = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
    h1_count = 0
    stack = []

    for h in soup.find_all(hs):
        level = int(h.name[1])
        
        if h.name == 'h1':
            h1_count += 1

        while stack and stack[-1] >= level:
            stack.pop()
        
        if stack and stack[-1] != level - 1:
            results['h_tags_order'] = 1
        else:
            results['h_tags_order'] = 0

        stack.append(level)
    results ['h1_count'] = h1_count
    return results

print(analyze_head('https://blog.boot.dev/python/python-for-web-development/'))
print(analyze_body('https://blog.boot.dev/python/python-for-web-development/'))
