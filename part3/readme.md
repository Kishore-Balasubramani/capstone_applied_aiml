# Part 3 – Advanced Modeling, Hyperparameter Tuning and Machine Learning Pipeline

## Overview

In this part of the capstone project, I experimented with different ensemble learning techniques and compared their performance with the models developed in Part 2. I also performed hyperparameter tuning using Grid Search, created a complete machine learning pipeline, evaluated the models using cross-validation, and saved the best-performing model for future use.

---

## Dataset

The cleaned dataset generated in Part 1 was used throughout this notebook.

- **Target Variable:** Binary house price class
- **Class 0:** SalePrice less than or equal to the median
- **Class 1:** SalePrice greater than the median

The same preprocessing approach from Part 2 was followed before training the models.

---

## Data Preprocessing

Before training the models, the following preprocessing steps were carried out:

- Loaded the cleaned dataset.
- Converted categorical variables using one-hot encoding.
- Split the dataset into training and testing sets.
- Applied feature scaling using StandardScaler.
- Used the same train-test split for all models to ensure fair comparison.

---

## Decision Tree Models

Two Decision Tree models were trained.

### Default Decision Tree

The first model was trained using the default parameters.

The training accuracy was noticeably higher than the testing accuracy, indicating that the model tends to overfit the training data. Decision Trees are considered high-variance models because they make greedy decisions at every split and can easily memorize patterns that do not generalize well to unseen data.

### Controlled Decision Tree

The second Decision Tree used:

- max_depth = 5
- min_samples_split = 20

Limiting the depth of the tree reduces overfitting by preventing the model from learning unnecessary details from the training data. Increasing the minimum number of samples required for a split also helps avoid creating branches based on very small subsets of the data.

Compared with the default tree, the controlled tree produced a smaller gap between training and testing accuracy, suggesting better generalization.

---

## Gini vs Entropy

Two Decision Tree models were compared using different impurity measures.

### Gini Impurity

\[
Gini = 1 - \sum p_i^2
\]

### Entropy

\[
Entropy = -\sum p_i \log_2(p_i)
\]

A Gini value of **0** means that every sample in a node belongs to the same class, making it a perfectly pure node.

Both impurity measures produced similar performance, with only small differences in test accuracy.

---

## Random Forest

A Random Forest classifier was trained using:

- 100 Decision Trees
- Maximum depth of 10

The model was evaluated using:

- Training Accuracy
- Testing Accuracy
- ROC-AUC Score

The five most important features were identified using the model's feature importance scores.

Unlike Linear Regression coefficients, Random Forest feature importance measures how much each feature reduces impurity across all trees in the forest rather than measuring a direct positive or negative relationship with the target.

---

## Bagging

Random Forest improves performance by combining many Decision Trees.

Each tree is trained using a bootstrap sample, meaning that the training data is sampled with replacement.

Additionally, every split considers only a random subset of the available features.

This combination reduces variance and makes the model much more stable than a single Decision Tree.

---

## Gradient Boosting

Gradient Boosting was also trained and compared with the other models.

Unlike Random Forest, Gradient Boosting builds trees sequentially. Each new tree focuses on correcting the mistakes made by the previous trees, allowing the model to gradually improve its predictions.

The model was evaluated using:

- Training Accuracy
- Testing Accuracy
- ROC-AUC

---

## Feature Ablation Study

To determine whether every feature contributed to prediction performance, the five least important features identified by the Random Forest model were removed.

A second Random Forest model was trained using the reduced feature set.

The ROC-AUC scores of the full model and the reduced model were compared.

If the reduced model performs similarly, the removed features were likely contributing very little useful information. A simpler model can reduce computation time and maintenance effort without significantly affecting predictive performance.

---

## Cross Validation

Five-fold Stratified Cross Validation was performed for the following models:

- Logistic Regression
- Controlled Decision Tree
- Random Forest
- Gradient Boosting

The average ROC-AUC and standard deviation were calculated for every model.

Cross-validation provides a more reliable estimate of model performance than a single train-test split because every observation is used for both training and validation across different folds.

---

## Hyperparameter Tuning

A complete machine learning pipeline was created using:

- Median Imputation
- StandardScaler
- Random Forest Classifier

GridSearchCV was used to search for the best combination of:

- Number of Trees
- Maximum Tree Depth
- Minimum Samples per Leaf

A total of **90 model fits** were evaluated:

- 18 parameter combinations
- 5 cross-validation folds

Grid Search evaluates every possible parameter combination, while Randomized Search evaluates only a subset, making it faster for very large search spaces.

---

## Manual Learning Curve

The best pipeline obtained from Grid Search was trained using five different training set sizes:

- 20%
- 40%
- 60%
- 80%
- 100%

For every training size, both the training ROC-AUC and testing ROC-AUC were calculated.

As more training data becomes available, the training performance usually decreases slightly while the testing performance becomes more stable. This helps determine whether the model would benefit from collecting additional data.

---

## Model Serialization

The best pipeline was saved using Joblib as:

```
best_model.pkl
```

The saved model was successfully reloaded and used to generate predictions for two sample observations without retraining.

This demonstrates that the trained model can be reused later in production.

---

## Final Model Comparison

All models were compared using:

- 5-Fold Mean ROC-AUC
- 5-Fold Standard Deviation
- Test ROC-AUC

The ensemble models consistently performed better than a single Decision Tree.

Among all models, the Random Forest (or the model with the highest ROC-AUC in your results) provided the best balance between predictive performance and generalization. Based on these results, it would be the recommended model for deployment because it achieved strong performance while remaining relatively robust against overfitting.

---

## Files Included

- part3_advanced_modeling.ipynb
- cleaned_data.csv
- best_model.pkl
- README.md
- requirements.txt
- plots/

---

## Requirements

Install the required libraries using:

```bash
pip install -r requirements.txt
```

---

## Running the Notebook

1. Open the notebook.
2. Upload `cleaned_data.csv` when prompted.
3. Run all cells from top to bottom.

The notebook will:

- Train Decision Tree models
- Train Random Forest and Gradient Boosting models
- Compare feature importance
- Perform cross-validation
- Tune hyperparameters using Grid Search
- Save the best model
- Reload the saved model
- Generate predictions on sample observations