import json

 
# function to add to JSON
def write_json(new_data, filename='customerreviews.json'):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["businessCategory"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)
 
    # python object to be appended
y = {"businessCategory":3,
     "rating": 0,
     "reviewText": "Terrible food, unhygenic place"
    }
     
write_json(y)

