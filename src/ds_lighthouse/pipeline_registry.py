"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline, pipeline
from ds_lighthouse.pipelines import data_processing as dp
from ds_lighthouse.pipelines import data_engineering as de
from ds_lighthouse.pipelines import data_science as ds
from ds_lighthouse.pipelines import predict as pred

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """
    data_processing_pipeline = dp.create_pipeline()
    data_engineering_pipeline = de.create_pipeline()
    data_science_pipeline = ds.create_pipeline()    
    predict_pipeline = pred.create_pipeline()

    return {
        "dp": data_processing_pipeline,
        "de": data_engineering_pipeline,
        "ds": data_science_pipeline,
        "pred": predict_pipeline,
        "__default__": data_processing_pipeline+data_engineering_pipeline+data_science_pipeline+predict_pipeline
    }