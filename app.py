import os
import logging

import gradio as gr

def greet(name):
    classifier = pipeline("sentiment-analysis")
    a = classifier(i)
    return a


iface = gr.Interface(fn=greet, inputs="text", outputs="text")


iface.launch()
