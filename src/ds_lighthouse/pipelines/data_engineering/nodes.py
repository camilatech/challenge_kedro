"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.18.1
"""
import pandas as pd 

def election_features (pp_election_data: pd.DataFrame) -> pd.DataFrame:
    """Preprocesses the data for votes.

    Args:
        election_data: Preprocessed data.
    Returns:
        One hot encoded data with:
          dummies to represent the Party.
    """
    election_features = pd.get_dummies(pp_election_data)
    return election_features    