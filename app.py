from transformers import pipeline
import gradio as gr


def hello(i):
    


iface = gr.Interface(fn=hello, inputs="text", outputs="text")
iface.launch()
