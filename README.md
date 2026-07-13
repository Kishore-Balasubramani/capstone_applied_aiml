# Applied AI & Machine Learning Capstone

## Overview

This repository contains my Applied AI & Machine Learning Capstone project. The project covers the complete machine learning workflow, starting from data preprocessing and exploratory analysis to model development, evaluation, optimization, and finally integrating a Large Language Model (LLM) into a practical application.

The project is divided into four independent parts, with each part focusing on a different stage of the machine learning lifecycle.

---

## Repository Structure

```
Applied-AI-ML-Capstone/
│
├── part1/
├── part2/
├── part3/
└── part4/
```

---

## Part 1 – Data Cleaning and Exploratory Data Analysis

This section focuses on preparing the Ames Housing dataset for machine learning.

Main tasks completed:

- Loaded and explored the dataset
- Handled missing values
- Removed duplicate records
- Identified numerical and categorical features
- Performed descriptive statistical analysis
- Analysed feature distributions and skewness
- Created visualizations using Matplotlib and Seaborn
- Generated the final cleaned dataset for later stages

**Output**

- Cleaned dataset
- Statistical summaries
- Data visualizations

---

## Part 2 – Supervised Machine Learning

In this section, regression and classification models were developed using the cleaned dataset.

Main tasks completed:

- Feature preprocessing
- Train-test split
- Feature scaling
- Linear Regression
- Ridge Regression
- Logistic Regression
- Performance evaluation
- ROC Curve and AUC analysis
- Threshold sensitivity analysis
- Bootstrap confidence interval analysis

**Models Used**

- Linear Regression
- Ridge Regression
- Logistic Regression

---

## Part 3 – Advanced Machine Learning

This section compares multiple machine learning models and builds a reusable ML pipeline.

Main tasks completed:

- Decision Tree
- Controlled Decision Tree
- Gini vs Entropy comparison
- Random Forest
- Gradient Boosting
- Feature importance analysis
- Feature ablation study
- Cross-validation
- Hyperparameter tuning using GridSearchCV
- Learning curve analysis
- Model serialization using Joblib

**Models Used**

- Decision Tree
- Random Forest
- Gradient Boosting
- Logistic Regression

---

## Part 4 – LLM-Based Batch Scoring System

The final section demonstrates the integration of Google's Gemini API into a production-style application.

Main tasks completed:

- Prompt engineering
- Structured JSON generation
- JSON schema validation
- Guardrails for basic PII detection
- Temperature comparison
- Batch processing of housing records
- JSON output generation

**Technologies Used**

- Gemini API
- Python
- JSON Schema
- Prompt Engineering

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- JSON Schema
- Requests
- Python-dotenv
- Google Gemini API

---

## How to Run

Each part of the project is self-contained and includes its own documentation.

Navigate to the required folder and follow the instructions in its README file.

Example:

```bash
cd part2
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the notebook or Python script as instructed in the corresponding README.

---

## Author

**Kishore B**

B.Tech CSE (AI & ML)

SRM Institute of Science and Technology

---

## License

This project was developed as part of an academic capstone assignment for educational purposes.
