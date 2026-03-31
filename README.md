#  Bank Marketing Data Cleaning with Pandas

This project focuses on cleaning and preparing raw marketing campaign data from a Portuguese bank for analysis and reporting.

---

##  Objective

The dataset is based on direct marketing campaigns (phone calls).  
The goal is to prepare the data for analyzing whether a client will subscribe to a term deposit.

---

##  What This Project Covers

- Data profiling and inspection  
- Handling hidden missing values ("unknown")  
- Removing duplicates  
- Cleaning categorical variables  
- Feature engineering  
- Preparing data for Power BI  

---

## 📂 Project Structure
bank-marketing-data-cleaning-pandas/
 ```
 │
 ├── data/
 │ ├── raw/
 │ └── processed/
 │
 ├── notebooks/
 │ └── 01_data_cleaning.ipynb
 │
 ├── src/
 │ └── data_cleaning.py
 │
 ├── docs/
 │ └── data_dictionary.md
 │
 ├── main.py
 ├── requirements.txt
 └── README.md
```
---

##  How to Run This Project

1. Clone the repository:

https://github.com/JudeNwagu/bank-marketing-data-cleaning-pandas.git

2. Install dependencies:

pip install -r requirements.txt

3. Run the cleaning pipeline:

python main.py


---

##  Key Cleaning Steps

- Fixed incorrect data loading (delimiter issue)  
- Replaced "unknown" values with proper handling strategy  
- Removed duplicate rows  
- Dropped `duration` column (data leakage)  
- Standardized categorical variables  
- Created new features for analysis  

---

##  Output

Clean dataset saved to:

data/processed/bank_marketing_clean.csv


---

##  Next Step

The cleaned dataset is used in Power BI for:

- Customer segmentation  
- Campaign performance analysis  
- Conversion insights  

---

##  Tech Stack Used

- Language: Python  
- Libraries: Pandas, NumPy  
- Visualization: Power BI  
- Version Control: Git 

---

##  Contact

If you're interested in my work or have opportunities in data analytics, feel free to connect.
