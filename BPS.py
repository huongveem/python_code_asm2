import pandas as pd

def data_processing(action_type, file_name, column_name):
    data_frame = pd.read_csv(file_name)

    if action_type == "a":
        processed_data = data_frame.dropna()
    elif action_type == "b":
        processed_data = data_frame.drop_duplicates()
    elif action_type == "c":
        if column_name is None:
            print("Error: Please provide a column name for action C")
            return None
        processed_data = data_frame[data_frame[column_name] >= 0]
    elif action_type == "d":
        if column_name is None:
            print("Error: Please provide a column name for action D")
            return None
        data_frame[column_name] = data_frame[column_name].str.replace(r'[^a-zA-Z0-9\s]', '', regex=True)
        processed_data = data_frame
    else:
        print("Error: Invalid action")
        return None

    processed_data.to_csv(f"processed_{file_name}", index=False)
    print(f"File {file_name} has been implemented action_type {action_type} and saved as processed_{file_name}")

# Example usage:
#a: Delete blank data
#b: Remove duplicate data
#c: Delete data containing negative numbers
#d: Delete data containing special characters
    
action_type = "a"
file_name = "product.csv"
column_name = "Name"

data_processing(action_type, file_name, column_name) 