
import json
import pandas as pd


def add_surrogate_key_dimension_table(dimension_table, surrogate_key_column):
    """
    Adds a surrogate key attribute to a dimension table.

    Args:
        dimension_table (pandas.DataFrame): the dimension table to add the surrogate key column to.
        surrogate_key_column (str): The name of the surrogate key column to be added.
    """

    dimension_table.insert(0, surrogate_key_column, range(1, len(dimension_table) + 1))


def add_surrogate_key_fact_table(fact_table, surrogate_key_mapping_file, natural_key_column, surrogate_key_column):
    """
    Adds a surrogate key attribute to a fact table.

    Args:
        fact_table (pandas.DataFrame): the fact table to add the surrogate key column to.
        surrogate_key_mapping_file (str): the name of the file containing the mappings between natural and surrogate
                                          keys.
        natural_key_column (str): name of the column in the fact table containing the natural key.
        surrogate_key_column (str): name of the column in the fact table that will contain the surrogate key.
    """
    
    with open(surrogate_key_mapping_file, 'r') as f:
        surrogate_key_mapping = json.load(f)
    
    fact_table = fact_table.merge(pd.DataFrame(surrogate_key_mapping.items(), 
                                               columns=[natural_key_column, surrogate_key_column]), 
                                               on=natural_key_column)

    fact_table[surrogate_key_column] = fact_table[surrogate_key_column].astype(int)
    fact_table.drop(natural_key_column, axis=1, inplace=True)

    return fact_table


def map_surrogate_to_natural_key(dataframe, natural_key_column, surrogate_key_column):
    """
    Maps the surrogate key values in the dataframe to the corresponding natural key values.

    Args:
        dataframe (pandas.DataFrame): The dataframe containing the surrogate key and natural key columns.
        natural_key_column (str): The name of the natural key column.
        surrogate_key_column (str): The name of the surrogate key column.

    Returns:
        dict: A dictionary mapping surrogate key values to their corresponding natural key values.
    """
    
    surrogate_key_mapping = dict(zip(dataframe[natural_key_column], dataframe[surrogate_key_column]))

    return surrogate_key_mapping


def map_surrogate_to_natural_key_junk_dimension(dataframe, key_columns):
    """
    Maps the natural key values of the junk dimension dataframe to their corresponding surrogate key.

    Args:
        dataframe: The junk dimension dataframe containing the natural key and surrogate key columns.
        key_columns: A list of column names representing the natural key columns.

    Returns:
        A dictionary mapping the concatenated natural key values to their corresponding surrogate key.
    """
    
    junk_key_mapping = {}

    for _, row in dataframe.iterrows():
        key_values = ' + '.join(str(row[col]) for col in key_columns)
        junk_key_mapping_key = row['ORDER_INDICATOR_KEY']
        junk_key_mapping[key_values] = junk_key_mapping_key

    return junk_key_mapping


def save_lookup_to_json(mappings, filename):
    """
    Saves a lookup mapping dictionary to a JSON file.

    Args:
        mappings: the dictionary containing the lookup mapping.
        filename: the name of the JSON file to be saved.
    """
    
    with open(filename, 'w') as file:
        json.dump(mappings, file)