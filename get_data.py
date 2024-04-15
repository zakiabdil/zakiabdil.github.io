from bs4 import BeautifulSoup
import requests
from datetime import datetime
import json

html_text = requests.get('https://www.republika.co.id/').text
soup = BeautifulSoup(html_text, 'html.parser')

months = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober",
          "November", "Desember"]

# dapatkan semua dengan class "....rder conten1"
news = soup.find_all('li', class_='list-group-item list-border conten1')
# deklarasi list
data = []
# pembukaan file json untuk menulis
with open('data.json', 'w') as f:
    for new in news:
        # strip fungsinya removing useless white space di awal dan di akhir kalimat
        title = new.h3.text.strip()
        categories = new.find('span', class_='kanal-info').text

        current_year = str(datetime.now().date())[0:4] + " "
        current_month = int(str(datetime.now().date())[5:7])
        current_date = str(int(str(datetime.now().date())[8:10])) + " "
        current_hour = str(datetime.now().isoformat())[11:13] + ":"
        current_minute = str(datetime.now().isoformat())[14:16] + ":"
        current_second = str(datetime.now().isoformat())[17:19]

        waktuScraping = current_date + months[
            current_month - 1] + " " + current_year + current_hour + current_minute + current_second
        waktuPublish = (new.find('div', class_='date').text.split('-')[1]).strip()

        info = {"judul": title, "kategori": categories, "waktu_publish": waktuPublish,
                "waktu_scraping": waktuScraping}
        data.append(info)
    # Mengubah format dictionary/json menjadi format string
    jdumps = json.dumps(data)
    # menuliskan data pada data.json
    f.writelines(jdumps)
