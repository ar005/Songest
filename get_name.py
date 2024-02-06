import subprocess
import re
from bs4 import BeautifulSoup
from check_folder import check_and_create_folder

def send_curl_request(url):
    try:
        # Execute cURL command
        output = subprocess.check_output(['curl', url], stderr=subprocess.STDOUT)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        #print("Error executing cURL command:", e.output)
        return None

def extract_meta_description(response):
    # Find the line containing meta name="description" content=
    pattern = r'<meta\s+name="description"\s+content="(.+?)">'
    match = re.search(pattern, response)
    if match:
        return match.group(1)
    else:
        return "No meta description found."
    
def name(url):
    response = send_curl_request(url)
    if response:
        meta_description = extract_meta_description(response)
        soup = BeautifulSoup(meta_description, 'html.parser')
        # Extracting name
        name = soup.find('meta', property='og:title')['content']
        # Extracting type
        type_ = soup.find('meta', property='og:type')['content']
        
        check_and_create_folder(name)
        
        return name
        # print("Name:", name)
        # print("Type:", type_)
        

    
    
    
        
