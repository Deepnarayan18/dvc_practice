import pandas as pd
import os

# कुछ sample data
data = {
    'Name': ['Rahul', 'Amit', 'Priya', 'Neha'],
    'Age': [25, 30, 22, 28],
    'City': ['Delhi', 'Mumbai', 'Kolkata', 'Chennai']
}

# DataFrame बनाएं
df = pd.DataFrame(data)

# 'data' नाम की डायरेक्टरी बनाएं (अगर पहले से नहीं है)
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)  # makedirs बेहतर है क्योंकि यह nested directories भी बना सकता है

# फाइल को सेव करने का path
file_path = os.path.join(data_dir, "sample.csv")

# CSV फाइल में सेव करें
df.to_csv(file_path, index=False)

print(f"CSV file saved at: {os.path.abspath(file_path)}")
