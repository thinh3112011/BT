import google.generativeai as genai
from gtts import gTTS
import pygame
import time
import os

genai.configure(api_key="AIzaSyCdHc-9cc3cBiWwxNoE9oKAW1eCO0A2mQk")

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 250,
    "response_mime_type": "text/plain"
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config
)

pygame.mixer.init()

def speak(text, lang='vi'):
    temp_path = os.path.join(os.getcwd(), "temp_audio.mp3")

    tts = gTTS(text=text, lang=lang)
    tts.save(temp_path)

    pygame.mixer.music.load(temp_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    pygame.mixer.music.unload()  
    os.remove(temp_path)


# Các chức năng chính
def feat1():
    print("mô tả khung cảnh")
    speak("Đây là chức năng mô tả khung cảnh")

def feat2():
    print("đọc văn bản")
    speak("Đây là chức năng đọc văn bản")

def feat3():
    print("tìm đồ vật")
    speak("Đây là chức năng tìm đồ vật")

context = """Tôi có một câu yêu cầu từ người dùng, hãy giúp tôi phân loại chức năng và chỉ trả về đúng một số. Nếu không phân loại được trả về 0:
0. không phân loại được
1. mô tả khung cảnh
2. đọc văn bản
3. tìm đồ vật
yêu cầu: """

while True:
    n = input("input: ")

    if n == "0" or n.lower() == "stop":
        speak("Tạm biệt")
        break

    response = model.generate_content(context + n)
    response_option = response.text.strip()

    if response_option == "1":
        feat1()
    elif response_option == "2":
        feat2()
    elif response_option == "3":
        feat3()
    else:
        print("không phân loại được")
        speak("Tôi không phân loại được yêu cầu này, vui lòng thử lại.")
