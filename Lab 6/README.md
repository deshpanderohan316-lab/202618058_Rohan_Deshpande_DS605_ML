# DS605 Lab 6: Feature Extraction and Machine Learning with Image and Text Data

## Overview

This project explores two applications of machine learning:

1. **Image Feature Extraction and Classification:** Extract numerical features from crack and non-crack images and use machine learning classifiers to identify cracks.
2. **Text Vectorization and Spam Classification:** Represent email data as text features and use Logistic Regression to classify spam and non-spam emails.

The project demonstrates how raw images and text-related data can be converted into numerical representations that machine learning models can process.

## Objectives

- Inspect and preprocess image and email datasets.
- Extract intensity-based and edge-based features from images.
- Apply Canny edge detection to identify image edges.
- Train and compare multiple image classification algorithms.
- Understand text vectorization using `CountVectorizer`.
- Build a Logistic Regression model for spam classification.
- Evaluate models using accuracy, precision, recall, and F1-score.
- Compare training and prediction times.

## Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- OpenCV
- Scikit-learn
- Jupyter Notebook
- Python `time` module

## Part A: Image Feature Extraction and Classification

### Dataset

The image dataset contains two classes:

- `Cracks`: Images containing visible cracks.
- `NonCracks`: Images without cracks.

The dataset contains **400 images**, evenly divided between the two classes.

| Class | Number of images |
|---|---:|
| Crack | 200 |
| Non-crack | 200 |
| **Total** | **400** |

The sample images have dimensions of 448 × 448 pixels with three color channels.

### 1. Image preprocessing

The notebook performs the following preprocessing steps:

- Reads images using OpenCV.
- Inspects image dimensions and color channels.
- Visualizes sample images.
- Resizes images to 224 × 224 pixels.
- Converts images to grayscale to simplify intensity analysis.

### 2. Intensity-based feature extraction

The notebook extracts the following features from grayscale images:

| Feature | Description |
|---|---|
| `mean_brightness` | Average pixel intensity |
| `contrast` | Variation in pixel intensities |
| `dark_pixel_ratio` | Proportion of pixels below a dark-intensity threshold |
| `bright_pixel_ratio` | Proportion of pixels above a bright-intensity threshold |
| `min_intensity` | Minimum pixel intensity |
| `max_intensity` | Maximum pixel intensity |
| `median_intensity` | Median pixel intensity |

These features summarize the brightness and intensity distribution of each image.

### 3. Edge-based feature extraction

The notebook uses **Canny Edge Detection** to identify edges in grayscale images.

Two additional features are extracted:

- `edge_count`: Number of detected edge pixels.
- `edge_density`: Proportion of image pixels identified as edges.

Edge information can help distinguish images because cracks may create characteristic lines and boundaries.

### 4. Feature dataset creation

Features are extracted from all images and stored in a Pandas DataFrame.

The resulting dataset contains:

- 400 rows, representing images.
- 11 columns, including the filename, class label, and nine numerical image features.
- No missing values in the reported feature dataset.

The filename is excluded from the model input, and class labels are encoded as:

- `NonCrack = 0`
- `Crack = 1`

### 5. Train-test split

The dataset is divided into training and testing sets using an 80:20 split, with `random_state=42` and stratification to preserve class proportions.

| Set | Images |
|---|---:|
| Training | 320 |
| Testing | 80 |
| Total | 400 |

Each set maintains equal representation of the two classes.

### 6. Machine learning models

Four classifiers are trained and evaluated:

- **Logistic Regression:** A linear classification model that predicts class probabilities.
- **Random Forest:** An ensemble of decision trees that combines their predictions.
- **Decision Tree:** A tree-based model that learns decision rules from features.
- **Support Vector Machine (SVM):** A classifier that separates classes using a decision boundary; the notebook uses an RBF kernel.

StandardScaler is used in pipelines for Logistic Regression and SVM.

### 7. Evaluation metrics

The image classification models are evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Training time
- Prediction time
- Confusion matrices

### 8. Image classification results

The following values are from the notebook's recorded execution.

| Model | Accuracy | Precision | Recall | F1-score |
|---|---:|---:|---:|---:|
| Logistic Regression | 93.75% | 92.68% | 95.00% | 93.83% |
| Random Forest | 95.00% | 95.00% | 95.00% | 95.00% |
| Decision Tree | 93.75% | 94.87% | 92.50% | 93.67% |
| SVM | 93.75% | 92.68% | 95.00% | 93.83% |

