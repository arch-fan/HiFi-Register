import requests
from dotenv import load_dotenv
import os

load_dotenv()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
    'X-Requested-With': 'XMLHttpRequest',
    'Cookie': f"bbs_token={os.environ.get('AUTH_TOKEN')}",
}

response = requests.post('https://www.hifini.com/sg_sign.htm', headers=headers)
print(response.json())