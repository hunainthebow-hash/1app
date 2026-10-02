import time 

import pyautogui
import streamlit as st 
import pywhatkit as kit
import pandas as pd 

st.title("whatsapp Automation")


url=st.text_input(label="Enter Your Url Here" ,value="https://almushaf-15.streamlit.app/")
msg=st.text_area(label="Enter Your Url Here" ,value="Follow Me on this Web")

meriUploadFile=st.file_uploader("Upload a file" ,type=["xlsx"])

if meriUploadFile is not None:

    st.write("Contacts are Uploaded")
    df=pd.read_excel(meriUploadFile)

    st.dataframe(df)

    if st.button("send message "):

        for i,row in df.iterrows():
            phonenNumber=f"+92{row["phone"]}"
            customMessage=f"{msg}\n{url}"

            kit.sendwhatmsg_instantly(phone_no=phonenNumber,message=customMessage,wait_time=35)

            time.sleep(15)
            pyautogui.press("enter")

            time.sleep(15)
            pyautogui.press("enter")
            

    st.success("copyright alright reserved by smasb")