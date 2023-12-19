import time

import requests
from bs4 import BeautifulSoup
import multiprocessing
from multiprocessing.dummy import Pool as th_pool


def timer(f):
    """
    Décorateur pour avoir la durée de temps d'exécution
    """

    def wrap(*args, **kwargs):
        tstart = time.time()
        res = f(*args, **kwargs)
        print(f.__name__, time.time() - tstart, "s")
        return res

    return wrap


def top_25_articles_urls():
    """
    Récupère la liste des 25 top articles de wikipedia.

    On utilise Beautiful soup pour parser le HTTP
    """
    r = requests.get("http://en.wikipedia.org/wiki/Wikipedia:Top_25_Report")
    d = BeautifulSoup(r.text, features="html.parser")
    urls = []
    for table in d.find_all("table", class_="wikitable"):
        for row in table.find_all("tr"):
            row = row.find_all("td")
            try:
                link = row[1].find_all("a")[0].attrs["href"]
            except IndexError:
                pass
            else:
                urls.append("http://en.wikipedia.org" + link)
    return urls


def download_article_and_count_words(url):
    """
    Fonction de base qui va télécharger un article et compter le
    nombre de mots qui le constituent.

    On effectue aussi des affichage pour identifier les process en cours.
    """
    article = requests.get(url).content
    count = len(article.split())
    print("    * downloading", url, " : ", count)
    print("      * pid", multiprocessing.current_process())
    return count


@timer
def sequential_urls_download():
    urls = top_25_articles_urls()
    for url in urls:
        print(url, download_article_and_count_words(url))


@timer
def mp_urls_download():
    urls = top_25_articles_urls()
    p = multiprocessing.Pool(processes=20)  # Give me moarrr
    p.map(download_article_and_count_words, urls)


@timer
def th_urls_download():
    urls = top_25_articles_urls()
    # on utilise un pool threadé...
    p = th_pool()
    p.map(download_article_and_count_words, urls)


def main():
    sequential_urls_download()
    mp_urls_download()
    th_urls_download()


if __name__ == "__main__":
    main()
