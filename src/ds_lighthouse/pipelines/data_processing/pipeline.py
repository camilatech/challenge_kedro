"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.1
"""

from kedro.pipeline import Pipeline, node, pipeline
from ds_lighthouse.pipelines.data_processing.nodes import preprocess_election_data

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node (
                func=preprocess_election_data,
                inputs=['election_data_database'],
                outputs='preprocess_election_data',
                name='preprocess_election_data_node'
            ),
    ])
