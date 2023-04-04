import os
import logging

import gradio as gr
import flask

def greet(name):
    print(os.environ.get('test1'))
    logging.error("+++++")
    logging.error(os.environ.get('test'))
    logging.error("-----")
    return "Hello" + name + "!!"
iface = gr.Interface(fn=greet, inputs="text", outputs="text")
iface.launch()
