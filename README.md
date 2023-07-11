# Furnidata Generator

This script generates a JSON file containing entries for furniture items based on SWF or Nitro files in the specified directory. The generated JSON file follows a specific structure and can be used for various purposes in a project.

## Usage

1. Place your SWF or Nitro files in the "furni" directory.
2. To execute the script, navigate to the directory where the "furnidata_generator.py" file is located and run the command: python furnidata_generator.py
3. Follow the prompts to specify the starting point for ID values and select the desired MIME type.
4. The script will process the files and generate a JSON file with the furniture item entries.
5. The generated JSON file will be saved in the "generated" folder as "furnidata.json".

## Configuration

- `json_folder`: The folder where the generated JSON file will be saved. By default, it is set to "generated".
- `json_file`: The name of the generated JSON file. By default, it is set to "furnidata.json".

## Functionality

1. The script retrieves the file list from the specified directory based on the MIME type.
2. It prompts the user to enter the desired starting point for the ID values.
3. The user selects the MIME type for filtering the files.
4. The script processes the files, extracts the classname from each file, and creates a JSON entry for each unique classname.
5. The generated JSON entries contain various properties such as ID, classname, revision, category, dimensions, name, description, etc.
6. The script saves the generated entries in a JSON file with proper indentation.
7. If no files are found or processed, appropriate error messages are displayed.

**Note:** Ensure that the necessary files are present in the "furni" directory and the desired MIME type is selected correctly.

## Reminder
This script lacks the ability to differentiate between furniture placed on the floor and furniture placed on walls. Consequently, when generating the furnidata entries, it will assume that all furniture belongs to the floor category due to its prevalence. As a result, the generated furnidata.json file will not include the section for wall furniture. It is recommended to either copy these entries to a separate furnidata file that follows the appropriate furnidata structure with a wall section, or manually incorporate the wall section into the generated furnidata.

## Credits

This script was created by Gizmo.

## Donate

If you wish to donate, please contact Gizmo#1813 on Discord.
