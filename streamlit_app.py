import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Príprava dát
data = {
    'Čas': pd.date_range(start='2023-01-01', periods=10, freq='D'),
    'Hodnota': np.random.randint(1, 100, size=10)
}
df = pd.DataFrame(data)

# Rozdelenie na dva stĺpce
col1, col2 = st.columns(2)


# Prvý stĺpec - tabuľka
with col1:
    st.header("Tabuľka údajov")
    st.dataframe(df)

# Druhý stĺpec - graf
with col2:
    st.header("Graf údajov")
    plt.plot(df['Čas'], df['Hodnota'], marker='o')
    plt.title("Graf Hodnôt")
    plt.xlabel("Čas")
    plt.ylabel("Hodnota")
    st.pyplot(plt)


user = st.secrets["p_user"]
db_password = st.secrets["p_password"]


st.write(f"DB Username: {user}")

