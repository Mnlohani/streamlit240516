import streamlit as st

st.header("Our first streamlit App video :sunglasses:", divider="rainbow")

st.subheader("Wow streamlit is so cool")
st.markdown(
    """
    :red[We] :orange[can] :green[see] :blue[Homer] :violet[dancing]
    :gray[in] :rainbow[streamlit] and :blue-background[in 5 secs]"""
)

st.write("Wooohooo!!!!")

st.video("https://www.youtube.com/watch?v=LeMlMCOam9w")
