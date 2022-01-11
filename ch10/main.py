from urllib.request import urlopen
from bs4 import BeautifulSoup
from pprint import pprint
# import requests
import glob
import re

# ? => 0 ou 1
# + => 1 ou n
# * => 0 ou n
# {2} => 2
# {2,5} => 2 à 5
 
def main():
    log_files = glob.glob("*.log")

    reg_ip_1 = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    reg_ip_2 = r"^(.+?)\s"
    reg_status = r"\"\s(\d{3})\s[\d|-]+"
    reg_all = r"^(.+?)\s.*\"\s(\d{3})\s[\d|-]+"

    for log in log_files:
        with open(log) as f:
            for line in f:
                line = line.strip()
                result = re.findall(reg_all, line)
                d = result.pop()
                if '404' in d:
                    print(d)


def main_read_html():
    html=""
    with open('index.html','r') as f:
        html=f.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    list_a = soup.find_all('a')
    list_files = ["http://logs.eolem.com/"+a['href'] for a in soup.find_all('a') if a['href'][0] != "?"]
    pprint(list_files)


# def main_requests():
#     r = requests.get('http://logs.eolem.com/')
#     print(r.text)
#     with open('index.html','w') as f:
#         f.write(r.text)


# def main_urlopen():
#     url = ""
#     with urlopen('http://logs.eolem.com/') as response:
#         for r in response:
#             r = r.decode('utf-8')
#             print(r)

if __name__ == '__main__':
    main()