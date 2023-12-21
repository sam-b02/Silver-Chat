from bs4 import BeautifulSoup
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import time

# Function for requests retry session
def requests_retry_session(retries=3, backoff_factor=0.3, status_forcelist=(500, 502, 503, 504), session=None):
    session = session or requests.Session()
    retry = Retry(total=retries, read=retries, connect=retries, backoff_factor=backoff_factor, status_forcelist=status_forcelist)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session

# Base URLs
urls = [
    "https://forums.tomshardware.com/forums/networking.31/page-", .#0
    "https://forums.tomshardware.com/forums/systems.7/page-", #1
    "https://forums.tomshardware.com/forums/windows-11.84/page-", #2
    "https://forums.tomshardware.com/forums/windows-10.13/page-", #3
    "https://forums.tomshardware.com/forums/macos.20/page-", #4
    "https://forums.tomshardware.com/forums/antivirus-security-privacy.24/page-", #5
    "https://forums.tomshardware.com/forums/computer-peripherals.45/page-", #6
    "https://forums.tomshardware.com/forums/home-audio-theater.48/page-", #7
    "https://forums.tomshardware.com/forums/consumer-electronics.49/page-", #8
    "https://forums.tomshardware.com/forums/wireless-networking.32/page-", #9
    "https://forums.tomshardware.com/forums/android-chrome-os.35/page-", #10
    "https://forums.tomshardware.com/forums/laptop-general-discussion.40/page-", #11
    "https://forums.tomshardware.com/forums/laptop-tech-support.41/page-", #12
    "https://forums.tomshardware.com/forums/macbooks.42/page-" #13
]

url2 = "?prefix_id=2"


def get_max_page_number(soup):
    page_items = soup.find_all('li', class_='pageNav-page')
    if page_items:
        # Get the href attribute of the <a> tag within the last <li> element
        last_page_href = page_items[-1].find('a').get('href')
        # Extract the page number from the href value
        max_page_number = int(last_page_href.split('/')[-1].split('?')[0].replace('page-', ''))
        if max_page_number > 100:
            max_page_number = 100
        print(max_page_number)
        return max_page_number
        
    else:
        # Return 1 if there are no pagination items found
        return 1

m = 26

with open("questions.txt", "a", encoding='utf-8') as questions_file, open("answers.txt", "a", encoding='utf-8') as answers_file:
    for count in range(4,15):
        response = requests_retry_session().get(urls[count-1] + "1" + url2, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        max_page = get_max_page_number(soup)

        for i in range(m, max_page + 1):
            m = 1
            time.sleep(0.5)
            url = urls[count-1] + str(i) + url2
            response = requests_retry_session().get(url, timeout=10)
            if response.status_code == 200:
                html_content = response.text
                soup = BeautifulSoup(html_content, 'html.parser')
                thread_links = soup.find_all('a', attrs={'data-xf-init': 'preview-tooltip'})
                counter = 1
                for link in thread_links:
                    thread_url = "https://forums.tomshardware.com" + link['href']
                    thread_response = requests_retry_session().get(thread_url, timeout=5)

                    if thread_response.status_code == 200:
                        thread_soup = BeautifulSoup(thread_response.text, 'html.parser')
                        title = thread_soup.find('h1').text.strip()

                        question_content = thread_soup.find('div', {'class': 'bbWrapper'}).text.strip()
                        bb_wrappers = thread_soup.find_all('div', {'class': 'bbWrapper'})

                        if bb_wrappers and len(bb_wrappers) > 1:
                            answer_content = bb_wrappers[1].text.strip()
                            answers_file.write(title + "\n" + answer_content + "\n")
                            answers_file.write(f"------------------------------------------------count is {count} and i is {i} and counter is {counter}\n")
                            questions_file.write(title + "\n" + question_content + "\n")
                            questions_file.write(f"------------------------------------------------count is {count} and i is {i} and counter is {counter}\n")
                            print(f"count is {count} and i is {i} and counter is {counter}")
                            counter = counter + 1
                        else:
                            answers_file.write("No answer found\n\n")
                        time.sleep(0.8)
                    
                

            