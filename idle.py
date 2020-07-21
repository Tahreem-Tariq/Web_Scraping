'''Name: Tahreem Tariq
   Project: Web Scraping
   Purpose: To extract data from web
   Date: 07/20/2020'''

from bs4 import BeautifulSoup
import requests
import csv



Source = requests.get('https://www.healthline.com/nutrition/17-tips-to-sleep-better').text

Sleep = BeautifulSoup(Source, 'html.parser')

csv_file = open('cms_scraping.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Tip', 'Summary'])

Tips = Sleep.find('div',  class_='css-13sft9o').h1.text
print(Tips)
print()


h2s = Sleep.find_all("h2")
blockquotes = Sleep.find_all("blockquote")

count = 0
total = 0

for h2 in h2s:
    print(h2.a.text.strip())
    #csv_writer.writerow(h2)
    total += 1
    for blockquote in blockquotes:
        count += 1
        if count == total:
            print("Summary:",blockquote.p.text.strip())
            print()
        else:
            continue
    csv_writer.writerow([h2.a.text.strip(),blockquote.p.text.strip()])
        
        
    count = 0
    if total == 17:
        break
csv_file.close()
