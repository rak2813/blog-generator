import streamlit as st 
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
from langchain.llms import HuggingFaceHub

import os 
os.environ['HUGGINGFACEHUB_API_TOKEN'] = "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"

def getLLamaResponse(input, words, style): 
    llm=CTransformers(model='llama-2-7b-chat.ggmlv3.q5_0.bin',
                      model_type='llama',
                      config={'max_new_tokens':256,
                              'temperature':0.01})

    template = "Write an informative blog on the topic {input} intended for {style} in {words} words."
    prompt = PromptTemplate(input_variables=["input", "style", "words"], template=template)
    response = llm(prompt.format(input=input, words=words, style=style))
    print(response)
    return response

st.set_page_config(page_title="Blog Generator", layout="centered", initial_sidebar_state="collapsed")
st.header("Generate Blogs")
input = st.text_input("Write a topic")
col1, col2 = st.columns([5,5])
with col1:
    words = st.text_input("No. of words")

with col2:
    style = st.selectbox('Blog is for', ("Researchers", "College Students", "Children"), index=0)

submit = st.button("Generate")
if submit:
    st.write(getLLamaResponse(input, words, style))
    