import logging

import gradio as gr

def hello(i):
    logging.error("log fail test")
    return "hello"


iface = gr.Interface(fn=hello, inputs="text", outputs="text")
iface.launch()
