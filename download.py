import os
import sys
import requests
from update_jellyfin import update_jellyfin_library
from get_name import *

link=sys.argv[1]

def download(link,directory):
    os.chdir(directory)
    final_link="python3 -m spotdl --lyrics synced "+link
    os.popen(final_link)
    
directory_name=name(link)

download(link,directory_name)
update_jellyfin_library()
