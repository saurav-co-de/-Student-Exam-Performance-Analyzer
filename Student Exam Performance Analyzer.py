# -*- coding: utf-8 -*-
"""
Created on Fri Apr 25 11:58:42 2025

@author: Saurav K
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv("student_performance.csv")

# Fill missing values
data['Exam_Score'].fillna(data['Exam_Score'].mean(), inplace=True)
data['Attendance'].fillna(data['Attendance'].mean(), inplace=True)

# Basic statistics
mean_score = data['Exam_Score'].mean()
print(f"Mean Exam Score: {mean_score}")

# Visualizations
# Bar chart for Exam Scores
plt.bar(data['Student_ID'], data['Exam_Score'], color='blue')
plt.xlabel('Student ID')
plt.ylabel('Exam Score')
plt.title('Exam Scores of Students')
plt.show()

# Line chart for Attendance vs Exam Score
plt.plot(data['Attendance'], data['Exam_Score'], marker='o', color='green')
plt.xlabel('Attendance (%)')
plt.ylabel('Exam Score')
plt.title('Attendance vs Exam Score')
plt.show()

# Pie chart for grade distribution
grades = data['Final_Grade'].value_counts()
plt.pie(grades, labels=grades.index, autopct='%1.1f%%', colors=['lightcoral', 'lightblue', 'lightgreen'])
plt.title('Grade Distribution')
plt.show()
