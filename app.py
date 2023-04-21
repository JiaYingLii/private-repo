import os
import logging
from transformers import pipeline


import gradio as gr

def greet(name):
    classifier = pipeline("sentiment-analysis")
    a = classifier(name)
    return a


iface = gr.Interface(fn=greet, inputs="text", outputs="text")



iface.launch()

