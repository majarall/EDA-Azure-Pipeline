# EDA - Azure - Pipeline 

This README provides an overview of the tasks and requirements for a machine learning project conducted in the Azure ML environment. The project consists of two main tasks: Task 1, which involves developing a regression model, and Task 2, which focuses on operationalizing the model in Azure ML. Below are detailed instructions and expectations for each task.

### Task 1: Develop a Regression Model
Dataset
You are provided with a dataset (See attached data file).

Objectives
Your primary objective in Task 1 is to develop a regression model that can accurately predict a target variable based on the features in the dataset. The model's performance will be evaluated based on Mean Absolute Error (MAE).

Steps
Exploratory Data Analysis (EDA):

Begin by conducting exploratory data analysis to understand the dataset. You should explore data distribution, correlations, missing values, and any other relevant statistics.
Document your findings and insights from EDA in a Jupyter Notebook.
Model Development:

Use the insights gained from EDA to guide your choice of regression model and preprocessing techniques.
Implement and train your regression model.
Document your model development process, including model selection, hyperparameter tuning, and feature engineering, in a Jupyter Notebook.
Evaluation:

Evaluate the performance of your model using suitable metrics (you are free to choose other metrics, but MAE will be the final score).
Iterate over the model development and evaluation cycle as needed to improve performance.
Presentation:


### Task 2: Operationalize the Model in Azure ML
Requirements
Model Deployment:

Deploy your trained regression model as an HTTP REST endpoint.
Demonstrate an interaction with the endpoint using Python or Jupyter Notebook within the Azure ML workspace environment. No public IP is required.
Training Script:

Create a training script following best practices for instrumentation and logging using MLFlow.
Test Script (Scoring Script):

Create a test script (scoring script) to test the trained model.
Note: Due to the dataset's size, you are allowed to use the same data for both testing and validation. Be sure to explain why this might be a suboptimal practice.
AML Pipelines:

Create an Azure Machine Learning (AML) pipeline (scripts or components) to perform model training.
Create an AML pipeline (scripts or components) to test the model.
Automation:

Demonstrate or discuss how you would automate (schedule) model training, testing, and deployment of a newly trained model, including when to push the model to the Azure Model Registry.
Considerations:

Conclusion
This project encompasses the development of a regression model, deployment as an API, and automation of key processes within the Azure ML framework. Task 1 lays the foundation for model development and evaluation, while Task 2 focuses on making the model operational and scalable.
