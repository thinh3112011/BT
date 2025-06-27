import google.generativeai as genai
genai.configure(api_key="AIzaSyCdHc-9cc3cBiWwxNoE9oKAW1eCO0A2mQk")

generation_config = {
    "temperature":1,
    "top_p":0.95,
    "top_k":64,
    "max_output_tokens":250,
    "response_mime_type":"text/plain"
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config
)

def feat1():
    print("mô tả khung cảnh")
def feat2():
    print("đọc văn bản")
def feat3():
    print("tìm đồ vật")

context = """tôi có một câu yêu cầu từ người dùng hãy giúp tôi phân loại chức năng và chỉ trả về đúng một số. Nếu không phân loại được trả về 0: 
0. không phân loại được
1. mô tả khung cảnh
2. đọc văn bản
3. tìm đồ vật
yêu cầu: """
while True:
    n = input("input: ")

    if n == "0" or n == "stop":
        break

    response = model.generate_content(context + n)
    response_option = response.text.strip()
    #print(response.text.strip())
    if   response_option == "1":
        feat1()
    elif response_option == "2":
        feat2()
    elif response_option == "3":
        feat3()
    else:
        print("không phân loại được")
    
    