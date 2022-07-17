# MLOps Challenge

## Overview

This is Kedro project, which was generated using `Kedro 0.18.1`.

Take a look at the [Kedro documentation](https://kedro.readthedocs.io) to get started.

## Goals

The outcome of this project is a prediction of the winner Party in Portugal's 2019 election in Lisboa.
This machine leaning project uses the framework Kedro to mantain the MLOps best pratices.

## Data

The only data filed in this repository is in: data/01_raw
It's "Real-time Election Results: Portugal 2019 Data Set" available in UCI archives.

## How to install dependencies

Declare any dependencies in `src/requirements.txt` for `pip` installation and `src/environment.yml` for `conda` installation.

To install them, run:

```
pip install -r src/requirements.txt
```

## How to run your Kedro pipeline and obtain the Predictions

You can run this Kedro project with:

```
kedro run
```

With this step, you will generate the files need to obtain the predictions.
The final prediction is in: data/07_model_output
The CSV file of the final prediction: undummified_final_predictions

## How to work with Kedro and notebooks

> Note: Using `kedro jupyter` or `kedro ipython` to run your notebook provides these variables in scope: `context`, `catalog`, and `startup_error`.
>
> Jupyter, JupyterLab, and IPython are already included in the project requirements by default, so once you have run `pip install -r src/requirements.txt` you will not need to take any extra steps before you use them.

### JupyterLab
You can start JupyterLab:

```
kedro jupyter lab
```

### IPython
And if you want to run an IPython session:

```
kedro ipython
```
