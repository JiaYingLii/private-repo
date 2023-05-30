import os
import logging
from transformers import pipeline


import gradio as gr

def greet(name):
    classifier = pipeline("sentiment-analysis")
    a = classifier(name)
    return a


print("--------print env-----------")
print("http_proxy: " + os.getenv('http_proxy'))
print("https_proxy: " + os.getenv('https_proxy'))
print("no_proxy: " + os.getenv('no_proxy'))
iface = gr.Interface(fn=greet, inputs="text", outputs="text")


iface.launch()

