from transformers import pipeline
import gradio as gr


def hello(i):
    return "dev-new"



iface = gr.Interface(fn=hello, inputs="text", outputs="text")
iface.launch()
