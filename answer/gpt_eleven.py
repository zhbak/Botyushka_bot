from dotenv import load_dotenv
from openai import OpenAI
from elevenlabs import generate, save
import os

# подгружаем ключи
load_dotenv()
client = OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY_BIBLE")
)

# Функция задающая prompt
def gpt_message(content):
    gpt_message = "{}\n".format(content) + \
                """
                - ответь как православный священик;
                - процитируй Библию    
                """
    message = [
        {
            "role" : "user",
            "content" : gpt_message
        }
    ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=message,
        temperature=0.4
    )

    print("GPT output made")

    return response.choices[0].message.content

# Функция генерирующая аудио
def audio_generation(gpt_output):
    print("Audio is generating")
    audio = generate(
                    api_key=os.environ.get("ELEVEN_KEY"),
                    text=gpt_output,
                    voice="Thomas",
                    model="eleven_multilingual_v2"
    )
    print("Audio generated")
    save(audio, "audio.mp3")
    print("Audio file saved")