"""
This is a boilerplate pipeline 'predict'
generated using Kedro 0.18.1
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import batch_predict,undummify

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
            node(
                func=batch_predict,
                inputs=['linear_regression', 'validate'],
                name='batch_predict',
                outputs='final_predictions'
            ),
            node(
                func=undummify,
                inputs=['final_predictions'],
                name='undummify',
                outputs='undummified_final_predictions'
            )   
    ])
