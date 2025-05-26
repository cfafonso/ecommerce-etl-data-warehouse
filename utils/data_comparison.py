

def check_unique_value_equality(df_1, key_1, df_2, key_2):
    """
    Checks if two dataframes contain exactly the same set of unique values in the specified columns.

    Args:
        df_1 (pandas.DataFrame): the first dataframe to compare.
        key_1 (str): the column name in df_1 containing the values to check.
        df_2 (pandas.DataFrame): the second dataframe to compare.
        key_2 (str): the column name in df_2 containing the values to check.

    Returns:
        bool: True if the sets of unique values in both columns of the two dataframes are identical or
              False otherwise.
    """

    return set(df_1[key_1].unique()) == set(df_2[key_2].unique())


def is_subset_of(df_subset, key_subset, df_superset, key_superset):
    """
    Checks if the unique values in a dataframe's column are a subset of the unique values in another
    dataframe's column. It prints whether the subset relationship exists and if so, also prints the 
    percentage of values from the superset that are covered by the subset.

    Args:
        df_subset (pandas.DataFrame): the dataframe potentially containing a subset of values.
        key_subset (str): the column name in the subset dataframe containing the values to check.
        df_superset (pandas.DataFrame): the dataframe potentially containing a superset of values.
        key_superset (str): the column name in the superset dataframe containing the values to check.
    """
    
    if set(df_subset[key_subset].unique()).issubset(set(df_superset[key_superset].unique())) == True:
        difference = set(df_superset[key_superset].unique()) - set(df_subset[key_subset].unique())
        percentage = round((1-(len(difference)/len(set(df_superset[key_superset].unique()))))*100, 3)
        print(f"True")
        print(f"The percentage of correspondence is: {percentage} %")
    
    else:
        print("False")


def get_set_differences(df_subset, key_subset, df_superset, key_superset):
    """
    Identifies elements that exist in a subset dataframe but not in a superset dataframe, according to the
    specified key columns.
    
    Args:
        df_subset (pandas.DataFrame): the dataframe potentially containing a subset of values.
        key_subset (str): the column name in the subset dataframe containing the values to check.
        df_superset (pandas.DataFrame): the dataframe potentially containing a superset of values.
        key_superset (str): the column name in the superset dataframe containing the values to check.
    """

    return set(df_subset[key_subset]) - set(df_superset[key_superset])