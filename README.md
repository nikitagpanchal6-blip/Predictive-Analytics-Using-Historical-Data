# Predictive-Analytics-Project

## Overview

This project demonstrates a simple predictive analytics workflow for sales forecasting using a linear regression model.

The notebook `notebook/prediction.ipynb` loads a sales dataset from `data/train.csv`, converts time into a numeric feature, trains a model, evaluates accuracy, and plots sales predictions.

## Project Structure

* `data/` - contains the dataset used for training and prediction.
* `notebook/prediction.ipynb` - main analysis notebook with data loading, preprocessing, model training, evaluation, and visualization.
* `output/README.md` - project documentation and usage instructions.

## Key Steps

1. Load the sales dataset from `data/train.csv`.
2. Convert the `Month` column into a numerical feature.
3. Split the data into training and testing sets.
4. Train a `LinearRegression` model from scikit-learn.
5. Evaluate model accuracy using the test set.
6. Visualize actual vs. predicted sales.
7. Predict future sales for a future date.

## Requirements

* Python 3.8+ (recommended)
* pandas
* matplotlib
* scikit-learn

## Usage

1. Open `notebook/prediction.ipynb` in Jupyter Notebook or JupyterLab.
2. Run the notebook cells sequentially.
3. Review the model accuracy output and sales prediction plot.

## Notes

* The current notebook uses `Month` as the only feature.
* The model predicts sales based on the linear trend in historical data.
* For better accuracy, consider adding more features, using time-series methods, or testing other regression models.

