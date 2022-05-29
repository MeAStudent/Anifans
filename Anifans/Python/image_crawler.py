import requests
import os
import re
import time
from bs4 import BeautifulSoup
from selenium import webdriver

page = "2"
dst_url = "https://www.wallpaperbetter.com/es/search?q=4k+anime&page="

url = dst_url + page

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"}

response = requests.get(url, headers=headers)
response.encoding = "utf-8"

main_page = BeautifulSoup(response.text, "html.parser")
a_list = main_page.find_all("a", attrs={"itemprop": "url"})


options = webdriver.ChromeOptions()
prefs = {"download.default_directory":r'C:\xampp\htdocs\www\Anifans\images',
        "profile.default_content_setting_values.automatic_downloads":1}
options.add_experimental_option("prefs", prefs)



for a in a_list:
    href = a.get("href")
    href_response = requests.get(href, headers=headers)
    href_bs = BeautifulSoup(href_response.text, "html.parser")
    img_link = href_bs.find_all("a", attrs={"rel": "nofollow"})
    
    objective = re.compile(r".*?3840x2160")

    for a in img_link:
        child_href = a.get("href")
        if objective.search(child_href):
            dlink = child_href
    
    driver = webdriver.Chrome(options=options)
    
    driver.get(dlink)
    time.sleep(1)
    driver.quit()

    print(dlink + " download succes!")

print("All contents on this page are donwloaded successfully!")


#rename images
numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

folder = r'C:\xampp\htdocs\www\Anifans\images\\'
count = 1

for old_name in sorted(os.listdir(folder), key=numericalSort):

    new_name = str(count) + ".jpg"
    source = folder + old_name
    
    if os.path.isfile(new_name):
        print('The file already exists"')
        count += 1
    else:
        destination = folder + str(count) + ".jpg"
        os.rename(source, destination)
        count += 1
    
    
print('All Files Renamed')