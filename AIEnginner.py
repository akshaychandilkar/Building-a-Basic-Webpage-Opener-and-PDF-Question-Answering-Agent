import subprocess
import platform
import time
import PyPDF2
from PyPDF2 import PdfReader
from transformers import pipeline
import tensorflow.compat.v1 as tf

# Replace tf.losses.sparse_softmax_cross_entropy with tf.compat.v1.losses.sparse_softmax_cross_entropy
tf.losses.sparse_softmax_cross_entropy = tf.compat.v1.losses.sparse_softmax_cross_entropy

def open_webpage(url):
    try:
        if platform.system() == 'Darwin':  # macOS
            subprocess.run(['open', url])
        elif platform.system() == 'Windows':  # Windows
            subprocess.run(['start', url], shell=True)
        else:
            print("Unsupported platform. Please open the URL manually.")
    except Exception as e:
        print(f"Error opening webpage: {e}")

def close_webpage():
    try:
        if platform.system() == 'Darwin':  # macOS
            subprocess.run(['osascript', '-e', 'tell application "System Events" to keystroke "w" using {command down, option down}'])
        elif platform.system() == 'Windows':  # Windows
            subprocess.run(['taskkill', '/F', '/IM', 'chrome.exe'], shell=True)  # Change 'chrome.exe' to the browser's executable if different
        else:
            print("Unsupported platform. Please close the tab manually.")
    except Exception as e:
        print(f"Error closing webpage: {e}")

def read_pdf(pdf_file):
    try:
        with open(pdf_file, 'rb') as file:
            pdf_reader = PdfReader(file)
            pdf_text = ""
            for page_num in range(len(pdf_reader.pages)):
                pdf_text += pdf_reader.pages[page_num].extract_text()
        return pdf_text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None

def answer_question(pdf_text, question):
    try:
        qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad", revision="626af31")
        result = qa_pipeline(question=question, context=pdf_text)
        return result['answer']
    except Exception as e:
        print(f"Error answering question: {e}")
        return None

if __name__ == "__main__":
    print("You: open webpage https://www.example.com")
    open_webpage("https://www.example.com")
    print("Agent: Opening the webpage in your default browser...")
    time.sleep(2)  # Simulate some actions on the webpage
    print("Agent: Webpage opened successfully.")

    print("\nAgent: Performing some actions on the webpage...\n")

    time.sleep(3)  # Simulate some more actions on the webpage

    print("Agent: Closing the webpage in 5 seconds...")
    time.sleep(3)
    close_webpage()
    print("Agent: Webpage closed.")

    print("\nYou: exit")

    pdf_file_path = input("Enter the path to the PDF file: ").strip('"')
    pdf_text = read_pdf(pdf_file_path)
    if pdf_text:
        user_question = input("Ask a question about the PDF content: ")
        answer = answer_question(pdf_text, user_question)
        print("Answer:", answer)
    else:
        print("Error reading PDF.")
