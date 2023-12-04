# import module
import streamlit as st
 
# Title
st.title("Hello GeeksForGeeks !!!")

# Header
st.header("This is a header") 
 
# Subheader
st.subheader("This is a subheader")

# Text
st.text("Hello GeeksForGeeks!!!")

# Markdown
st.markdown("### This is a markdown")

# success
st.success("Success")
 
# success
st.info("Information")
 
# success
st.warning("Warning")
 
# success
st.error("Error")
 
# Exception - This has been added later
exp = ZeroDivisionError("Trying to divide by Zero")
st.exception(exp)

# Write text
st.write("Text with write")
 
# Writing python inbuilt function range()
st.write(range(10))

# Display Images
 
# import Image from pillow to open images
from PIL import Image
img = Image.open("streamlit.png")
 
# display image using streamlit
# width is used to set the width of an image
st.image(img, width=200)

# checkbox
# check if the checkbox is checked
# title of the checkbox is 'Show/Hide'
if st.checkbox("Show/Hide"):
 
    # display the text if the checkbox returns True value
    st.text("Showing the widget")
    
# radio button
# first argument is the title of the radio button
# second argument is the options for the radio button
status = st.radio("Select Gender: ", ('Male', 'Female'))
 
# conditional statement to print 
# Male if male is selected else print female
# show the result using the success function
if (status == 'Male'):
    st.success("Male")
else:
    st.success("Female")
    
# Selection box
 
# first argument takes the titleof the selectionbox
# second argument takes options
hobby = st.selectbox("Hobbies: ",
                     ['Dancing', 'Reading', 'Sports'])
 
# print the selected hobby
st.write("Your hobby is: ", hobby)

# multi select box
 
# first argument takes the box title
# second argument takes the options to show
hobbies = st.multiselect("Hobbies: ",
                         ['Dancing', 'Reading', 'Sports'])
 
# write the selected options
st.write("You selected", len(hobbies), 'hobbies')

# Create a simple button that does nothing
st.button("Click me for no reason")
 
# Create a button, that when clicked, shows a text
if(st.button("About")):
    st.text("Welcome To GeeksForGeeks!!!")
    
# Text Input
 
# save the input text in the variable 'name'
# first argument shows the title of the text input box
# second argument displays a default text inside the text input area
name = st.text_input("Enter Your name", "Type Here ...")
 
# display the name when the submit button is clicked
# .title() is used to get the input text string
if(st.button('Submit')):
    result = name.title()
    st.success(result)
    st.text("Sucessful Submited")
    
# text Input
# first_name = st.text_input("Enter your first name", "Type here..")
# if st.button("Submit", key="1"):
#     result = first_name.title()
#     st.success(result)

# Radio Buttons
status = st.radio("What is your Status", ("Active", "Inactive"))
    
# Link with some function
# if status == "Active":
#     st.success("You are Active")

#if Else function
if status == "Active":
    st.success("You are Active")
else:
    st.warning("Inactive, Activate it")
    
# Slider
lelvel = st.slider("What is your level", 1,5)

# Text Area
message = st.text_area("Enter your message", "Type here..")
if st.button("Submit", key = "2"):
    result = message.title()
    st.success(result)

# Date Input
import datetime
today = st.date_input("Today is", datetime.datetime.now())

# Time
the_time = st.time_input("The time is", datetime.time())
st.success(the_time)

#Display Json Output
st.text("Display json Data")
st.json({"Name":"Shivan",
        "Gender":"Male"})

# IMport numpy as np
st.text("Display Row Code")
st.code("import numpy as np")

# Display row code with dataframe
with st.echo():
    import pandas as pd
    df = pd.DataFrame()

# Progress bar

import time
my_bar = st.progress(0)
for p in range(10):
    my_bar.progress( p + 10)

#spinner

with st.spinner("Watinig .."):
    time.sleep(5)
st.success("Finished!")

