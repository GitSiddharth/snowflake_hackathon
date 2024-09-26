import streamlit as st
import snowflake.connector
import pandas as pd
import altair as alt

# Snowflake connection details
def init_connection():
    conn = snowflake.connector.connect(
        user='siddharth',
        password='Siddharth@123',
        account='ikjcjrn-vu31864',
        warehouse='MY_WH',
        database='MENTAL_HEALTH_DB',
        schema='SID'
    )
    return conn

# Function to query data from Snowflake
def run_query(query):
    conn = init_connection()
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

# Query to retrieve the data
query = """
    SELECT district, severe_mental_disorder, common_mental_disorder, alcohol_substance_abuse, 
           cases_referred_to_higher_centres, suicide_attempt_cases, others, total
    FROM mental_health_data
"""

# Fetch data from Snowflake
data = run_query(query)

# Convert to Pandas DataFrame
columns = ['District', 'Severe Mental Disorder', 'Common Mental Disorder', 'Alcohol & Substance Abuse',
           'Cases Referred to Higher Centres', 'Suicide Attempt Cases', 'Others', 'Total']
df = pd.DataFrame(data, columns=columns)

# Streamlit app title
st.title('Mental Health Data Dashboard')

# Display the data in a table
st.subheader('Data from Snowflake')
st.dataframe(df)

# Create charts using Altair

# Bar chart for total cases by district
st.subheader('Total Mental Health Cases by District')
chart_total = alt.Chart(df).mark_bar().encode(
    x='District:N',
    y='Total:Q',
    tooltip=['District', 'Total']
).properties(
    width=700,
    height=400
)
st.altair_chart(chart_total)

# Bar chart for Alcohol and Substance Abuse cases by district
st.subheader('Alcohol & Substance Abuse Cases by District')
chart_abuse = alt.Chart(df).mark_bar().encode(
    x='District:N',
    y='Alcohol & Substance Abuse:Q',
    tooltip=['District', 'Alcohol & Substance Abuse']
).properties(
    width=700,
    height=400
)
st.altair_chart(chart_abuse)

# Other visualizations can be added similarly
import sklearn

from sklearn.linear_model import LinearRegression
import numpy as np

# Add model section in sidebar
st.sidebar.header("Mental Health Predictor")
age = st.sidebar.slider('Age', 18, 70, 30)
hours_worked = st.sidebar.slider('Average hours worked per day', 0, 14, 8)
sleep_hours = st.sidebar.slider('Average sleep hours per day', 0, 12, 7)

# Mock data and prediction
X = np.array([[hours_worked, sleep_hours]])
model = LinearRegression()
model.fit([[6, 7], [8, 6], [10, 5]], [7, 6, 5])  # Mock data for training
prediction = model.predict(X)

st.sidebar.write(f"Predicted Mental Health Well-Being Score: {prediction[0]:.2f}")



import matplotlib.pyplot as plt
# Multi-page navigation
page = st.selectbox("Choose a page", ["Mental Health Predictor", "Work Hours Analysis"])

if page == "Mental Health Predictor":
    st.sidebar.header("Mental Health Predictor")
    # Add predictor code here

elif page == "Work Hours Analysis":
    st.title("Working Hours Analysis")
    # Add working hours chart code here
    
    # Example data for Indians' working hours across sectors
    data = {
        'Sectors': ['IT', 'Manufacturing', 'Health', 'Education'],
        'Hours per Week': [45, 50, 55, 40]
    }

    # Bar chart for hours worked
    fig, ax = plt.subplots()
    ax.bar(data['Sectors'], data['Hours per Week'], color=['blue', 'orange', 'green', 'red'])
    ax.set_ylabel('Hours Worked per Week')
    ax.set_title('Average Working Hours per Week in Different Sectors')
    st.pyplot(fig)



