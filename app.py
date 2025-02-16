```python
import streamlit as st
st.title("AI Doctor Role-Play Trainer")
st.write("Simulate conversations with an AI Doctor.")
if st.button("Start Role-Play"):
    st.write("Doctor: Why should I prescribe your brand?")
    user_response = st.text_input("Your Response:")
    if user_response:
        st.write("Doctor says: That's interesting, but what makes it better?")
```
