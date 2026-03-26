from src.data_cleaning import clean_data

input_path = "data/raw/bank-additional-full.csv"
output_path = "data/processed/bank_marketing_clean.csv"

df = clean_data(input_path, output_path)

print("Data cleaning completed.")
print(f"Final shape: {df.shape}")