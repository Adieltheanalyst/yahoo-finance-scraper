import os
import pandas as pd
import json

# Directory where your JSON files are located
directory = "C:/Users/gacha/PycharmProjects/type2"

# Output directory (modify as needed)
output_directory = os.path.join(directory, "converted_files")
os.makedirs(output_directory, exist_ok=True)

# Loop through all files in the directory
for file in os.listdir(directory):
    if file.endswith(".json"):  # Only process JSON files
        file_path = os.path.join(directory, file)

        try:
            # Load JSON file
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Convert to DataFrame
            df = pd.DataFrame(data)

            # Define output file paths
            csv_path = os.path.join(output_directory, file.replace(".json", ".csv"))
            excel_path = os.path.join(output_directory, file.replace(".json", ".xlsx"))

            # Save as CSV and Excel
            df.to_csv(csv_path, index=False)
            df.to_excel(excel_path, index=False)

            print(f"Converted {file} to CSV and Excel successfully!")

        except Exception as e:
            print(f"Error processing {file}: {e}")

print("All JSON files processed.")