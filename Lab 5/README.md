# DS605 Lab 5: Linear and Logistic Regression

## Overview

This project implements and compares **Linear Regression and Logistic Regression** using two approaches:

1. **Scikit-learn:** Using built-in machine learning models and preprocessing tools.
2. **From Scratch:** Implementing the core algorithms using NumPy and Pandas to understand their mathematical operations.

The project uses the Garment Worker Productivity dataset to predict workers' productivity and classify whether their actual productivity meets the targeted productivity.

It also explores optimization techniques for Logistic Regression by experimenting with different learning rates and numbers of iterations.

## Objectives

- Inspect and understand the dataset.
- Handle missing values and preprocess numerical and categorical features.
- Create a fixed training and testing split.
- Implement Linear Regression using Scikit-learn and the least-squares solution from scratch.
- Implement Logistic Regression using Scikit-learn and gradient descent from scratch.
- Evaluate regression and classification models using appropriate metrics.
- Compare model performance and execution time.
- Optimize the manual Logistic Regression model to reduce training time while maintaining predictive performance.

## Dataset

**Dataset name:** Garment Worker Productivity

**File:** `data/garments_worker_productivity.csv`

The dataset contains **1,197 records** and includes information about garment production teams, working conditions, and productivity.

### Important attributes

| Attribute | Description |
|---|---|
| `quarter` | Quarter of the year |
| `department` | Production department |
| `day` | Day of the week |
| `team` | Team identifier |
| `targeted_productivity` | Expected productivity target |
| `smv` | Standard Minute Value |
| `wip` | Work in progress |
| `over_time` | Overtime worked |
| `incentive` | Incentive amount |
| `idle_time` | Time spent idle |
| `idle_men` | Number of idle workers |
| `no_of_style_change` | Number of style changes |
| `no_of_workers` | Number of workers |
| `actual_productivity` | Actual productivity achieved |

### Prediction targets

The notebook solves two machine learning tasks.

**1. Regression**

Predict the continuous value of `actual_productivity`.

**2. Binary classification**

Create a new target called `MeetsTarget`:

- `1`: Actual productivity is greater than or equal to targeted productivity.
- `0`: Actual productivity is below targeted productivity.

The `date` column is excluded from the predictor features.

## Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- Jupyter Notebook
- Python `time` module for measuring execution time

## Project Workflow

### 1. Data inspection

- Load the dataset.
- Examine the first few rows and column names.
- Check data types, missing values, duplicate records, and numerical summaries.

### 2. Data preprocessing

The Scikit-learn implementation uses preprocessing pipelines.

**Numerical features:**
- Replace missing values with the median.
- Standardize features using `StandardScaler`.

**Categorical features:**
- Replace missing values with the most frequent value.
- Apply one-hot encoding.

A `ColumnTransformer` combines both preprocessing pipelines. The preprocessing steps are fitted using training data to avoid information leakage from the test set.

### 3. Train-test split

The notebook uses a fixed 80:20 training and testing split with `random_state=42`.

- Training records: 957
- Testing records: 240

Both regression and classification use the same split to make the comparison consistent.

### 4. Scikit-learn implementation

The notebook trains and evaluates:

- `LinearRegression` for predicting actual productivity.
- `LogisticRegression` for predicting whether the productivity target is met.

Training time, prediction time, and evaluation metrics are recorded.

### 5. From-scratch implementation

The same tasks are implemented using NumPy and Pandas.

**Linear Regression**
- Adds an intercept term.
- Calculates regression coefficients using the Moore–Penrose pseudoinverse.
- Generates predictions and manually calculates MAE, RMSE, and R².

**Logistic Regression**
- Uses the sigmoid function to calculate probabilities.
- Uses binary cross-entropy as the loss function.
- Applies batch gradient descent to update model weights.
- Uses a threshold of 0.5 to convert probabilities into binary predictions.
- Manually calculates accuracy, precision, recall, and F1-score.

### 6. Model comparison

The results from Scikit-learn and the from-scratch implementations are compared using the same train-test split and equivalent preprocessing.

The notebook evaluates predictive performance and computational efficiency.

### 7. Optimization

The manual Logistic Regression model is optimized by experimenting with different learning rates:

`0.01, 0.03, 0.05, 0.1`

It also evaluates different iteration counts to understand the effect of gradient descent on convergence, training time, and test-set performance.

The final optimized configuration uses:

- Learning rate: `0.1`
- Number of iterations: `1,000`

## Evaluation Metrics

### Regression metrics

| Metric | Purpose |
|---|---|
| MAE | Measures the average absolute prediction error |
| RMSE | Measures prediction error while penalizing larger errors more heavily |
| R² | Measures how much variation in the target is explained by the model |

### Classification metrics

| Metric | Purpose |
|---|---|
| Accuracy | Proportion of correct predictions |
| Precision | Proportion of positive predictions that are correct |
| Recall | Proportion of actual positive cases correctly identified |
| F1-score | Harmonic mean of precision and recall |

The notebook also measures training and prediction time in seconds.

## Results

### Regression

Both implementations produced essentially identical regression results.

| Metric | Result |
|---|---:|
| MAE | 0.108453 |
| RMSE | 0.148618 |
| R² | 0.168168 |

These results demonstrate that the from-scratch least-squares implementation reproduces the Scikit-learn model's predictive results on the same processed data and split.

### Classification

The baseline from-scratch Logistic Regression achieved the following results:

| Metric | Result |
|---|---:|
| Accuracy | 0.775000 |
| Precision | 0.778281 |
| Recall | 0.971751 |
| F1-score | 0.864322 |

The from-scratch and Scikit-learn implementations showed similar classification performance.

### Optimization results

| Parameter | Baseline | Optimized |
|---|---:|---:|
| Learning rate | 0.01 | 0.1 |
| Iterations | 10,000 | 1,000 |
| F1-score | 0.864322 | 0.864322 |
| Training-time reduction | — | 88.09% |

The optimized configuration reduced the manual Logistic Regression training time by approximately **88.09%** while maintaining the same observed test-set F1-score.

## Installation

Install the required libraries:

```bash
pip install numpy pandas matplotlib scikit-learn jupyter
```

## How to Run

1. Download or clone the project files.
2. Ensure the dataset is located at `data/garments_worker_productivity.csv`.
3. Open the notebook `202618058_Lab5.ipynb` in Jupyter Notebook or JupyterLab.
4. Install the required dependencies.
5. Run the notebook cells sequentially, from initialization through the final results and conclusion.

If the dataset is stored elsewhere, update the CSV file path in the data-loading cell.

## Conclusion

This project demonstrates the implementation of regression and classification using both Scikit-learn and NumPy/Pandas from scratch.

The Linear Regression implementations produced equivalent predictive metrics, validating the manual least-squares calculation. The Logistic Regression implementation demonstrated how sigmoid activation, binary cross-entropy, and gradient descent work together to solve a binary classification problem.

Finally, learning-rate and iteration experiments showed that the manual Logistic Regression model could reduce training time by approximately 88.09% while preserving its observed test-set F1-score.

Overall, the project provides practical experience with data preprocessing, supervised learning, model evaluation, algorithm implementation, and optimization.