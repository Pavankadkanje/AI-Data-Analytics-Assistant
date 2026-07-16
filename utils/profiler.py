import pandas as pd

def dataset_summary(df):
    return {
        "Rows": df.shape[0],
        "Columns": df.shape[1],
        "Missing Values": df.isnull().sum().sum(),
        "Duplicate Rows": df.duplicated().sum(),
        "Memory (KB)": round(df.memory_usage(deep=True).sum()/1024,2)
    }


def column_information(df):
    return pd.DataFrame({
        "Column": df.columns,
        "Datatype": df.dtypes.astype(str),
        "Missing": df.isnull().sum().values,
        "Unique": df.nunique().values
    })


def statistical_summary(df):
    return df.describe(include="all")


def missing_report(df):
    return pd.DataFrame({
        "Column": df.columns,
        "Missing": df.isnull().sum(),
        "Percentage": round(df.isnull().sum()/len(df)*100,2)
    })