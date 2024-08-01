import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
col1, col2 = st.columns([2, 3])

with col1:
    st.image("images/photo.png")
with col2:
    st.title("About this page")
    content = """
Lorem ipsum odor amet, consectetuer adipiscing elit. 
Porta senectus ridiculus interdum velit elementum magna sollicitudin ex! Lorem fames convallis urna morbi, quam facilisi semper. 
Semper cubilia hac parturient ornare elit duis elit praesent ullamcorper. Eros sit aliquet fusce sociosqu in pellentesque tellus porta. 
Dis sed phasellus mus ligula tortor egestas. Fames potenti efficitur tempus cursus est; arcu sollicitudin dictum. Congue nam quis; efficitur magna potenti imperdiet.
"""
    st.info(content)

st.write(
    "Below you can find some of the apps I have built with python. Feel free to contact."
)

df = pd.read_csv("data.csv", sep=";")

col3, col4 = st.columns(2)
with col3:
    for _, row in df[0::2].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row["url"]})")

with col4:
    for _, row in df[1::2].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row["url"]})")

