"""
Author Group 1
Date: 10/03/24
File: data_file_maker.py
Workspace: SWENGroup-1
"""

# Constants:
# None

# Imports:
import json

def create_json_file(filename, json_data):
    # Serializing json
    json_object = json.dumps(json_data, indent=4)
    
    with open(filename, "w") as outfile:
        outfile.write(json_object)

def create_dorm_data():
    # Create 8 machines for each dorm
    machines = {}
    for i in range(1, 9):
        machines[f"machine_{i}"] = {
            "status": "open",
            "time_started": None,
            "duration": None
        }
    return machines

# Main function
def main():
    dorm_names = [
        "Carlton Gibson Hall", "Colby Hall", "Frances Baker Hall", 
        "Fredericka Douglass Sprague Perry Hall", "Helen Fish Hall", 
        "Kate Gleason Hall", "Mark Ellingson Hall", "Peter Peterson Hall", 
        "Residence Hall A", "Residence Hall B", "Residence Hall C", 
        "Residence Hall D", "Sol Heumann Hall"
    ]
    
    # Create a dictionary of dorms, where each key is the dorm name
    dorms_dict = {dorm_name: create_dorm_data() for dorm_name in dorm_names}
    
    # Create JSON file
    create_json_file("machine_data.json", dorms_dict)

# Call the main function
if __name__ == "__main__":
    main()