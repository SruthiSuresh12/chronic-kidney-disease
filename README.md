# Chronic Kidney Disease Prediction

## Overview

This project uses machine learning to predict the presence of chronic kidney disease (CKD) based on patient data. The workflow includes data loading, cleaning, exploratory analysis, feature engineering, model training, evaluation, and prediction. The goal is to build a robust classifier to assist in early detection of CKD, improving patient outcomes and supporting clinical decision-making.

## Features

- Data preprocessing and cleaning
- Exploratory data analysis (EDA)
- Feature selection and engineering
- Multiple machine learning models (e.g., Logistic Regression, Random Forest, SVM)
- Model evaluation using accuracy, precision, recall, F1-score, ROC-AUC
- Visualization of results
- Predictive function for new patient data

## Requirements

- Python 3.7+
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn
- jupyter

Install dependencies:
```bash
pip install pandas numpy scikit-learn matplotlib seaborn jupyter
```

## Usage

### 1. Open the Notebook

Launch Jupyter Notebook and open `Main-Code.ipynb`.

### 2. Data Preparation

- The notebook loads a CKD dataset (CSV format).
- Missing values are handled, and categorical variables are encoded.

### 3. Exploratory Data Analysis

- Visualizations and statistics summarize feature distributions and relationships.
- Correlation analysis identifies important predictors.

### 4. Feature Engineering

- Features are selected based on domain knowledge and correlation.
- Data is split into training and testing sets.

### 5. Model Training

- Several classifiers are trained and compared, such as Logistic Regression, Random Forest, and SVM.
- Hyperparameters are tuned for optimal performance.

### 6. Model Evaluation

- Models are evaluated using accuracy, confusion matrix, precision, recall, F1-score, and ROC curves.
- The best-performing model is selected for deployment.

### 7. Prediction

- The notebook includes a function to predict CKD status for new patient data.

## File Structure

| File/Folder               | Purpose                                 |
|---------------------------|-----------------------------------------|
| Main-Code.ipynb           | Main Jupyter notebook with all steps    |
| data/                     | (Optional) Folder for dataset files     |
| README.md                 | Project documentation                   |

## How to Use

1. Clone the repository.
2. Ensure all dependencies are installed.
3. Place the CKD dataset in the appropriate directory if not already present.
4. Run the notebook cell by cell, following the explanations and outputs.
5. Use the final prediction function to test with new patient data.

## Project Flow

1. **Load and inspect data**
2. **Clean and preprocess features**
3. **Visualize and analyze data**
4. **Select and engineer features**
5. **Train and evaluate multiple models**
6. **Select best model**
7. **Predict CKD for new cases**

## Notes

- The project is intended for educational and research purposes.
- Predictions should not be used for clinical decision-making without further validation.
- The approach can be extended to other medical datasets with similar structure.

## References

- UCI Machine Learning Repository: Chronic Kidney Disease Dataset
- Standard machine learning literature on CKD prediction
