import openai
openai_api_key = "####"
completion_response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Give me 3 ideas for apps I could build with OpenAI APIs"}])
print(completion_response.choices[0].message.content)
import openai
openai_api_key = "####"
chat_messages = []
system_prompt = input("What type of chatbot would you like to create?\n")
chat_messages.append({"role": "system", "content": system_prompt})
print("Your new chat assistant is ready!")
while input != "quit()":
    user_input = input()
    chat_messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=chat_messages)
    chatbot_reply = response["choices"][0]["message"]["content"]
    chat_messages.append({"role": "assistant", "content": chatbot_reply})
    print("\n" + chatbot_reply + "\n")
import openai
import gradio
openai_api_key = "####"
chat_messages = [{"role": "system", "content": "You are a financial expert specializing in real estate investment and negotiation"}]
def custom_chat_gpt(user_input):
    chat_messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=chat_messages)
    chat_gpt_reply = response["choices"][0]["message"]["content"]
    chat_messages.append({"role": "assistant", "content": chat_gpt_reply})
    return chat_gpt_reply
demo_interface = gradio.Interface(fn=custom_chat_gpt, inputs="text", outputs="text", title="Real Estate Pro Chatbot")
demo_interface.launch(share=True)

