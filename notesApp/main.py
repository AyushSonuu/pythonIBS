import streamlit as st
import pandas as pd

def read_csv_file(uploaded_file):
    """
    Read the uploaded CSV file into a Pandas DataFrame.
    
    Parameters:
    - uploaded_file: The uploaded CSV file.
    
    Returns:
    - DataFrame: The Pandas DataFrame containing the data.
    """
    if uploaded_file is not None:
        try:
            # Read CSV file into DataFrame
            df = pd.read_csv(uploaded_file)
            return df
        except Exception as e:
            st.error(f"Error reading CSV file: {e}")
            return None
    else:
        st.warning("Please upload a CSV file.")
        return None

def get_column_names(df):
    """
    Get column names from a Pandas DataFrame.
    
    Parameters:
    - df: The Pandas DataFrame.
    
    Returns:
    - list: A list of column names.
    """
    if df is not None:
        return df.columns.tolist()
    else:
        return []

def display_columns(selected_columns, df):
    """
    Display selected columns from a Pandas DataFrame.
    
    Parameters:
    - selected_columns: List of selected column names.
    - df: The Pandas DataFrame.
    """
    st.subheader("Selected Columns:")
    st.write(df[selected_columns])

def transform_columns(selected_columns, df, transformation, **kwargs):
    """
    Apply transformation to selected columns in a Pandas DataFrame.
    
    Parameters:
    - selected_columns: List of selected column names.
    - df: The Pandas DataFrame.
    - transformation: The transformation to apply (e.g., 'strip', 'lower', 'upper', 'split', 'join').
    - **kwargs: Additional keyword arguments for transformations (e.g., 'sep' for 'join' transformation).
    
    Returns:
    - DataFrame: The transformed DataFrame.
    """
    transformed_df = df.copy()
    
    for col in selected_columns:
        if transformation == 'strip':
            transformed_df[col] = transformed_df[col].str.strip()
        elif transformation == 'lower':
            transformed_df[col] = transformed_df[col].str.lower()
        elif transformation == 'upper':
            transformed_df[col] = transformed_df[col].str.upper()
        elif transformation == 'split':
            if 'sep' in kwargs:
                transformed_df[col] = transformed_df[col].str.split(kwargs['sep'])
            else:
                transformed_df[col] = transformed_df[col].str.split()
        elif transformation == 'join':
            if 'sep' in kwargs:
                transformed_df[col] = transformed_df[col].apply(lambda x: kwargs['sep'].join(x))
            else:
                transformed_df[col] = transformed_df[col].apply(lambda x: ' '.join(x))
        # Add more transformations as needed
        
    return transformed_df

def main():
    st.set_page_config(page_title='Transformation')
    
    # Upload CSV file
    uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=['csv'])
    
    # Read CSV file into DataFrame
    df = read_csv_file(uploaded_file)
    
    if df is not None:
        # Get column names
        column_names = get_column_names(df)
        
        # Display checkboxes for selecting columns
        st.sidebar.header("Select Columns")
        selected_columns = st.sidebar.multiselect("Columns", options=column_names)
        
        # Display transformation options
        st.sidebar.header("Transformation")
        transformation = st.sidebar.selectbox("Choose Transformation", ["strip", "lower", "upper"])
        
        # Display selected columns when button is clicked
        if st.sidebar.button("Apply Transformation"):
            transformed_df = transform_columns(selected_columns, df, transformation)
            display_columns(selected_columns, transformed_df)

if __name__ == '__main__':
    main()
