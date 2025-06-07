from django.shortcuts import render
from google import genai
import speech_recognition as sr
from gtts import gTTS 
import pygame


# Create your views here.
def home(request):
    return render(request,'index.html')


def sendmsg(request):
    msg=request.GET['chat']
    client = genai.Client(api_key="AIzaSyBKDGnj7enfnEMUf-AD1lhIdIeE6XBsRvM")

    response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=msg,
)
    return render(request,'index.html',{'ans':response.text})

def sendvoice(request):
    r = sr.Recognizer()
    with  sr.Microphone() as source:
        print("Talk")
        audio_text = r.listen(source)
        try:
            txt=r.recognize_google(audio_text, language='my-MM')
            print(txt)
            client = genai.Client(api_key="AIzaSyBKDGnj7enfnEMUf-AD1lhIdIeE6XBsRvM")
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=txt,
            )
            pygame.mixer.init()
            sound_file = "sound_file.mp3"
            text_to_speech = gTTS(text=response.text, lang='my')
            text_to_speech.save(sound_file)
            sound = pygame.mixer.Sound(sound_file)
            sound.play()
            while pygame.mixer.get_busy(): 
                pygame.time.delay(100)
            return render(request,'index.html',{'ans':response.text})
        except:
 
            print("Sorry, I did not get that")
    return render(request,'index.html')