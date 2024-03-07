import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize
from nltk import bigrams

def get_soup(url):
    """Get BeautifulSoup object from URL."""
    res = requests.get(url)
    return BeautifulSoup(res.content, "html.parser")

def analyze_head(soup):
    """Analyze HTML head section."""
    results = {}
    title_tag = soup.find('title')
    results['title'] = 1 if title_tag else 0
    results['title_length'] = len(title_tag.get_text()) if title_tag else 0

    description_tag = soup.find('meta', attrs={'name': 'description'})
    results['description'] = 1 if description_tag else 0

    return results

def analyze_body(soup):
    """Analyze HTML body section."""
    results = {}

    h1 = soup.find('h1')
    results['h1'] = 1 if h1 else 0

    h_tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
    h_tags_order = [int(tag.name[1]) for tag in soup.find_all(h_tags)]
    results['h_tags_order'] = 1 if len(set(h_tags_order)) != len(h_tags_order) else 0

    results['h1_count'] = len(soup.find_all('h1'))

    results['img_alt'] = 1 if soup.find('img', alt='') else 0

    body_text = soup.find('body').get_text().lower()
    words = [word for word in word_tokenize(body_text) if word.isalpha()]

    with open('english', 'r') as file:
        stopwords = set(line.strip() for line in file)

    filtered_words = [word for word in words if word not in stopwords]
    new_bigrams = list(bigrams(filtered_words))
    bi_freq = nltk.FreqDist(new_bigrams).most_common(10)

    most_common_bigram_strings = [" ".join(bigram) for bigram, freq in bi_freq]
    keywords_dict = {str(i + 1): keyword for i, keyword in enumerate(most_common_bigram_strings)}

    results['keywords'] = keywords_dict
    return results

def analyze_url(url):
    """Analyze URL for SEO."""
    soup = get_soup(url)
    head_results = analyze_head(soup)
    body_results = analyze_body(soup)

    # Combine results from head and body analysis
    results = {**head_results, **body_results}
    results['url'] = url
    return results
