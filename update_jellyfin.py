import os
import sys
import requests

def update_jellyfin_library():
    #print("updated")
    
    jellyfin_url = ""
    api_key = ""
    
    # Construct the URL for updating the library
    update_url = f"{jellyfin_url}/Library/Refresh?api_key={api_key}"

    try:
        # Send a POST request to trigger library update
        response = requests.post(update_url)
        response.raise_for_status()  # Raise an error for unsuccessful requests

        # Check if the request was successful
        if response.status_code == 200:
            #print("Library update initiated successfully.")
            pass
        else:
            #print(f"Failed to initiate library update. Status code: {response.status_code}")
            pass
    except requests.exceptions.RequestException as e:
        # Handle any exceptions that occurred during the request
        #print("Error occurred during library update:", e)


update_jellyfin_library()