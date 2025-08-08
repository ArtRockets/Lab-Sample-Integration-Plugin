import pandas as pd
import requests
import json
import logging

# Set up basic logging
logging.basicConfig(filename='plugin_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

# Step 1: Read the CSV file
def read_sample_data(file_path):
    try:
        df = pd.read_csv("C:/Users/tzoar/Downloads/lab_samples.csv")
        logging.info("CSV file loaded successfully.")
        print("✅ Loaded CSV file.")
        return df
    except Exception as e:
        logging.error(f"Failed to load CSV: {e}")
        print("❌ Failed to load CSV file.")
        return None

# Step 2: Clean/filter the data
def clean_data(df):
    df = df.dropna(subset=["volume"])  # Remove rows with missing volume
    df = df[df["volume"] > 0]          # Remove rows with 0 volume
    print(f"✅ Cleaned data. {len(df)} valid samples found.")
    return df

# Step 3: Send each sample as JSON to a mock API
def send_to_api(sample):
    url = "https://jsonplaceholder.typicode.com/posts"  # Mock endpoint
    try:
        response = requests.post(url, json=sample)
        if response.status_code == 201:
            logging.info(f"Successfully sent sample {sample['sample_id']}")
            print(f"📤 Sent sample {sample['sample_id']} successfully.")
        else:
            logging.warning(f"Failed to send sample {sample['sample_id']} - Status Code: {response.status_code}")
            print(f"⚠️ Failed to send sample {sample['sample_id']}")
    except Exception as e:
        logging.error(f"Error sending sample {sample['sample_id']}: {e}")
        print(f"❌ Error sending sample {sample['sample_id']}: {e}")

# Step 4: Main plugin simulation logic
def main():
    df = read_sample_data("lab_samples.csv")
    if df is not None:
        cleaned = clean_data(df)
        for _, row in cleaned.iterrows():
            sample_json = {
                "sample_id": row["sample_id"],
                "sample_type": row["sample_type"],
                "volume": row["volume"]
            }
            send_to_api(sample_json)

if __name__ == "__main__":
    main()
