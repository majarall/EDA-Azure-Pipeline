# EDA - Azure - Pipeline

## Overview

This README provides a detailed overview of a machine learning project conducted in the Azure ML environment. The project comprises two primary tasks: Task 1, which involves the development of a regression model, and Task 2, which centers on the operationalization of the model within Azure ML. The tasks are executed in two Jupyter Notebooks: Task1.ipynb and Azure/Task2.ipynb.

---

## Task 1: Develop a Regression Model

### Dataset

- You are provided with a dataset (refer to the attached data file).

### Objectives

- In Task 1, your primary objective is to develop a regression model capable of accurately predicting a target variable based on the features within the dataset. The evaluation of your model's performance will be based on the Mean Absolute Error (MAE).

### Steps

1. **Exploratory Data Analysis (EDA)**:
   - Begin by conducting exploratory data analysis to gain a comprehensive understanding of the dataset. Key aspects to explore include data distribution, correlations, missing values, and other pertinent statistics.
   - Document your findings and insights from the EDA in a Jupyter Notebook.

2. **Model Development**:
   - Leverage the insights gleaned from the EDA to inform your choice of regression model and preprocessing techniques.
   - Implement and train your regression model.
   - Document your model development process, encompassing model selection, hyperparameter tuning, and feature engineering, within a Jupyter Notebook.

3. **Evaluation**:
   - Assess your model's performance using appropriate metrics (you have the freedom to choose metrics, but MAE will be the final score).
   - Iterate over the model development and evaluation cycle as needed to enhance performance.

### Presentation

- Present your results from Task 1 in a Jupyter Notebook. This presentation should encompass code, visualizations, and explanations of your approach.

---

## Task 2: Operationalize the Model in Azure ML

### Requirements

1. **Model Deployment**:
   - Deploy your trained regression model as an HTTP REST endpoint.
   - Demonstrate an interaction with the endpoint using Python or Jupyter Notebook within the Azure ML workspace environment. No public IP is required.

2. **Training Script**:
   - Develop a training script adhering to best practices for instrumentation and logging using MLFlow.

3. **Test Script (Scoring Script)**:
   - Create a test script (scoring script) for testing the trained model.
   - Note: Due to the dataset's size, you are allowed to use the same data for both testing and validation. Ensure to explain why this approach may not be optimal.

4. **AML Pipelines**:
   - Establish an Azure Machine Learning (AML) pipeline (scripts or components) for model training.
   - Create an AML pipeline (scripts or components) for testing the model.

5. **Automation**:
   - Demonstrate or discuss how you would automate (schedule) model training, testing, and deployment of a newly trained model, including when to push the model to the Azure Model Registry.

6. **Considerations**:
   - Address any additional considerations that you deem important within the context of the Azure ML project.

### Conclusion

- This project encompasses the development of a regression model, deployment as an API, and automation of critical processes within the Azure ML framework. Task 1 forms the foundation for model development and evaluation, while Task 2 focuses on making the model operational and scalable.
