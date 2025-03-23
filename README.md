# Loan Eligibility Prediction Using PCA & KNN

## Overview
This project focuses on predicting loan eligibility using Principal Component Analysis (PCA) for dimensionality reduction and K-Nearest Neighbors (KNN) for classification. The notebook `PCA_KNN_LOAN_ELIGIBLITY_PREDICT.ipynb` contains the full implementation.

## Features
- **Data Preprocessing**: Cleans and prepares the dataset
- **Dimensionality Reduction**: Uses PCA to reduce feature dimensions
- **Machine Learning Model**: Applies KNN for loan eligibility classification
- **Model Evaluation**: Measures accuracy and performance
- **Data Visualization**: Includes graphical insights into the dataset

## Requirements
To run this project, install the required dependencies:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```

## Dataset
The dataset should contain relevant features such as income, credit history, loan amount, and more. Ensure the dataset is preprocessed correctly before running the notebook.

## How to Use
1. Open the `PCA_KNN_LOAN_ELIGIBLITY_PREDICT.ipynb` notebook.
2. Load the dataset and perform exploratory data analysis (EDA).
3. Apply PCA for dimensionality reduction.
4. Train the KNN model using the reduced dataset.
5. Evaluate the model's accuracy and test it on new data.

## Model Workflow
- **Step 1**: Load and clean the dataset
- **Step 2**: Apply PCA to extract key features
- **Step 3**: Train a KNN model for classification
- **Step 4**: Evaluate model performance using accuracy metrics

## Results
The model's effectiveness is evaluated using accuracy, precision, recall, and F1-score. Visualization of results is included in the notebook.

## Future Improvements
- Experiment with different classifiers (e.g., Random Forest, SVM)
- Optimize PCA parameters for better feature extraction
- Deploy the model as a web application

## License
This project is open-source and can be modified as needed. Ensure proper citation if used in research or commercial projects.

## Author
Developed by Arnab Chakraborty

