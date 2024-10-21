import streamlit as st
import time
st.title("Dahej Calculator")

st.sidebar.title("Navigation")

page = st.sidebar.radio("naviagtion",['Home','Contribute data','About us'])

if page== 'Home':
    age = st.slider("Choose age", 21,80)
    st.write("Age : ",age)
    prof = st.selectbox("Profession",['Please select','Doctor','Engineer','Lawyer','Civil Services','BusinessMan','Corporate Job','Agriculture','Other'])
    if prof == 'Other':
        other_prof = st.text_input("Enter profession")

    sal = st.text_input("Salary")

    mar = st.selectbox("Marital status",["please select","Bachelor","Divorced","Widower","Married"])
    local = st.radio("Locality",['Urban','Rural'])
    house = st.radio("House",['owned','rented','None'])
    girl_age = st.slider("Choose woman age",21,38, (25,30))

    submit_but = st.button("Calculate Dahej")

    if submit_but == 1:
        st.write("Asking for dowry is a criminal offence!")


if page == 'Contribute data':
    st.title("Contribute Data")

    new_age = st.text_input("Enter age")
    new_prof = st.text_input("Enter profession")
    new_sal = st.text_input("Enter salary")
    dahej = st.text_input("Enter total amount of gifts")

if page == 'About us':
    st.title("About Us")


