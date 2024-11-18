#https://www.youtube.com/watch?v=zSRBVxvhriA&ab_channel=Beginner%27sCodeZone
import mysql.connector
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'tu_contraseña',
    database = 'finalv1'
)
print('Connected')

cursor = connection.cursor()

cursor.execute("Select * from medicinav1")
data = cursor.fetchall()
#print(data)

st.title('Lecturas del sensor')

df = pd.DataFrame(data,columns = cursor.column_names)
st.dataframe(df)
