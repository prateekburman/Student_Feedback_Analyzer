## Project Summary Report

Problem Statement Number: 96
Project Title: Student Feedback Analyzer
Programming Language: Python 3
Libraries Used: Pandas, Matplotlib
Concepts: Strings, Data Analysis, Frequency Analysis and Data Visualization

## 1. Introduction

Student Feedback Analyzer is a Python-based project designed to analyze student feedback collected through ratings and comments.

The program reads feedback from a CSV file and processes the data to generate useful information about students' opinions and experiences.

It helps understand the overall feedback through rating analysis, sentiment analysis and frequently used words.

## 2. Problem Statement

Educational institutions collect feedback from students to understand the quality of teaching and learning experiences.

Analyzing feedback manually can take time. This project provides an automated solution to process student ratings and comments using Python.

## 3. Objectives

The main objectives are:

1. Read student feedback from a CSV file.
2. Calculate the average rating.
3. Count ratings from 1 to 5.
4. Calculate positive, neutral and negative feedback percentages.
5. Identify the top 3 frequently used words in comments.
6. Ignore predefined stop words.
7. Detect and skip invalid ratings.
8. Display sentiment analysis using a bar chart.

## 4. Technologies Used

- Python 3: Main programming language.
- Pandas: Used to read and process CSV data.
- Matplotlib: Used to create the sentiment bar chart.
- CSV: Used to store student feedback.

## 5. Input Dataset

The project uses a file named "feedback.csv".

It contains three columns:

- StudentID
- Rating
- Comment

The dataset contains feedback from six students.

## 6. Working of the Project

The project works in the following steps:

1. Reads the CSV file.
2. Checks whether the required columns are available.
3. Validates ratings to ensure they are whole numbers from 1 to 5.
4. Skips invalid ratings and displays warnings.
5. Calculates the average rating and rating counts.
6. Analyzes comments to find the most frequent words.
7. Calculates positive, neutral and negative feedback percentages.
8. Displays a bar chart for sentiment analysis.

## 7. Rating Classification

- Positive: Ratings 4 and 5.
- Neutral: Rating 3.
- Negative: Ratings 1 and 2.

## 8. Stop Words

The following words are removed during word frequency analysis:

and, but, the, is, a, of, too

## 9. Menu Options

The program provides three menu options:

1. Summary and Top 3 Words
2. Sentiment
3. Exit

## 10. Test Cases

Test Case 1: Normal Input

Six valid student feedback records are provided.

Expected results:

- Valid feedback: 6
- Average rating: 3.83
- Rating counts: 5 → 2, 4 → 2, 3 → 1, 2 → 1, 1 → 0
- Top words: great (3), notes (3), clear (2)

Test Case 2: Minimum Input

Only one valid student feedback record is provided.

Expected results:

- Valid feedback: 1
- Average rating: 5.00
- Rating counts: 5 → 1, 4 → 0, 3 → 0, 2 → 0, 1 → 0
- Top word: great (1)

Test Case 3: Invalid Ratings

Two invalid ratings are provided: 6 and abc.

Expected results:

- Both invalid records are skipped.
- Warning messages are displayed.
- Valid feedback: 6
- Average rating: 3.83

Test Case 4: Sentiment Analysis

The original six feedback records are analyzed.

Expected results:

- Positive: 4 (66.67%)
- Neutral: 1 (16.67%)
- Negative: 1 (16.67%)

A bar chart is generated to represent sentiment percentages.

## 11. Output and Results

The program successfully analyzes valid student feedback and displays:

- Total valid feedback records.
- Average rating.
- Rating-wise counts.
- Top three frequently used words.
- Positive, neutral and negative percentages.
- Sentiment bar chart.

Invalid ratings are skipped with warning messages.

## 12. Advantages

- Saves time in feedback analysis.
- Provides accurate rating calculations for valid records.
- Identifies common words in student comments.
- Presents feedback in an understandable format.
- Uses graphical visualization for sentiment analysis.

## 13. Conclusion

The Student Feedback Analyzer project demonstrates how Python can be used to process and analyze student feedback.

It combines CSV handling, Pandas, string processing, frequency analysis and Matplotlib visualization.

The project provides a simple and useful way to understand student opinions and evaluate feedback.