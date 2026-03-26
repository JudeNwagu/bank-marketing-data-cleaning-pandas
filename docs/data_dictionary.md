
# 📘 Data Dictionary  Bank Marketing Dataset

This document describes all variables in the cleaned dataset used for analysis and reporting.

---

## 📊 Dataset Overview

* **Records:** 41,176
* **Features:** 26
* **Target Variable:** `y` (subscription outcome)

Each row represents a client contacted during a marketing campaign.

---

## 🧾 Column Definitions

### 👤 Customer Demographics

| Column      | Type        | Description       | Notes                              |
| ----------- | ----------- | ----------------- | ---------------------------------- |
| `age`       | Integer     | Age of the client | Range: 17–98                       |
| `job`       | Categorical | Type of job       | Cleaned (e.g., "admin." → "admin") |
| `marital`   | Categorical | Marital status    | `divorced` includes widowed        |
| `education` | Categorical | Education level   | Standardized labels applied        |

---

### 💳 Financial & Personal Status

| Column    | Type        | Description            | Notes                            |
| --------- | ----------- | ---------------------- | -------------------------------- |
| `default` | Categorical | Has credit in default? | High missing → kept as "Unknown" |
| `housing` | Categorical | Has housing loan?      | Missing values filled            |
| `loan`    | Categorical | Has personal loan?     | Missing values filled            |

---

### 📞 Campaign Information

| Column        | Type        | Description                        | Notes                        |
| ------------- | ----------- | ---------------------------------- | ---------------------------- |
| `contact`     | Categorical | Contact method                     | Cellular or telephone        |
| `month`       | Categorical | Last contact month                 | Not full-year data           |
| `day_of_week` | Categorical | Day of contact                     | Mon–Fri only                 |
| `campaign`    | Integer     | Number of contacts during campaign | Contains outliers (up to 56) |

---

### 📈 Previous Campaign History

| Column     | Type        | Description                  | Notes                  |
| ---------- | ----------- | ---------------------------- | ---------------------- |
| `pdays`    | Float       | Days since last contact      | 999 replaced with NaN  |
| `previous` | Integer     | Number of previous contacts  | Mostly zero            |
| `poutcome` | Categorical | Outcome of previous campaign | "nonexistent" is valid |

---

### 🌍 Economic Indicators

| Column           | Type  | Description               | Notes                   |
| ---------------- | ----- | ------------------------- | ----------------------- |
| `emp_var_rate`   | Float | Employment variation rate | Renamed for consistency |
| `cons_price_idx` | Float | Consumer price index      |                         |
| `cons_conf_idx`  | Float | Consumer confidence index |                         |
| `euribor3m`      | Float | Euribor 3-month rate      |                         |
| `nr_employed`    | Float | Number of employees       |                         |

---

### 🎯 Target Variable

| Column       | Type        | Description            | Notes           |
| ------------ | ----------- | ---------------------- | --------------- |
| `y`          | Categorical | Subscription outcome   | yes / no        |
| `subscribed` | Integer     | Binary target variable | 1 = yes, 0 = no |

---

### 🆕 Engineered Features

| Column                 | Type        | Description                         | Notes                         |
| ---------------------- | ----------- | ----------------------------------- | ----------------------------- |
| `previously_contacted` | Categorical | Whether client was contacted before | Derived from `pdays`          |
| `age_band`             | Categorical | Grouped age ranges                  | Used for segmentation         |
| `education_rank`       | Integer     | Numeric ranking of education        | Enables ordered analysis      |
| `month_order`          | Integer     | Month sorting index                 | Prevents alphabetical sorting |
| `day_order`            | Integer     | Day sorting index                   | Mon → Fri                     |

---

## ⚠️ Data Notes & Considerations

* No true null values initially; missing data stored as `"unknown"`
* `default` variable has **20.9% missing values**
* `pdays` dominated by placeholder value `999` (converted to NaN)
* Dataset is **imbalanced**:

  * ~89% = No subscription
  * ~11% = Subscription
* Campaign activity is **seasonal**, with heavy concentration in May
* `duration` column was removed due to **data leakage**

---

## 📌 Usage

This dataset is prepared for:

* Data analysis
* Dashboarding (Power BI / Excel)
* Customer segmentation
* Campaign performance evaluation

---

## 🧠 Interpretation Guide

* Use **percentages instead of counts** for target analysis due to imbalance
* Treat `"Unknown"` values as meaningful segments, not errors
* Focus on:

  * Customer profiles with higher conversion rates
  * Campaign timing effectiveness
  * Impact of previous contact history



