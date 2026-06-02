# Student Performance Classifier

## Overview

This project predicts student performance categories using machine learning classification algorithms.

The model classifies students into:

- High Performer
- Average Performer
- Risk Student

based on:

- Study Hours
- Attendance
- Assignment Scores
- Previous Marks
- Participation

## Algorithms Used

- Logistic Regression
- Decision Tree
- Random Forest

The model with the highest accuracy is automatically selected and saved.

## Files

student_performance_classifier.py

Main source code for dataset generation, model training and prediction.

student_data.csv

Generated dataset.

best_model.pkl

Saved trained model.

requirements.txt

Required Python libraries.

## How to Run

Install dependencies:

pip install -r requirements.txt

Run:

python student_performance_classifier.py

## Future Improvements

- Larger dataset
- Web dashboard
- More classification algorithms
- Real-world educational data
