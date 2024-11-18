import mysql.connector
import streamlit as st
import pandas as pd
connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Contra#1',
    database = 'finalv1'
)
print('Connected')

cursor = connection.cursor()

cursro.execute("Select * from medicinav1")
data = cursor.fetchall()

st.title('Lecturas del sensor')

df = pd.DataFrame(data,colums = cursor.column_names)
st.dataframe(df)
