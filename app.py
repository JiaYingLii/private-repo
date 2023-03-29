from transformers import pipeline
import gradio as gr
import sys


def hello(i):
    print("run fail test")
    sys.exit(-1)


iface = gr.Interface(fn=hello, inputs="text", outputs="text")
iface.launch()
