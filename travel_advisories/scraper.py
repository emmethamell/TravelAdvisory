from bs4 import BeautifulSoup
import time
import requests


class TravelAdvisory:
    
    @staticmethod
    def scrape_website():
        base_url = "https://travel.state.gov"
        response = requests.get("https://travel.state.gov/content/travel/en/traveladvisories/traveladvisories.html/")
        
        return_list = []
        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            rows = soup.find_all('tr')
           
            for row in rows:
                data = row.find_all('td')
                
                data_text = [td.text for td in data]
                
                link = row.find('a')
                
                if link and link.get('href'):
                    link_url = base_url + link['href']
                    summary = TravelAdvisory.scrape_advisory_page(link_url)
                    
                    data_text.append(summary)
                    return_list.append(data_text)
        else:
            print("Error:", response.status_code)
            
        return TravelAdvisory.clean_content(return_list)
    
    
    @staticmethod
    def scrape_advisory_page(url):
        try:
            response = requests.get(url)
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
        
            summary_tag = soup.find('b', string=lambda text: 'summary' in text.lower())
        
            if summary_tag and summary_tag.parent.name == 'p':
                return summary_tag.parent.text.strip()
        
            return 'N/A'
        except:
            return 'N/A'
          
    @staticmethod
    def clean_content(content_list):
        new_list = []
        for item in content_list:
            if 'Travel' in item[0]:
                words = item[0].split()
                index = words.index('Travel')
                country = ' '.join(words[:index])
                new_list.append([country, item[1], item[2], item[3]])
        return new_list