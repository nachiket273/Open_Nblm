import gradio as gr
import os
import shutil


def upload_file(file):
    UPLOAD_FOLDER = './data'
    if not os.path.exists(UPLOAD_FOLDER):
        os.mkdir(UPLOAD_FOLDER)
    shutil.copy(file, UPLOAD_FOLDER)
    gr.Info("File Uploaded Successfully")


if __name__ == "__main__":
    demo = gr.Interface(
        fn=upload_file,
        inputs=[
            "file"
        ],
        outputs=[]
    )
    demo.launch()
