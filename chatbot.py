import google.generativeai as genai
import gradio as gr
import os
from dotenv import load_dotenv

class ChatBot:
    def __init__(self):
        load_dotenv()  # Load environment variables
        self.model_name = "gemini-1.5-flash"
        self.api_key = os.getenv("GOOGLE_API_KEY")
        
        genai.configure(api_key=self.api_key)
        self.load_model()
    
    def load_model(self):
        self.llm = genai.GenerativeModel(model_name=self.model_name)

    def chat_bot(self, message, img):
        if not message and not img: 
            return "Plz provides text and/or image to get best result!!!"


        inputs =[]
        if message:
            inputs.append(message)

        else:
            inputs.append("Describe Image : ")

        if img:
            inputs.append(img)

        response = self.llm.generate_content(inputs)
        return response.text

if __name__ == "__main__":
    chatbot = ChatBot()
    # gr.ChatInterface(chatbot.chat_bot).launch(share=True)

    app = gr.Interface(
        fn = chatbot.chat_bot,
        inputs = [
                    gr.Textbox(lines = 5,            
                            placeholder="Ask your question??", 
                            label="Text"), 
                    gr.Image(type='pil',
                                label="Image"),
                ],
        outputs = "text",
        description = "Upload your question and an image to generate caption!!!",
        title = "Multitasking ChatBot"
    )

    app.launch(share = True)

