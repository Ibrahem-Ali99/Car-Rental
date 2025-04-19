# app.py
import streamlit as st
import sqlite3
from datetime import datetime

# Connect to DB
conn = sqlite3.connect('cars.db', check_same_thread=False)
c = conn.cursor()

st.title("🚗 Dad's Car Rental Tracker")

# Add car form
with st.form("car_form"):
    plate = st.text_input("Plate Number")
    color = st.text_input("Color")
    name = st.text_input("Car Name")
    renter = st.text_input("Renter Name")
    return_date = st.date_input("Return Date")
    submit = st.form_submit_button("Add Car")
    if submit:
        c.execute("INSERT INTO cars (plate, color, name, renter_name, return_date) VALUES (?, ?, ?, ?, ?)", 
                  (plate, color, name, renter, str(return_date)))
        conn.commit()
        st.success("Car added!")

# View cars
st.subheader("📋 Current Cars")
cars = c.execute("SELECT * FROM cars").fetchall()
for car in cars:
    st.write(f"🚘 {car[3]} | Plate: {car[1]}, Color: {car[2]}, Renter: {car[4]}, Return: {car[5]}")

conn.close()
