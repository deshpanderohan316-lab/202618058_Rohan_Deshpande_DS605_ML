# DS605 Lab Assignment 7: Image Representation, PCA, Eigenfaces and Face Recognition

## Overview

This project explores image representation, dimensionality reduction, image reconstruction, and face recognition using Principal Component Analysis (PCA). It uses the **AT&T Database of Faces (ORL)** dataset to represent facial images as numerical feature vectors and recognize subjects using different approaches.

PCA is implemented using NumPy's linear algebra operations, including eigendecomposition and Singular Value Decomposition (SVD). Scikit-learn is used for the final comparison of machine-learning classifiers.

## Objectives

- Represent grayscale facial images as numerical feature vectors.
- Implement PCA using eigendecomposition and SVD.
- Generate and visualize eigenfaces.
- Determine the number of principal components required to retain at least 90% of the explained variance.
- Reconstruct facial images using reduced-dimensional representations.
- Compare the storage requirements of original images and PCA representations.
- Evaluate face recognition using nearest-neighbor matching in raw pixel space and PCA space.
- Compare K-Nearest Neighbors (KNN) and Support Vector Machine (SVM) classifiers.

## Dataset

**AT&T Database of Faces (ORL)**

The dataset contains facial images organized into subject-specific folders. Each subject folder contains grayscale images of that individual.

The dataset should be arranged as follows:

```text
project/
├── 202618058_Lab7.ipynb
├── README.md
├── data/
│   └── orl_faces/
│       ├── s1/
│       │   ├── 1.pgm
│       │   ├── 2.pgm
│       │   └── ...
│       ├── s2/
│       │   ├── 1.pgm
│       │   └── ...
│       └── ...
└── outputs/
```

Download and extract the ORL face dataset before running the notebook. Place all subject folders (`s1`, `s2`, ..., `s40`) inside `data/orl_faces/`.

## Technologies Used

- **Python** — implementation and data processing
- **NumPy** — numerical operations, eigendecomposition, SVD, and PCA
- **Matplotlib** — image visualization and plotting
- **Pillow (PIL)** — loading grayscale images
- **Scikit-learn** — KNN, SVM, and accuracy evaluation
- **Jupyter Notebook** — interactive execution and analysis

## Project Workflow

### Part A: Image Representation

- Load facial images in grayscale.
- Inspect image dimensions and pixel intensity ranges.
- Flatten each image into a one-dimensional feature vector.
- Assign subject labels to the images.
- Create a reproducible training and testing split for each subject.

### Part B: PCA, Eigenfaces and Compression

- Calculate the mean face and center the training data.
- Perform eigendecomposition using the sample-space Gram matrix.
- Compute PCA directions directly using SVD.
- Compare the principal directions obtained through both methods.
- Calculate explained variance and select the minimum number of components required to retain at least 90% of the variance.
- Visualize eigenfaces and reconstruct facial images.
- Compare the storage requirements of original pixel representations and PCA representations.

### Part C: Face Recognition

- Perform nearest-neighbor matching using raw pixel features.
- Perform nearest-neighbor matching using PCA-transformed features.
- Calculate recognition accuracy.
- Inspect examples of correct and incorrect predictions.

### Part D: Machine-Learning Classifier Comparison

- Train a K-Nearest Neighbors (KNN) classifier using PCA features.
- Train a linear Support Vector Machine (SVM) using PCA features.
- Evaluate and compare classifier accuracy.
- Experiment with different numbers of principal components to investigate their effect on recognition performance.

## Installation

Install the required Python libraries:

```bash
pip install numpy matplotlib pillow scikit-learn jupyter
```

## How to Run

1. Download or clone the project files.
2. Download and extract the AT&T/ORL face dataset.
3. Place the subject folders inside `data/orl_faces/`.
4. Install the required dependencies.
5. Open `202618058_Lab7.ipynb` in Jupyter Notebook or JupyterLab.
6. Run all cells sequentially.
7. Review the generated plots, reconstruction examples, storage comparisons, and recognition results.

If the dataset is stored in a different location, update the `DATA_DIR` variable in the notebook.

## Outputs

The notebook generates visualizations and numerical results for:

- Sample grayscale facial images
- Explained variance and cumulative variance
- Eigenface visualizations
- Original and reconstructed facial images
- Storage requirements for original and PCA representations
- Face recognition accuracy using raw pixels and PCA features
- KNN and SVM classifier comparisons across different component counts

Generated figures are saved in the `outputs/` directory where configured by the notebook.

## Conclusion

This project demonstrates how PCA can reduce the dimensionality of facial image data while preserving important information for reconstruction and recognition. It also compares two numerical approaches to PCA and evaluates nearest-neighbor matching against traditional machine-learning classifiers.

The final conclusions should be based on the results obtained by running the notebook, including explained variance, reconstruction quality, storage requirements, and recognition accuracy.

## Author

**Student ID:** 202618058

**Course:** DS605

**Assignment:** Lab Assignment 7
