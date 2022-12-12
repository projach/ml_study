import streamlit as st

st.set_page_config(page_title="Cat breed classification", page_icon=":cat:",layout="wide",)

with st.container():
    st.markdown("<h2 style='text-align: center; padding-top: 0px; margin-top: 0px;'>This is a dysertation project that classifies cat breeds with machine learning</h1>", 
    unsafe_allow_html=True)

with st.container():
    st.write("---")
    left_column, middle_column, right_column = st.columns([1,2,3])
    with left_column:
        slider_1_value = st.slider(
        'Select a range of values', 0, 100, 35)
        st.write('slider_1_value:', slider_1_value)

        slider_2_value  = st.slider(
        'Select a range of values', 0, 100, 15)
        st.write('slider_2_value:', slider_2_value)

        slider_3_value = st.slider(
        'Select a range of values', 0, 100, 25)
        st.write('slider_3_value:', slider_3_value)

        algorithm_option = st.selectbox(
        'Select the algorithm you want to use',
        ('algorithm 1', 'Algorithm 2', 'algorithm 3'))
    with right_column:
        st.file_uploader('Upload a png or a jpg photo of a cat', type=['png', 'jpg'], accept_multiple_files=False, key="cat_photo", help=None, on_change=None, args=None, kwargs=None, disabled=False)

