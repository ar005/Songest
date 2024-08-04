import subprocess
import re
from bs4 import BeautifulSoup
from check_folder import check_and_create_folder

def send_curl_request(url):
    try:

        output = subprocess.check_output(['curl', url], stderr=subprocess.STDOUT)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:

        return None

def extract_meta_tags(response):

    soup = BeautifulSoup(response, 'html.parser')
    
    # Extract the meta tags
    title = soup.find('meta', property='og:title')
    type_ = soup.find('meta', property='og:type')

    return {
        'title': title['content'] if title else "No title found.",
        'type': type_['content'] if type_ else "No type found."
    }

def name(url):
    response = send_curl_request(url)
    if response:
        meta_tags = extract_meta_tags(response)
        name = meta_tags['title']
        type_ = meta_tags['type']
        
        check_and_create_folder(name)
        return name
