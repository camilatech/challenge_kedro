"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.18.1
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import election_features

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node (
                func=election_features,
                inputs=['preprocess_election_data'],
                outputs='election_features',
                name='election_features_node'
            ),
    ])
