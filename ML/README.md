# Pokémon Type Prediction Based on Stats

## Overview
This project builds a machine learning model that predicts the primary type of a Pokémon based on its stats such as HP, Attack, Defense, Special Attack, Special Defense, and Speed. The model is trained using Gradient Boosting (XGBoost) to achieve high accuracy and support complex feature interactions.

## Features
- Data preprocessing to clean and select relevant stats
- Gradient Boosting classifier training and evaluation
- Model persistence: trained model saved to disk for reuse
- Command-line prediction tool: input a Pokémon name to get its predicted type based on stats

## Dataset
https://www.kaggle.com/datasets/rounakbanik/pokemon

Make sure to download and place the dataset at the correct path (`data/pokemon.csv`) or update paths accordingly.

## Setup Instructions

### Prerequisites
- Python 3.8+
- Virtual environment
- Required Python libraries:
  - pandas
  - xgboost
  - scikit-learn
  - joblib

## Usage
### Clean Data
Run fetch_data.py script to clean and format the data for training and prediction.  

```bash
python src/clean_data.py 
```

### Train the Model
Run the train.py script to train the model and saves it in model/ 

```bash
python src/train.py
```

### Predict Type by Pokémon Name
Use the predict.py script. Provide the Pokémon name and it will output the predicted type.

```bash
python src/predict.py
```






