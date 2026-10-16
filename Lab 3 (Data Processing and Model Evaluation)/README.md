# Hotel Booking Cancellation Prediction

## Overview
This project focuses on predicting whether a hotel booking will be canceled using machine learning classification models. The project uses the Hotel Bookings dataset and explores data preprocessing, missing-value handling, feature encoding, scaling, model training, and evaluation.

Two classification algorithms are compared:
- Logistic Regression
- Decision Tree Classifier

The models are evaluated using training accuracy, testing accuracy, precision, recall, F1-score, and confusion matrices.

## Dataset
The project uses the `hotel_bookings.csv` dataset.

- **Total records:** 119,390
- **Original features:** 32
- **Target variable:** `is_canceled`
  - `0` — Booking not canceled
  - `1` — Booking canceled

The dataset includes information about hotel type, booking lead time, arrival dates, length of stay, number of guests, meal plans, market segments, previous cancellations, room types, and other reservation details.

## Objectives
- Explore and understand the hotel booking dataset.
- Identify missing values and analyze their distribution.
- Separate numerical and categorical features.
- Prepare the dataset for machine learning.
- Compare different preprocessing and scaling approaches.
- Train Logistic Regression and Decision Tree classifiers.
- Evaluate and compare model performance.

## Technologies Used
- Python
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- Jupyter Notebook

## Project Workflow

### 1. Data Loading and Exploration
The dataset is loaded using Pandas. Initial exploration includes:
- Viewing the first records with `head()`.
- Checking the dataset dimensions using `shape`.
- Examining column data types and non-null counts with `info()`.
- Generating descriptive statistics using `describe()`.
- Checking the distribution of canceled and non-canceled bookings.

### 2. Missing-Value Analysis
Missing values are identified and summarized by count and percentage.

The analysis identifies columns such as `company`, `agent`, `country`, and `children` with missing values. The `company` column has more than 50% missing data in the original dataset.

The notebook imports both `SimpleImputer` and `KNNImputer` for missing-value handling.

### 3. Data Preprocessing
The dataset is prepared for model training through:
- Separating the target variable (`is_canceled`) from the input features.
- Identifying numerical and categorical columns.
- Handling missing values.
- Encoding categorical variables using `OneHotEncoder`.
- Scaling numerical features using `StandardScaler` or `MinMaxScaler`.
- Using Scikit-learn pipelines and `ColumnTransformer` to organize preprocessing and model training.

The columns `reservation_status` and `reservation_status_date` are removed because they can reveal the outcome of a reservation and cause **data leakage**.

### 4. Model Training
The project compares two classification algorithms:

**Logistic Regression:** A classification model used to estimate the probability of a booking being canceled.

**Decision Tree Classifier:** A model that learns decision rules from booking features to classify reservations.

Different preprocessing pipelines are evaluated to study the effect of feature scaling on each model.

### 5. Model Evaluation
The models are evaluated using the following metrics:

| Metric | Purpose |
|---|---|
| Accuracy | Overall proportion of correct predictions |
| Precision | Proportion of predicted cancellations that are actual cancellations |
| Recall | Proportion of actual cancellations correctly identified |
| F1-score | Harmonic mean of precision and recall |
| Confusion Matrix | Shows correct and incorrect predictions for each class |

## Results

The notebook reports the following comparison:

| Model | Training Accuracy | Testing Accuracy | Precision | Recall | F1-score |
|---|---:|---:|---:|---:|---:|
| Logistic Regression — Pipeline A | 81.89% | 81.88% | 0.8113 | 0.6658 | 0.7314 |
| Logistic Regression — Pipeline B | 81.26% | 81.33% | 0.8083 | 0.6502 | 0.7207 |
| Decision Tree — Pipeline A | 99.63% | 86.02% | 0.8084 | 0.8159 | 0.8122 |
| Decision Tree — Pipeline B | 99.63% | 86.00% | 0.8078 | 0.8164 | 0.8121 |

**Best overall result:** Decision Tree with Pipeline A, achieving approximately **86.02% testing accuracy** and an **F1-score of 0.8122**.

### Key Observations
- Decision Tree models achieve higher testing accuracy and F1-scores than Logistic Regression in these experiments.
- StandardScaler performs slightly better than MinMaxScaler for Logistic Regression.
- Scaling has very little effect on Decision Tree performance.
- The Decision Tree's high training accuracy compared with its testing accuracy suggests possible overfitting.

## Installation

Install the required libraries:

```bash
pip install numpy pandas matplotlib scikit-learn jupyter
```

## How to Run
1. Download or clone the project repository.
2. Place `hotel_bookings.csv` in the appropriate dataset folder.
3. Open the Jupyter Notebook.
4. Update the CSV file path in the notebook to match your local environment.
5. Run the notebook cells in order to perform preprocessing, train the models, and view the evaluation results.

Example dataset-loading statement:

```python
df = pd.read_csv("hotel_bookings.csv")
```

The notebook currently uses an absolute Windows file path, so it must be updated if the dataset is stored elsewhere.

## Learning Outcomes
By completing this project, you can learn how to:
- Perform exploratory data analysis.
- Identify and handle missing values.
- Distinguish numerical and categorical features.
- Build preprocessing pipelines.
- Apply categorical encoding and numerical scaling.
- Train and evaluate classification models.
- Compare model performance using multiple metrics.
- Recognize data leakage and potential overfitting.

## Conclusion
This project demonstrates an end-to-end classification workflow for hotel booking cancellation prediction. By comparing Logistic Regression and Decision Tree models under different preprocessing configurations, it illustrates how preprocessing choices influence model performance. In the reported experiments, Decision Tree achieves the best overall testing performance, although the gap between training and testing accuracy indicates that further work to reduce overfitting may be beneficial.