**Observation:** Random Forest achieved the highest accuracy and F1-score among the four image classifiers in this execution.

## Part B: Text Vectorization and Spam Classification

### Dataset

The email dataset is stored in `emails.csv`.

It contains 5,172 email records and 3,002 columns:

- `Email No.`: Email identifier.
- 3,000 word-frequency features.
- `Prediction`: Target label indicating whether an email is spam.

The class distribution is:

| Class label | Number of emails |
|---|---:|
| `0` — Non-spam | 3,672 |
| `1` — Spam | 1,500 |
| **Total** | **5,172** |

**Important dataset note:** The supplied CSV does not contain the original email messages. Instead, it contains word-frequency values for an existing vocabulary.

### 1. Inspecting the email data

The notebook examines:

- Dataset dimensions and column names.
- Email identifiers.
- The target column and unique class labels.
- The distribution of spam and non-spam emails.
- The existing word-frequency features.

A visualization is created to compare the two class counts.

### 2. Reconstructing text representation

Because the original email text is unavailable, the notebook reconstructs a token-based representation using the existing word-frequency columns.

Words are repeated according to their stored frequency values to create a text string for each email.

This reconstructed text is a representation derived from the frequency data, not the original email content.

### 3. Train-test split

The reconstructed email data is divided into training and testing sets using an 80:20 split with `random_state=42` and stratification.

| Set | Number of emails |
|---|---:|
| Training | 4,137 |
| Testing | 1,035 |
| Total | 5,172 |

### 4. Text vectorization with CountVectorizer

`CountVectorizer` converts the reconstructed text into a numerical document-term matrix.

The notebook fits the vectorizer on the training text and transforms the testing text using the fitted vocabulary.

The resulting matrices have the following dimensions:

| Matrix | Shape |
|---|---|
| Training | 4,137 × 2,974 |
| Testing | 1,035 × 2,974 |

The vectorizer generates 2,974 features from the reconstructed text.

### 5. Logistic Regression for spam classification

A Logistic Regression model is trained using the vectorized email data.

The model predicts whether an email belongs to the spam or non-spam class.

Its performance is measured using accuracy, precision, recall, F1-score, execution time, and a confusion matrix.

### 6. Spam classification results

The recorded results are:

| Metric | Result |
|---|---:|
| Accuracy | 98.07% |
| Precision | 95.45% |
| Recall | 98.00% |
| F1-score | 96.71% |
| Training time | 0.246212 seconds |
| Prediction time | 0.000939 seconds |

The confusion matrix is:

| | Predicted non-spam | Predicted spam |
|---|---:|---:|
| Actual non-spam | 721 | 14 |
| Actual spam | 6 | 294 |

The model correctly classified 721 non-spam emails and 294 spam emails in the test set.

**Observation:** Logistic Regression achieved an accuracy of approximately 98.07% on the reconstructed email representation.

Because the original email messages are unavailable, these results evaluate classification using reconstructed word-frequency data rather than raw email text.

## Installation

Install the required libraries using:

```bash
pip install numpy pandas matplotlib opencv-python scikit-learn jupyter
```

## How to Run

1. Download the notebook `202618058_Lab6.ipynb`.
2. Prepare the image dataset with the following directory structure:

   ```text
   Datasets/
   ├── Cracks/
   │   ├── image1.jpg
   │   └── ...
   └── NonCracks/
       ├── image1.jpg
       └── ...
   ```

3. Place `emails.csv` in the dataset folder used by Part B.
4. Open the notebook using Jupyter Notebook or JupyterLab.
5. Update the image and email dataset paths to match your local directories.
6. Install the required dependencies.
7. Run the notebook cells sequentially.

**Note:** The notebook currently contains Windows-specific absolute dataset paths. These must be updated if the project is run on another computer or directory.

## Conclusion

This lab demonstrates two ways of applying machine learning to different types of data.

In Part A, image processing techniques transform crack and non-crack images into numerical intensity and edge features. Four classifiers are then compared, with Random Forest achieving the best recorded image classification results.

In Part B, an existing word-frequency dataset is converted into reconstructed text, vectorized using CountVectorizer, and classified using Logistic Regression. The model achieves 98.07% test accuracy on the supplied data representation.

Overall, the project provides practical experience with feature extraction, data preprocessing, text vectorization, classification algorithms, evaluation metrics, confusion matrices, and execution-time comparison.