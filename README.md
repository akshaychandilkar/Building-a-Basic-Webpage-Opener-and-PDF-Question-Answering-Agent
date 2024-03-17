## Task: AI Engineer Intern: Building a Basic Webpage Opener and PDF Question Answering Agent ## 

# The purpose of this Python program is to create a PDF Question Answering (QA) agent with the following functionalities:
# Opening and Closing Webpages: It can open a webpage in the default browser using platform-specific commands open for macOS and ‘start’ for Windows) and close the webpage by simulating actions such as keystrokes or using the ‘ taskkill’ command.
# Reading PDF Text: It reads text from a PDF file using PyPDF2 and extracts the text content from each page to be used for question answering.
# Answering Questions: It uses the Hugging Face Transformers library to implement a question-answering pipeline(‘ pipeline(“question-answering”)’) with a pre-trained model (‘distilbert-base-cased-distilled-squad’) to answer questions based on the PDF text.
# The overall purpose of the program is to demonstrate a basic PDF Question Answering agent that can interact with webpages and provide answers to questions based on the content of a PDF file.
