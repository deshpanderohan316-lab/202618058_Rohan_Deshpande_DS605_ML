# Garment Employee Productivity Prediction

## DS605 — Fundamentals of Machine Learning

A machine learning project for predicting **actual productivity of garment manufacturing workers** using supervised regression models.

---

## 1. Project Objective

The objective of this project is to predict the `actual_productivity` of garment manufacturing teams based on operational, workforce, incentive, and production-related variables.

The project compares multiple machine learning regression models and evaluates their performance using standard regression metrics.

---

## 2. Dataset

The dataset contains:

- **1,197 observations**
- **16 variables**
- Target variable: `actual_productivity`

### Main Features

- `quarter`
- `department`
- `day`
- `team`
- `targeted_productivity`
- `smv`
- `wip`
- `over_time`
- `incentive`
- `idle_time`
- `idle_men`
- `no_of_style_change`
- `no_of_workers`
- `month`
- `day_of_month`

### Target

`actual_productivity`

---

## 3. Data Preprocessing

The following preprocessing steps were performed:

### Numerical Features

Missing numerical values were handled using:

```text
Median Imputation
