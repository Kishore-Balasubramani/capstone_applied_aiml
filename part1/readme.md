# Part 1 – Data Acquisition, Cleaning and Exploratory Data Analysis

## Overview

In this part of the project, I worked on cleaning and exploring the Ames Housing dataset before building any machine learning models. The main objective was to understand the dataset, identify data quality issues, perform exploratory analysis, and prepare a clean dataset that can be used in the next part of the capstone.

---

## Dataset

I used the **Ames Housing Dataset**, which contains information about residential properties sold in Ames, Iowa. The dataset includes both numerical and categorical features such as house size, neighborhood, construction quality, and sale price.

I chose this dataset because it has enough rows and columns, contains missing values, different data types, and a numerical target variable (SalePrice), making it suitable for this project.

---

## What I Did

### Loading the Dataset

- Loaded the dataset using pandas.
- Displayed the first five rows.
- Checked the data types of all columns.
- Verified the number of rows and columns.

### Missing Value Analysis

- Calculated the number and percentage of missing values in every column.
- Identified columns with more than 20% missing values.
- Filled missing values in eligible numerical columns using the median.

I used the **median** instead of the mean because some numerical features are highly skewed, and the median is less affected by extreme values.

### Duplicate Records

- Checked for duplicate rows.
- Removed duplicates if any were found.
- Compared the dataset before and after removing duplicates.

### Data Type Correction

- Converted **MS SubClass** to the `category` data type since it represents categories rather than continuous values.
- Converted **Neighborhood** to the `category` data type to reduce memory usage.
- Compared memory usage before and after the conversion.

### Descriptive Statistics

Generated summary statistics for all numerical columns to understand the overall distribution of the data.

### Skewness Analysis

Calculated the skewness of every numerical feature and identified the most skewed column.

A positive skew means that a few very large values pull the distribution to the right, while a negative skew means that a few very small values pull it to the left. In both situations, the median usually represents the center of the data better than the mean.

### Outlier Detection

Used the IQR method to identify outliers in two numerical columns.

The outliers were not removed because they may represent genuine expensive or unusually large houses. I will decide how to handle them during model building in Part 2.

---

## Visualizations

The following plots were created during the analysis:

- Line Plot
- Bar Chart
- Histogram
- Scatter Plot
- Box Plot
- Correlation Heatmap

All plots are saved in the **plots** folder.

---

## Correlation Analysis

Computed the Pearson correlation matrix and visualized it using a heatmap.

The strongest correlated variables were identified. Although two variables may have a strong correlation, it does not necessarily mean one causes the other. Other factors such as house size, location, or construction quality may influence both variables.

---

## Mean vs Median Comparison

Compared the mean and median of the two most skewed numerical columns before performing imputation.

Based on the skewness, the median was chosen because it provides a more reliable estimate of the center when extreme values are present.

---

## Spearman Correlation

Calculated the Spearman correlation matrix and compared it with the Pearson correlation matrix.

This helped identify relationships that are monotonic but not perfectly linear. The comparison will be useful when selecting features for the machine learning models in Part 2.

---

## Grouped Aggregation

Grouped the data using a categorical feature and calculated the mean, standard deviation, and count for a numerical feature.

The results helped understand how different categories vary and whether the categorical feature may be useful for prediction.

---

## Output

The cleaned dataset was saved as:

`cleaned_data.csv`

This file will be used in Part 2 of the project.

---

## Files Included

- `part1_data_cleaning_eda.ipynb`
- `README.md`
- `requirements.txt`
- `AmesHousing.csv`
- `cleaned_data.csv`
- `plots/`

---

## Requirements

Install the required libraries using:

```bash
pip install -r requirements.txt
```

---

## Running the Notebook

Open the notebook and run all the cells from top to bottom.

The notebook will:
- Load the dataset
- Clean the data
- Perform exploratory data analysis
- Generate all required plots
- Save the cleaned dataset