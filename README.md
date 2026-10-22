
# Student Marks Calculator

## Project Description

A beginner-friendly Python command-line utility that accepts
student details, validates user input, calculates marks,
and prints a formatted student report.

## Requirements

- Python 3
- Git
- Visual Studio Code (optional)

## Setup Instructions

### 1. Clone the repository

```powershell
git clone YOUR_GITHUB_REPOSITORY_URL
cd student-marks-calculator
```

If you already have the project folder, skip this step.

### 2. Create a virtual environment

```powershell
python -m venv .venv
```

### 3. Activate the virtual environment

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Run the program

```powershell
python app.py
```

## Features

- Accepts student name and age
- Accepts Python and Maths marks
- Validates empty names and invalid numbers
- Checks marks are between 0 and 100
- Calculates total and average
- Displays PASS or FAIL
- Prints a formatted report

## Validation Rules

- Student name cannot be empty.
- Age must be a positive whole number.
- Marks must be numeric and between 0 and 100.
- Average of 40 or more is considered PASS.

## Dependencies

Uses Python built-in functions only.
No additional packages are required.
