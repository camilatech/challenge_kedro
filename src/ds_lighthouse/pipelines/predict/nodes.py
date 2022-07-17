"""
This is a boilerplate pipeline 'predict'
generated using Kedro 0.18.1
"""
import pandas as pd 

def batch_predict(model_artifact, dataset):
    """This function takes a pre-trained model
    and predicts an unknown dataset"""
    predictions = model_artifact.predict(dataset)
    predictions = predictions.round().astype('int64')
    final_predictions = dataset  
    final_predictions['FinalMandates']=predictions
    return final_predictions

def undummify(final_predictions, prefix_sep="_"):
    cols2collapse = {
        item.split(prefix_sep)[0]: (prefix_sep in item) for item in final_predictions.columns
    }
    series_list = []
    for col, needs_to_collapse in cols2collapse.items():
        if needs_to_collapse:
            undummified = (
                final_predictions.filter(like=col)
                .idxmax(axis=1)
                .apply(lambda x: x.split(prefix_sep, maxsplit=1)[1])
                .rename(col)
            )
            series_list.append(undummified)
        else:
            series_list.append(final_predictions[col])
    undummified_predictions = pd.concat(series_list, axis=1)
    return undummified_predictions
