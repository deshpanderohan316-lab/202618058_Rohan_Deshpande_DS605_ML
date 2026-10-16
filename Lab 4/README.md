# Airbnb Price Prediction Using Machine Learning

## 1. Project Overview

This project predicts the nightly price of Airbnb listings in New York City using machine learning regression models. It uses information such as location, room type, geographical coordinates, number of reviews, minimum nights, and availability to estimate the listing price.

The project covers the complete machine learning workflow, including data cleaning, exploratory feature preparation, feature engineering, preprocessing, model training, cross-validation, hyperparameter tuning, model evaluation, and saving the final trained model.

## 2. Objectives

- Analyze the Airbnb NYC 2019 dataset.
- Clean invalid prices and handle missing or invalid feature values.
- Create useful features from the available data.
- Build and compare multiple regression models.
- Evaluate models using MAE, RMSE, and R².
- Use cross-validation and hyperparameter tuning to improve prediction performance.
- Save the final model for future price predictions.

## 3. Dataset

**Dataset:** Airbnb NYC 2019 (`AB_NYC_2019.csv`)

The original dataset contains **48,895 rows and 16 columns**.

Important attributes include:

| Attribute | Description |
|---|---|
| `neighbourhood_group` | NYC borough or neighbourhood group |
| `neighbourhood` | Specific neighbourhood |
| `latitude` | Listing latitude |
| `longitude` | Listing longitude |
| `room_type` | Type of room or accommodation |
| `minimum_nights` | Minimum nights required |
| `number_of_reviews` | Total number of reviews |
| `reviews_per_month` | Average reviews per month |
| `availability_365` | Days available during the year |
| `price` | Nightly listing price; prediction target |

After cleaning and feature selection, the final modeling dataset contains **48,410 observations and 13 features**.

## 4. Technologies Used

- **Python** — programming language
- **Pandas** — data loading and manipulation
- **NumPy** — numerical computations and feature engineering
- **Matplotlib** — visualization
- **Scikit-learn** — preprocessing, regression, evaluation, cross-validation, and hyperparameter tuning
- **Joblib** — model persistence

## 5. Project Workflow

### Step 1: Data Loading and Inspection

- Load the CSV dataset using Pandas.
- Inspect the dataset dimensions and column names.
- Check duplicate records and data types.

### Step 2: Data Cleaning

- Remove duplicate rows.
- Drop irrelevant identifier and free-text columns, including listing IDs, host IDs, names, and host names.
- Convert the target price to a numeric format.
- Remove missing, zero, and negative prices.
- Remove extreme prices above the 99th percentile.
- Convert numerical attributes to appropriate numeric types.
- Handle invalid negative values and restrict availability to the range of 0–365 days.

### Step 3: Feature Engineering

Create additional features to help the models identify useful patterns:

- **Log transformations:** Apply `log1p` to skewed numerical attributes such as minimum nights and review counts.
- **Availability ratio:** Convert annual availability into a ratio by dividing it by 365.
- **Distance from centre:** Calculate an approximate distance from the reference coordinates of NYC.
- **Neighbourhood and room interaction:** Combine neighbourhood group and room type into a single categorical feature.
- **Review indicator:** Create `has_review` to indicate whether a listing has a recorded review date.

### Step 4: Feature Selection

The final model uses 13 selected features covering:

- Location and geographical information
- Room type and neighbourhood combinations
- Log-transformed review and listing attributes
- Availability ratio
- Review presence

The target variable is `price`.

### Step 5: Train-Test Split

The cleaned dataset is split into training and testing sets:

- **Training data:** 38,728 observations
- **Testing data:** 9,682 observations
- **Test size:** 20%
- **Random state:** 42

### Step 6: Preprocessing

A Scikit-learn preprocessing pipeline is used to prepare the features.

**Numerical features**
- Fill missing values using the median.
- Standardize features using `StandardScaler`.

**Categorical features**
- Fill missing values using the most frequent value.
- Apply `OneHotEncoder` to convert categories into numerical representations.
- Ignore previously unseen categories during transformation.

`ColumnTransformer` combines the numerical and categorical preprocessing steps.

### Step 7: Target Transformation

Airbnb prices are right-skewed, so a logarithmic transformation is applied to the target variable using `log1p`.

