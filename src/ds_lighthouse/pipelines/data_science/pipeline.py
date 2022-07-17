"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.1
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import slip_data, fit_model


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node (
                func=slip_data,
                inputs=['election_features'],
                outputs=['X_train', 'X_test', 'y_train', 'y_test'],
                name='slip_data_node'
        ),
        node(
                func=fit_model,
                inputs=['X_train', 'X_test', 'y_train', 'y_test'],
                outputs='linear_regression',
                name='fit_model_node'
        )
    ])

