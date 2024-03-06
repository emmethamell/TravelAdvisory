# Database interactions, models, utils etc
import os
from dotenv import load_dotenv
from supabase import create_client, Client
from travel_advisories.scraper import TravelAdvisory

load_dotenv()
supabaseURL: str = os.environ.get("YOUR_SUPABASE_URL")
print(supabaseURL)
service_role_key: str = os.environ.get("YOUR_SUPABASE_SERVICE_ROLE_KEY")
print(service_role_key)
supabase: Client = create_client(supabaseURL, service_role_key)

def update_travel_advisories():
    contentList = TravelAdvisory.scrape_website()
    # item = [country, level, date, summary]
    for item in contentList:
        supabase.table('travel_advisories').upsert({
            'country': item[0],
            'level': item[1],
            'date_updated': item[2],
            'summary': item[3]
        }).execute()

def get_travel_advisory(country):
    result = supabase.table('travel_advisories').select('*').ilike('country', f'%{country}%').execute() 
    if result:       
        data = result.data
        if not data:
            return "Nothing found"
        data_json = data[0]
        return data_json
    else:
        return "Nothing found"