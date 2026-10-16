# Lab 02 — NumPy and Pandas

## Overview

This lab introduces numerical computing with NumPy and data manipulation with Pandas. It demonstrates how to create and manipulate arrays, perform mathematical operations, calculate statistics, inspect datasets, and analyze passenger survival patterns using the Titanic dataset.

The notebook is divided into two main parts:

- **Part A:** Vectorized Programming with NumPy
- **Part B:** Data Wrangling with Pandas using the Titanic Dataset

## Part A — Vectorized Programming with NumPy

### 1. Arrays, Statistics, and Indexing

This section demonstrates how to create and analyze NumPy arrays.

Operations include:

- Generating random integers using `np.random.randint()`.
- Setting a random seed using `np.random.seed(42)` for reproducibility.
- Calculating minimum, maximum, mean, median, and standard deviation.
- Creating arrays using `np.arange()`, `np.linspace()`, `np.zeros()`, and `np.ones()`.
- Creating one-dimensional, two-dimensional, and three-dimensional arrays.
- Inspecting array shape and dimensions using `shape` and `ndim`.
- Accessing elements, rows, columns, and layers through indexing and slicing.

### 2. Vectorized Arithmetic and Linear Algebra

This section explores numerical operations performed directly on arrays without explicit Python loops.

Operations include:

- Matrix addition.
- Element-wise multiplication.
- Matrix multiplication using `@` and `np.matmul()`.
- Finding the transpose of a matrix.
- Calculating the determinant using `np.linalg.det()`.
- Computing the inverse of an invertible matrix using `np.linalg.inv()`.
- Verifying the inverse using `np.allclose()` and the identity matrix.

These operations demonstrate how NumPy simplifies mathematical computations and supports efficient numerical programming.

### 3. Statistical Operations and Visualization

The notebook also demonstrates statistical calculations and visualization using numerical data.

It covers generating data, calculating statistical values, and plotting distributions to understand how observations are spread around a mean.

## Part B — Data Wrangling with Pandas: Titanic Dataset

### Objective

Analyze the Titanic passenger dataset to understand its structure, clean and filter records, summarize passenger information, and explore relationships between passenger characteristics and survival.

### Dataset

**File:** `train.csv`

The dataset contains passenger information such as:

- `PassengerId`
- `Survived`
- `Pclass`
- `Name`
- `Sex`
- `Age`
- `SibSp`
- `Parch`
- `Ticket`
- `Fare`
- `Cabin`
- `Embarked`

The `Survived` column indicates whether a passenger survived:

- `0` — Did not survive
- `1` — Survived

### 1. Loading and Inspecting Data

The notebook uses Pandas to load the CSV file and examine the dataset.

Methods include:

- `pd.read_csv()` — Load the dataset.
- `head()` and `tail()` — View the first and last rows.
- `shape` — Find the number of rows and columns.
- `columns` — Display column names.
- `info()` — Inspect data types and non-null counts.
- `describe()` — Generate descriptive statistics.

### 2. Data Cleaning and Missing Values

This part examines missing data and uses visualizations to understand which columns contain missing values.

The missing-value analysis helps identify columns that may require cleaning before further analysis.

### 3. Filtering and Querying

The notebook uses Boolean conditions to select specific passenger groups, including:

- Male passengers older than 50.
- Female passengers travelling in first class.
- Passengers satisfying combinations of multiple conditions.

These operations demonstrate how to filter rows using Pandas conditions.

### 4. Grouping and Aggregation

Grouping operations summarize passenger data by categories such as sex and passenger class.

Aggregation helps compare survival patterns across different groups.

### 5. Pivot Tables and Survival Analysis

A pivot table is used to calculate survival rates by sex and passenger class.

The recorded results show:

- **Highest survival rate:** Approximately 0.97 for first-class female passengers.
- **Lowest survival rate:** Approximately 0.14 for third-class male passengers.

These results illustrate how passenger characteristics are associated with survival in the dataset.

### 6. Visualization and Observations

The notebook uses visualization libraries to explore numerical relationships and patterns.

Visualizations include a correlation heatmap for relevant numerical columns. This helps identify positive and negative correlations between variables.

## Technologies Used

- **Python 3** — Programming language.
- **NumPy** — Array operations, statistics, and linear algebra.
- **Pandas** — Data loading, filtering, cleaning, grouping, and aggregation.
- **Matplotlib** — Data visualization.
- **Seaborn** — Statistical visualizations and correlation heatmaps.
- **Jupyter Notebook** — Interactive development environment.

## Installation

Install the required libraries using:

```bash
pip install numpy pandas matplotlib seaborn jupyter
```

## How to Run

1. Place the notebook and Titanic `train.csv` file in accessible directories.
2. Update the CSV file path in the notebook if it differs from the path used in the original environment.
3. Install the required Python libraries.
4. Start Jupyter Notebook:

   ```bash
   jupyter notebook
   ```

5. Open the notebook and execute the cells sequentially.

## Learning Outcomes

After completing this lab, you should be able to:

- Create and manipulate NumPy arrays of different dimensions.
- Perform array slicing, indexing, and vectorized operations.
- Apply matrix operations and basic linear algebra.
- Calculate descriptive statistics and visualize distributions.
- Load and inspect CSV datasets using Pandas.
- Identify missing values and filter records using conditions.
- Group data and calculate summary statistics.
- Create pivot tables and correlation heatmaps.
- Interpret patterns in the Titanic passenger survival data.

## Conclusion

This lab builds a foundation in numerical computing and data analysis. NumPy provides efficient tools for array manipulation and linear algebra, while Pandas makes it easier to clean, filter, summarize, and analyze structured datasets.

The Titanic analysis demonstrates how data manipulation and visualization can reveal meaningful patterns in real-world data.
