import pandas as pd
import numpy as np


# -----------------------------
# LOAD DATA
# -----------------------------
def load_data(file_path: str) -> pd.DataFrame:
    """
    Load dataset with correct delimiter and formatting.
    """
    df = pd.read_csv(file_path, sep=';', quotechar='"')
    return df


# -----------------------------
# REMOVE DUPLICATES
# -----------------------------
def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove duplicate rows.
    """
    return df.drop_duplicates().reset_index(drop=True)


# -----------------------------
# DROP IRRELEVANT COLUMNS
# -----------------------------
def drop_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Drop columns not suitable for analysis.
    """
    return df.drop(columns=['duration'])


# -----------------------------
# HANDLE UNKNOWN VALUES
# -----------------------------
def handle_unknowns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Replace 'unknown' with NaN and apply appropriate filling strategy.
    """
    cols = ['job','marital','education','default','housing','loan']

    for col in cols:
        df[col] = df[col].replace('unknown', np.nan)

    for col in cols:
        missing_pct = df[col].isnull().mean()

        if missing_pct < 0.05:
            df[col] = df[col].fillna(df[col].mode()[0])
        else:
            df[col] = df[col].fillna('Unknown')

    return df


# -----------------------------
# FIX PDays & CREATE FLAG
# -----------------------------
def handle_pdays(df: pd.DataFrame) -> pd.DataFrame:
    """
    Replace 999 with NaN and create previously_contacted flag.
    """
    df['pdays'] = df['pdays'].replace(999, np.nan)

    df['previously_contacted'] = df['pdays'].notna().map({
        True: 'yes',
        False: 'no'
    })

    return df


# -----------------------------
# STANDARDIZE TEXT
# -----------------------------
def clean_text_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize all string columns.
    """
    str_cols = df.select_dtypes(include='object').columns

    for col in str_cols:
        df[col] = df[col].str.strip().str.lower()

    # Fix job formatting
    df['job'] = df['job'].str.replace(r'\.$', '', regex=True)

    return df


# -----------------------------
# FIX CATEGORICAL VALUES
# -----------------------------
def fix_categories(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and standardize categorical columns.
    """
    df['marital'] = df['marital'].replace('divorced', 'divorced/widowed')

    education_map = {
        'basic.4y': 'Basic (4 years)',
        'basic.6y': 'Basic (6 years)',
        'basic.9y': 'Basic (9 years)',
        'high.school': 'High School',
        'professional.course': 'Professional Course',
        'university.degree': 'University Degree',
        'illiterate': 'Illiterate',
        'unknown': 'Unknown'
    }

    df['education'] = df['education'].replace(education_map)

    return df


# -----------------------------
# FEATURE ENGINEERING
# -----------------------------
def create_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create new analytical features.
    """

    # Binary target
    df['subscribed'] = df['y'].map({'yes': 1, 'no': 0})

    # Age banding
    df['age_band'] = pd.cut(
        df['age'],
        bins=[0, 25, 35, 45, 55, 65, 100],
        labels=['Under 25','25–34','35–44','45–54','55–64','65+']
    )

    # Education ranking
    edu_order = {
        'Illiterate': 0,
        'Basic (4 years)': 1,
        'Basic (6 years)': 2,
        'Basic (9 years)': 3,
        'High School': 4,
        'Professional Course': 5,
        'University Degree': 6,
        'Unknown': 7
    }

    df['education_rank'] = df['education'].map(edu_order)

    # Month & Day ordering
    month_order = {
        'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,
        'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12
    }

    day_order = {
        'mon':1,'tue':2,'wed':3,'thu':4,'fri':5
    }

    df['month_order'] = df['month'].map(month_order)
    df['day_order'] = df['day_of_week'].map(day_order)

    return df


# -----------------------------
# RENAME COLUMNS
# -----------------------------
def rename_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Rename columns for consistency and compatibility.
    """
    df = df.rename(columns={
        'emp.var.rate': 'emp_var_rate',
        'cons.price.idx': 'cons_price_idx',
        'cons.conf.idx': 'cons_conf_idx',
        'nr.employed': 'nr_employed'
    })

    return df


# -----------------------------
# FINAL PIPELINE
# -----------------------------
def clean_data(file_path: str, output_path: str) -> pd.DataFrame:
    """
    End-to-end data cleaning pipeline.
    """

    df = load_data(file_path)
    df = remove_duplicates(df)
    df = drop_columns(df)
    df = handle_unknowns(df)
    df = handle_pdays(df)
    df = clean_text_columns(df)
    df = fix_categories(df)
    df = create_features(df)
    df = rename_columns(df)

    df.to_csv(output_path, index=False)

    return df