The model's predictions are converted back to the original price scale using `expm1`.

### Step 8: Model Training and Comparison

Three regression models are evaluated:

1. **Ridge Regression** — a regularized linear regression model.
2. **Random Forest Regressor** — an ensemble of decision trees.
3. **Extra Trees Regressor** — an ensemble model that introduces additional randomness when building trees.

### Step 9: Cross-Validation

Five-fold cross-validation is performed on the training data to compare model performance across different data splits.

### Step 10: Hyperparameter Tuning

`RandomizedSearchCV` is used to tune the Random Forest model.

The search considers parameters such as:

- Number of trees (`n_estimators`)
- Maximum tree depth (`max_depth`)
- Minimum samples required to split a node
- Minimum samples required at a leaf
- Number of features considered for splitting

The tuning process evaluates 15 parameter combinations using three-fold cross-validation.

### Step 11: Model Evaluation and Saving

The final model is evaluated on the held-out test dataset using MAE, RMSE, and R². The trained model is saved as a pickle file for later use.

## 6. Model Performance

### Baseline Model Comparison

The following results were obtained before hyperparameter tuning:

| Model | Test MAE | Test RMSE | Test R² |
|---|---:|---:|---:|
| Random Forest | 44.39 | 78.76 | 0.4300 |
| Ridge Regression | 45.74 | 80.04 | 0.4113 |
| Extra Trees | 46.27 | 81.99 | 0.3823 |

Random Forest performed best among the three baseline models based on test RMSE.

### Final Model Results

The tuned Random Forest model achieved the following test results:

| Metric | Result |
|---|---:|
| Test MAE | $41.79 |
| Test RMSE | $72.66 |
| Test R² | 0.5148 |

The final model explains approximately **51.48% of the variation** in Airbnb listing prices in the test dataset.

- **MAE:** The average absolute prediction error is approximately $41.79 per listing.
- **RMSE:** The root mean squared prediction error is approximately $72.66, with larger errors receiving greater weight.
- **R²:** The model explains approximately 51.48% of the variation in the target prices.

These results indicate that the tuned Random Forest improved upon the baseline Random Forest. Prediction errors can still be substantial, so the model should be treated as an estimation tool rather than a guarantee of actual listing prices.

## 7. Installation

Install the required Python libraries:

```bash
pip install numpy pandas matplotlib scikit-learn joblib jupyter
```

## 8. How to Run the Project

1. Download or place `AB_NYC_2019.csv` in your dataset directory.
2. Open the Jupyter Notebook.
3. Update `DATA_PATH` in the notebook to point to your local CSV file.
4. Run the notebook cells in order.
5. Review the model comparison, cross-validation, and final evaluation results.
6. Ensure the final model file is generated by the notebook.

Example:

```python
DATA_PATH = "path/to/AB_NYC_2019.csv"
```

Replace the example path with the actual location of your dataset.

## 9. Saved Model

The final trained model is saved as:

`airbnb_price_prediction_final.pkl`

The saved model can be loaded with Joblib:

```python
import joblib

model = joblib.load("airbnb_price_prediction_final.pkl")
```

The file must exist in the expected location before loading. Use the same feature names and preprocessing-compatible input structure that the notebook expects when generating predictions.

**Note:** The notebook creates the saved model file; it is not necessarily included with the notebook or dataset.

## 10. Key Learnings

- Cleaning real-world data before training a model.
- Handling missing values and invalid numerical values.
- Engineering features to represent location and availability.
- Encoding categorical features and scaling numerical features.
- Comparing linear and tree-based regression models.
- Using cross-validation to assess model reliability.
- Tuning hyperparameters with randomized search.
- Evaluating regression models using MAE, RMSE, and R².
- Saving a trained model for future predictions.

## 11. Conclusion

This project demonstrates an end-to-end machine learning approach to predicting Airbnb listing prices in New York City. After data cleaning, feature engineering, preprocessing, and model comparison, Random Forest emerged as the strongest baseline model. Hyperparameter tuning improved its performance, producing a final test MAE of $41.79, RMSE of $72.66, and R² of 0.5148.

The project provides practical experience in regression modeling and shows how machine learning can use location, accommodation type, and listing characteristics to estimate prices.
