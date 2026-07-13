# Part 2 – Supervised Machine Learning

## Overview

In this part of the capstone, I built and evaluated both regression and classification models using the cleaned Ames Housing dataset from Part 1. Before training the models, the data was preprocessed by encoding categorical variables, splitting the dataset into training and testing sets, and applying feature scaling using StandardScaler.

---

## Dataset

The cleaned dataset generated in Part 1 was used as the input for all machine learning models.

- **Regression Target:** `SalePrice`
- **Classification Target:** A binary label created by comparing each house's sale price with the median sale price.
  - **Class 0:** SalePrice ≤ Median
  - **Class 1:** SalePrice > Median

---

## Data Preprocessing

The following preprocessing steps were performed before training the models:

- Loaded the cleaned dataset.
- Separated features and target variables.
- Converted categorical variables using one-hot encoding.
- Split the data into training and testing sets (80:20).
- Applied StandardScaler using only the training data to prevent data leakage.

Fitting the scaler only on the training data ensures that information from the test set does not influence the training process. Using the entire dataset for scaling would leak test-set statistics into the model and produce overly optimistic evaluation results.

---

## Regression Models

Two regression models were trained:

- Linear Regression
- Ridge Regression (alpha = 1.0)

The models were evaluated using:

- Mean Squared Error (MSE)
- R² Score

### Important Features

The three features with the largest absolute coefficient values were:

| Feature | Coefficient |
|---------|------------:|
| BsmtFin SF 1 | 133328.90 |
| Bsmt Unf SF | 120065.28 |
| Total Bsmt SF | -112078.08 |

### Interpretation

**BsmtFin SF 1** has the largest positive coefficient, indicating that houses with more finished basement area tend to have higher predicted sale prices when other features remain constant.

**Bsmt Unf SF** also has a strong positive coefficient. This suggests that additional unfinished basement space still contributes positively to the predicted house value, although its impact is slightly lower than finished basement area.

**Total Bsmt SF** has a large negative coefficient in the multiple regression model. Since this variable is highly correlated with other basement-related features, the negative value is most likely caused by multicollinearity rather than implying that larger basements reduce house prices. Ridge Regression helps reduce the effect of this multicollinearity by shrinking coefficient values.

---

## Ridge Regression

Ridge Regression was trained using an alpha value of **1.0** and compared with ordinary Linear Regression.

Unlike Linear Regression, Ridge Regression applies L2 regularization, which reduces the magnitude of model coefficients and helps improve stability when predictor variables are highly correlated.

The alpha parameter controls the strength of the regularization. Larger alpha values apply stronger penalties to large coefficients, while smaller values behave more like ordinary Linear Regression.

---

## Classification Model

The classification task predicts whether a house price is above or below the median sale price.

The Logistic Regression model was evaluated using:

- Confusion Matrix
- Accuracy
- Precision
- Recall
- F1 Score
- ROC Curve
- AUC Score

The class distribution was checked before training. If an imbalance was detected, Logistic Regression was trained using `class_weight="balanced"` to reduce the bias toward the majority class.

---

## Precision and Recall

The evaluation metrics are defined as:

**Precision**

\[
Precision = \frac{TP}{TP + FP}
\]

Precision measures how many of the houses predicted as high-priced actually belong to the high-priced class.

**Recall**

\[
Recall = \frac{TP}{TP + FN}
\]

Recall measures how many of the actual high-priced houses were correctly identified by the model.

For this classification task, recall is slightly more important because failing to identify a genuinely high-priced property (false negative) may be more costly than incorrectly predicting a property as high-priced.

---

## ROC Curve and AUC

The ROC curve illustrates the trade-off between the True Positive Rate and the False Positive Rate across different decision thresholds.

The AUC score summarizes this performance into a single value.

An AUC value closer to **1.0** indicates that the model can effectively distinguish between the two classes, while a value near **0.5** suggests performance similar to random guessing.

---

## Decision Threshold Analysis

The default classification threshold of **0.50** was compared with thresholds ranging from **0.30 to 0.70**.

For each threshold, Precision, Recall and F1-score were calculated to understand how changing the decision threshold affects model performance.

The threshold with the highest F1-score was selected as the best balance between precision and recall for this dataset.

Increasing the threshold generally improves precision but reduces recall, while lowering the threshold increases recall at the cost of more false positives.

---

## Logistic Regression Regularization

A second Logistic Regression model was trained using **C = 0.01**.

The value of **C** controls the amount of regularization.

- Smaller C → Stronger regularization
- Larger C → Weaker regularization

The baseline model (C = 1.0) and the regularized model (C = 0.01) were compared using Precision, Recall and AUC to evaluate the impact of stronger regularization.

---

## Bootstrap Confidence Interval

To measure the reliability of the difference between the two Logistic Regression models, a bootstrap experiment with **500 samples** was performed.

For each bootstrap sample:

- The test set was sampled with replacement.
- The AUC of both models was calculated.
- The difference in AUC was recorded.

Finally, the following statistics were reported:

- Mean AUC Difference
- 2.5th Percentile
- 97.5th Percentile

If the 95% confidence interval excludes zero, the performance difference between the two models is considered statistically reliable. Otherwise, the observed difference may simply be due to sampling variability.

---

## Files Included

- part2_supervised_machine_learning.ipynb
- cleaned_data.csv
- README.md
- requirements.txt

---

## Requirements

Install all required libraries using:

```bash
pip install -r requirements.txt
```

---

## Running the Notebook

Open the notebook and run all cells from top to bottom.

The notebook will:

- Load the cleaned dataset
- Preprocess the data
- Train regression and classification models
- Evaluate model performance
- Generate the ROC curve
- Compare regularization techniques
- Perform bootstrap analysis