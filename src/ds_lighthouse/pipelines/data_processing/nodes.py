"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.1
"""
import pandas as pd 

def preprocess_election_data (election_data_database: pd.DataFrame) -> pd.DataFrame:
    """Preprocesses the data for election_data.

    Args:
        election_data: Raw data.
    Returns:
        Preprocessed data with:
           blanck and null votes columns deleted, 
           also the roll "Territory Nacional" as it is a agreggation of all other rows.
    """      
    not_needed = ['time','blankVotes',  'pre.blankVotes', 'nullVotes',  'pre.nullVotes', 'pre.nullVotesPercentage', 'blankVotesPercentage', 'pre.blankVotesPercentage']
    election_data_database.drop(columns = not_needed, inplace = True) 
    election_data_database = election_data_database[election_data_database["territoryName"]=="Lisboa"]
    election_data_database.drop(columns = ["territoryName"], inplace = True)     
    return election_data_database