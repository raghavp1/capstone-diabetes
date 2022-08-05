from unittest.util import strclass
import streamlit as st

def app(df):
    st.title("Diabetes Prediction Web App")
    st.subheader("web app to predict diabetes")

    with st.beta_expander("View Data"):
        st.dataframe(df)

    c1, c2, c3 = st.beta_columns(3)
    with c1:
        if st.checkbox("Display column names"):
            st.table(df.columns)
    with c2:
        if st.checkbox("Display column data types"):
            st.table(df.dtypes.astype(str))
    with c3:
        if st.checkbox("Display data for column:"):
            choice = st.selectbox("Choose column:", tuple(df.columns))
            st.table(df[choice])


    if st.checkbox("Display summary"):
        st.write(df.describe())
