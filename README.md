# Mental Health Predictor & Working Hours Analysis Dashboard

This project is a multi-page Streamlit web application that integrates data from Snowflake and offers two primary functionalities:
1. **Mental Health Predictor**: Uses a simple linear regression model to predict an individual's mental well-being based on their work-life balance factors.
2. **Working Hours Analysis**: Displays charts analyzing how long Indians are working across various sectors.

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Snowflake Setup](#snowflake-setup)
- [Run the Application](#run-the-application)
- [Deployment](#deployment)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Mental Health Predictor**: A sidebar form to predict well-being scores based on hours worked and sleep.
- **Working Hours Analysis**: A bar chart displaying working hours across sectors.
- **Multi-page Navigation**: Users can navigate between the predictor and data insights.
- **Snowflake Integration**: Fetches and displays data stored in a Snowflake database.

## Tech Stack

- **Backend**: Python, Snowflake
- **Frontend**: Streamlit (Python framework)
- **Machine Learning**: `scikit-learn` (Linear Regression)
- **Data Visualization**: Matplotlib, Streamlit components
- **Database**: Snowflake

## Installation

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/your_username/mental_health_dashboard.git
    cd mental_health_dashboard
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Make sure you have your Snowflake credentials set up.

## Snowflake Setup

Create a table in Snowflake to store the mental health data:

```sql
CREATE TABLE mental_health_data (
    district STRING,
    severe_mental_disorder INT,
    common_mental_disorder INT,
    alcohol_substance_abuse INT,
    cases_referred_to_higher_centres INT,
    suicide_attempt_cases INT,
    others INT,
    total INT
);
