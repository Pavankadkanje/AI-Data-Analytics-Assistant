import pandas as pd


def answer_question(df, question):

    question = question.lower()

    # -------------------------
    # Basic dataset information
    # -------------------------

    if "rows" in question:
        return f"Dataset has {len(df)} rows."

    if "columns" in question:
        return f"Dataset has {df.shape[1]} columns."

    if "shape" in question:
        return f"Dataset shape is {df.shape}"

    if "missing" in question:
        return f"Missing values: {df.isnull().sum().sum()}"

    if "duplicate" in question:
        return f"Duplicate rows: {df.duplicated().sum()}"

    if "column names" in question or "columns name" in question:
        return ", ".join(df.columns)

    # -------------------------
    # Average / Mean
    # -------------------------

    if "average" in question or "mean" in question:

        for col in df.columns:

            if col.lower() in question:

                if pd.api.types.is_numeric_dtype(df[col]):

                    return f"Average {col}: {round(df[col].mean(),2)}"

                else:

                    return f"{col} is not a numeric column."

    # -------------------------
    # Maximum
    # -------------------------

    if "maximum" in question or "max" in question:

        for col in df.columns:

            if col.lower() in question:

                if pd.api.types.is_numeric_dtype(df[col]):

                    return f"Maximum {col}: {df[col].max()}"

    # -------------------------
    # Minimum
    # -------------------------

    if "minimum" in question or "min" in question:

        for col in df.columns:

            if col.lower() in question:

                if pd.api.types.is_numeric_dtype(df[col]):

                    return f"Minimum {col}: {df[col].min()}"

    # -------------------------
    # Describe
    # -------------------------

    if "describe" in question or "summary" in question:

        return df.describe(include="all")

    return "Sorry, I don't understand this question yet."