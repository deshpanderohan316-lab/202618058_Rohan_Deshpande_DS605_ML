### Assignment title-
Lab Assignment - 3: Scikit-learn: Data Preprocessing and Model Performance Evaluation

### Name-
Rohan Deshpande

### Student ID-
202618058

### Dataset-
Kaggle Hotel Booking Demand (hotel_bookings.csv)

### Preprocessing choices-
1) Feature selection
2) Column Identification (Numericals columns and Categorical columns)
3) StandardScalar, OneHotEncoder, MinMaxScalar

### Observations
Decision Tree models performed better than Logistic Regression models, achieving approximately 86.0% testing accuracy compared with approximately 81.9% for the best Logistic Regression model.
Decision Tree with StandardScaler produced the best overall result, with a testing accuracy of 86.02% and an F1-score of 0.8122.
StandardScaler performed slightly better than MinMaxScaler for Logistic Regression, with higher testing accuracy, precision, recall, and F1-score.
Scaling had almost no effect on Decision Tree performance, as the StandardScaler and MinMaxScaler versions produced nearly identical results.
The Decision Tree shows signs of overfitting, with training accuracy of approximately 99.63% compared with testing accuracy of approximately 86.02%, whereas Logistic Regression had very similar training and testing accuracy.