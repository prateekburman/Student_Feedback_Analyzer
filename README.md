# Student Feedback Analyzer

## Project Details

- Project Number: PS No. 96
- Project Title: Student Feedback Analyzer
- Programming Language: Python 3

## 1. Introduction

Student Feedback Analyzer is a Python-based project
that analyzes student feedback using ratings and comments.

It reads student feedback from a CSV file and
generates useful information about teaching quality.

## 2. Problem Statement

The purpose of this project is to analyze student
ratings and comments to understand their feedback.

The system calculates average ratings, rating counts,
sentiment percentages and frequently used words.

## 3. Objectives

- Read feedback from a CSV file.
- Validate student ratings.
- Calculate average rating.
- Count ratings from 1 to 5.
- Calculate Positive, Neutral and Negative percentages.
- Find the top 3 frequent words.
- Display a sentiment bar chart.

## 4. Technologies Used

- Python 3
- Pandas
- Matplotlib
- Regular Expressions
- Collections Counter

## 5. Features

1. CSV file reading.
2. Missing file handling.
3. Invalid rating validation.
4. Average rating calculation.
5. Rating frequency analysis.
6. Sentiment analysis.
7. Top 3 word frequency analysis.
8. Bar chart visualization.

## 6. Stop Words

The following words are removed:

and, but, the, is, a, of, too

## 7. How to Run

Install required libraries:

pip install pandas matplotlib

Run the program:

python student_feedback_analyser.py

Enter the CSV filename or press Enter
to use feedback.csv.

## 8. Menu Options

1. Summary and top 3 words
2. Sentiment
3. Exit

## 9. Test Cases

- Test Case 1: Normal Input
- Test Case 2: Boundary / Minimum Input
- Test Case 3: Invalid Input
- Test Case 4: Different Valid Scenario

## 10. Conclusion

The Student Feedback Analyzer successfully analyzes
student feedback using Python.

It helps understand student satisfaction through
rating analysis, word frequency and sentiment
visualization.