import os
import json
import sys

# Set the default values for mime type and other variables
mime_type = ""
json_folder = "generated"
json_file = "furnidata.json"

# Create the generated folder if it doesn't exist
if not os.path.exists(json_folder):
    os.makedirs(json_folder)

# Function to retrieve the file list from the directory
def get_file_list(directory, mime_type):
    file_list = []
    try:
        for file_name in os.listdir(directory):
            file_path = os.path.join(directory, file_name)
            if os.path.isfile(file_path) and file_name.endswith(mime_type):
                file_list.append(file_path)
    except Exception:
        print("An exception occurred while retrieving the file list.")
    return file_list

# Initialize furnidata
furnidata = {
    "roomitemtypes": {
        "furnitype": []
    }
}

# Default the directory to "furni" in the current project directory
directory = os.path.join(os.getcwd(), "furni")

# Prompt the user to enter the desired starting point for the id values
while True:
    try:
        starting_id = int(input("Enter the desired starting point for the id values: "))
        break
    except ValueError:
        print("Invalid input. Please enter a proper integer value.")

# Prompt the user to select the MIME type
valid_choice = False
while not valid_choice:
    try:
        mime_choice = input("Select the desired MIME type:\n1. .swf\n2. .nitro\n")
        if mime_choice == "1":
            mime_type = ".swf"
            valid_choice = True
        elif mime_choice == "2":
            mime_type = ".nitro"
            valid_choice = True
        else:
            print("Invalid choice. Please select 1 or 2.")
    except Exception:
        print("An exception occurred while prompting for the MIME type.")

# Retrieve the file list from the directory
file_list = get_file_list(directory, mime_type)

# Initialize id counter with the starting ID value
id_counter = starting_id

# Initialize the entry count
entry_count = 0

for file_path in file_list:
    try:
        # Extract the classname from the file name
        file_name = os.path.basename(file_path)
        classname = os.path.splitext(file_name)[0]

        # Create a JSON entry for each unique classname
        entry = {
            "id": id_counter,
            "classname": classname,
            "revision": -1,
            "category": "null",
            "defaultdir": 0,
            "xdim": 1,
            "ydim": 1,
            "name": "null",
            "description": "null",
            "adurl": None,
            "offerid": -1,
            "buyout": False,
            "rentofferid": -1,
            "rentbuyout": False,
            "bc": False,
            "excludeddynamic": False,
            "customparams": None,
            "specialtype": -1,
            "canstandon": False,
            "cansiton": False,
            "canlayon": False,
            "furniline": "null",
            "environment": None,
            "rare": False
        }

        # Increment the id counter
        id_counter += 1

        # Append the entry to the list
        furnidata["roomitemtypes"]["furnitype"].append(entry)

        # Increment the entry count
        entry_count += 1
    except Exception:
        print("An exception occurred while processing file:", file_path)
        sys.exit(1)

# Save the entries in a JSON file inside the generated folder
json_path = os.path.join(json_folder, json_file)
try:
    with open(json_path, "w") as f:
        json.dump(furnidata, f, indent=4)
except Exception:
    print("An exception occurred while saving the JSON file.")
    sys.exit(1)

# Check if the entry count is 0
if entry_count == 0:
    if mime_type == ".swf":
        print("No SWF files found in the 'furni' folder. Please add your .swf files to the folder.")
    elif mime_type == ".nitro":
        print("No Nitro files found in the 'furni' folder. Please add your .nitro files to the folder.")
else:
    # Print the entry count
    print(f"Generated {entry_count} entries in the {json_file} successfully in the '{json_folder}' folder.")
