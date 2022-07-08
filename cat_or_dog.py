# -*- coding: utf-8 -*-
"""
Created on Thu mar  7 20:01:05 2022

@author: Golf Blitz
"""

import os
import random

import streamlit as st



def show():
    st.write(
        """
        # 🐾🐾🐾🐾 Cat or Dog 🐾🐾🐾🐾
        
       `st.session_state`!
        """
    )

    
    #abs_file_path = "https://github.com/shafiiftikardwin/diffrentiate_cat_or_dog/tree/main/images/"
    files = "https://github.com/shafiiftikardwin/diffrentiate_cat_or_dog/tree/main/images/"
    if "annotations" not in st.session_state:
        st.session_state.annotations = {}
        st.session_state.files = files
        st.session_state.current_image = "cat.1.jpg"
        st.session_state.true = {}
        

    def annotate(label):
        st.session_state.annotations[st.session_state.current_image] = label
        if label in st.session_state.current_image:
            st.session_state.true = ":tada:true:tada:"
        else:
            st.session_state.true = "🐶false🐱"
        
        if st.session_state.files:
            st.session_state.current_image = random.choice(st.session_state.files)
            st.session_state.files.remove(st.session_state.current_image)
        
        
        
        
            
    image_path = (
        "https://github.com/shafiiftikardwin/diffrentiate_cat_or_dog/tree/main/images/"
        +
        st.session_state.current_image
    )

    st.write("")
    col1, col2 = st.columns(2)
    col1.image(image_path, width = 300)
    with col2:
        if st.session_state.files:
            st.write(
                "### Answered:",
                len(st.session_state.annotations),
                " 🐾🐾   Remaining:",
                len(st.session_state.files),
            )
            st.button(" This is a dog! 🐶", on_click=annotate, args=("dog",))
            st.button(" This is a cat! 🐱", on_click=annotate, args=("cat",))
            st.write("### Your answer is :-  " )
            st.write(st.session_state.true)

        else:
            st.success(
                f"🎈 Done! All {len(st.session_state.annotations)} images annotated."
            )
            

  



if __name__ == "__main__":
    show()
#st.write("### Annotations")
#st.write(st.session_state.annotations)
#st.write("## Your answer is :-  " + st.session_state.true)
#st.write(st.session_state.true)
