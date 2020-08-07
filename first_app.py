import streamlit as st
import numpy as np
import pandas as pd

"""You can use some streamlit specific function or not,
Streamlit can interpret usual python code and varables.

Example with streamlit.title() function :"""
st.title("My first app")

"""
And whithout :
# My first app

The same for dataframe with streamlit.write() function :
"""

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

st.write(df)

"And without"

df

"Some other functions :"
"with line_chart() (data from a random dataframe)"

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

"With map()"

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.write(map_data)
st.map(map_data)

"With selectbox() to show/hide"

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    st.line_chart(chart_data)

"With selectbox() to select"

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option