import streamlit as st
st.write("Hello ,let's learn how to build a streamlit app together")
st.title ("this is the app title")
st.header("this is the markdown")
st.markdown("this is the header")
st.subheader("this is the subheader")
st.caption("this is the caption")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')

# Method 1: Using st.selectbox
selected_option_1 = st.selectbox("Select Option 1", ["Option 1", "Option 2", "Option 3"])

# Method 2: Using st.selectbox with a default option
options = ["Option A", "Option B", "Option C"]
default_option = options[0]
selected_option_2 = st.selectbox("Select Option 2", options, index=options.index(default_option))

# Display the selected options
st.write("You selected:", selected_option_1, "using Method 1")
st.write("You selected:", selected_option_2, "using Method 2")