import time
import requests
import threading
import concurrent.futures

thead_local = threading.local()


def get_session():
    if not hasattr(thead_local, 'session'):
        thead_local.session = requests.Session()
    return thead_local.session


def download_site(url: str):
    session = get_session()
    with session.get(url) as resp:
        print(f"Read {len(resp.content)} from {url}")


def download_all_sites(sites: list):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_site, sites)


if __name__ == '__main__':
    sites = [
                "https://appdb.winehq.org/index.php",
                "https://reyestr.court.gov.ua/Review/96673802",
                "https://habr.com/ru/post/46598/",
                # "https://lurkmore.to/Python",
                "https://htmlacademy.ru/blog/boost/frontend/git-console",
                "https://tproger.ru/articles/cool-linux-commands/",
                "https://runestone.academy/runestone/books/published/pythonds/Introduction/InputandOutput.html",
                "https://itproger.com/news/5-sovetov-dlya-nachinayushtih-programmistov",
                "https://realpython.com/what-can-i-do-with-python/"
            ] * 100
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)}, Duration: {duration} sec")



