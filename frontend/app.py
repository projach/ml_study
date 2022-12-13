import streamlit as st
from  PIL import Image

first_prediction = "90% Ragdoll"
second_prediction = "5% Maine Coon Cat"
third_prediction = "5% Persian"

st.set_page_config(page_title="Cat breed classification", page_icon=":cat:",layout="wide",)

with st.container():
    st.markdown("<h2 style='text-align: center; padding-top: 0px; margin-top: 0px;'>This is a dissertation project that classifies cat breeds with machine learning</h2>", 
    unsafe_allow_html=True)

with st.container():
    st.write("---")
    left_column, middle_column, right_column = st.columns([2,1,3])


    with left_column:
        slider_1_value = st.slider(
        'Select a range of values', 0, 100, 35)
        st.write('value:', slider_1_value)

        slider_2_value  = st.slider(
        'Select a range of values', 0, 100, 15)
        st.write('value:', slider_2_value)

        slider_3_value = st.slider(
        'Select a range of values', 0, 100, 25)
        st.write('value:', slider_3_value)

        algorithm_option = st.selectbox(
        'Select the algorithm you want to use',
        ('algorithm 1', 'Algorithm 2', 'algorithm 3'))

    

    with right_column:
        holder_photo = st.empty()
        holder_button = st.empty()
        cat_photo = holder_photo.file_uploader('Upload a png or a jpg photo of a cat', type=['png', 'jpg'])
        start = holder_button.button("press when you are ready")
        if start:
            holder_button.empty()
            holder_photo.empty()
        if cat_photo is not None:
            image = Image.open(cat_photo)
            st.image(image,width=300)
                  
        st.markdown(f"<h3 style='text-align: left;'>{first_prediction}</h3>", 
        unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align: left;'>{second_prediction}</h3>", 
        unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align: left;'>{third_prediction}</h3>", 
        unsafe_allow_html=True)
                
                
        



