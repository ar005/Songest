import os

def check_and_create_folder(folder_name):
    # Get the current directory
    current_directory = os.getcwd()
    
    # Check if the folder already exists
    if os.path.exists(os.path.join(current_directory, folder_name)) and os.path.isdir(os.path.join(current_directory, folder_name)):
        #print(f"The folder '{folder_name}' already exists.")
        pass
    else:
        # Create the folder if it doesn't exist
        os.makedirs(os.path.join(current_directory, folder_name))
        #print(f"Folder '{folder_name}' created successfully.")

# if __name__ == "__main__":
#     folder_name = input("Enter the folder name: ")
#     check_and_create_folder(folder_name)
