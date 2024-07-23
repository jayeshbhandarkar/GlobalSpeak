import os
from flask import Flask, render_template, request, jsonify, redirect
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import speech_recognition as sr
import json
from moviepy.editor import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

languages = {"afrikaans": "af", "albanian": "sq", "amharic": "am", "arabic": "ar", "armenian": "hy", "azerbaijani": "az",
             "basque": "eu", "belarusian": "be", "bengali": "bn", "bosnian": "bs", "bulgarian": "bg",
             "catalan": "ca", "cebuano": "ceb", "chichewa": "ny", "chinese (simplified)": "zh-cn", "chinese (traditional)": "zh-tw",
             "corsican": "co", "croatian": "hr", "czech": "cs", "danish": "da", "dutch": "nl",
             "english": "en", "esperanto": "eo", "estonian": "et", "filipino": "tl", "finnish": "fi",
             "french": "fr", "frisian": "fy", "galician": "gl", "georgian": "ka", "german": "de",
             "greek": "el", "gujarati": "gu", "haitian creole": "ht", "hausa": "ha", "hawaiian": "haw",
             "hebrew": "he", "hindi": "hi", "hmong": "hmn", "hungarian": "hu", "icelandic": "is",
             "igbo": "ig", "indonesian": "id", "irish": "ga", "italian": "it", "japanese": "ja",
             "javanese": "jw", "kannada": "kn", "kazakh": "kk", "khmer": "km", "korean": "ko",
             "kurdish (kurmanji)": "ku", "kyrgyz": "ky", "lao": "lo", "latin": "la", "latvian": "lv",
             "lithuanian": "lt", "luxembourgish": "lb", "macedonian": "mk", "malagasy": "mg", "malay": "ms",
             "malayalam": "ml", "maltese": "mt", "maori": "mi", "marathi": "mr", "mongolian": "mn",
             "myanmar (burmese)": "my", "nepali": "ne", "norwegian": "no", "odia": "or", "pashto": "ps",
             "persian": "fa", "polish": "pl", "portuguese": "pt", "punjabi": "pa", "romanian": "ro",
             "russian": "ru", "samoan": "sm", "scots gaelic": "gd", "serbian": "sr", "sesotho": "st",
             "shona": "sn", "sindhi": "sd", "sinhala": "si", "slovak": "sk", "slovenian": "sl",
             "somali": "so", "spanish": "es", "sundanese": "su", "swahili": "sw", "swedish": "sv",
             "tajik": "tg", "tamil": "ta", "telugu": "te", "thai": "th", "turkish": "tr",
             "ukrainian": "uk", "urdu": "ur", "uyghur": "ug", "uzbek": "uz", "vietnamese": "vi",
             "welsh": "cy", "xhosa": "xh", "yiddish": "yi", "yoruba": "yo", "zulu": "zu"}

@app.route('/text_translate', methods=['GET', 'POST'])
def translate_text():
    """ Translate text from source language to target language

    Keyword arguments:
    Return: translated text in .json format which is later fetched by connector.js
    """

    print("inside translate_text")
    text = ""
    target = ""
    print("request.form: ", request.form)
    text = request.form.get('user_text')
    target = request.form.get('target_language')

    print(text, target)
    unicodeData = text_translator(text, target)
    data = {'text': unicodeData}
    encodedUnicode = json.dumps(data, ensure_ascii=False)
    return (encodedUnicode)
    # return render_template('index.html', result=encodedUnicode)

@app.route('/audio_translate', methods=['GET', 'POST'])
def audio_transcript():
    """ Return translated audio from source language to target language
        and generate audio file as well as text file

    Returns:
        dict: dictionary containing translated text in json format. 
        This is later fetched by connector.js
    """

    print("inside audio_transcript")
    print("request.form: ", request.form)
    target = request.form.get('target_language')
    if "file" not in request.files:
        print("No file 1")
        return redirect(request.url)

    file = request.files["file"]
    if file.filename == "":
        print("No file")
        return redirect(request.url)

    target = languages[target].lower()
    print(file, target)
    transcript = ""
    # os.save(filename= 'static\\translated_audio\\original.mp3',
    #         ignore_discard=False, ignore_expires=False)
    if file:
        print("transciption")
        recognizer = sr.Recognizer()
        audioFile = sr.AudioFile(file)
        with audioFile as source:
            data = recognizer.record(source)
        transcript = recognizer.recognize_google(data, key=None)
    print(transcript)
    ans = text_translator(transcript, target)
    audio_translator(ans, target)
    print('printing ans')
    data = {'text': ans}
    encodedUnicode = json.dumps(data, ensure_ascii=False)
    return (encodedUnicode)
    # return render_template('audio_translate.html', ans=ans)

@app.route('/video_translate', methods=['GET', 'POST'])
def translate_video():
    print("inside video_transcript")
    print("request.form: ", request.form)
    target = request.form.get('target_language')
    if "file" not in request.files:
        print("No file 1")
        return redirect(request.url)

    file = request.files["file"]
    if file.filename == "":
        print("No file")
        return redirect(request.url)

    target = languages[target].lower()
    print(file, target)
    file.save(r'static/audio_from_video/original.mp4')
    print("file saved")
    videoclip = VideoFileClip(r'static/audio_from_video/original.mp4')
    # Insert Local Audio File Path
    videoclip.audio.write_audiofile(r"static/audio_from_video/audio.wav", codec='pcm_s16le')
    print("audio extracted")
    video_translator(r'static/audio_from_video/audio.wav', target, videoclip)
    return {'text': 'success'}

def video_translator(file, target, videoclip):
    transcript = ""
    r = sr.Recognizer()
    with sr.AudioFile(file) as source:
        audio = r.record(source)    # read the entire audio file
    transcript = r.recognize_google(audio, key=None)
    translated_text = text_translator(transcript, target)
    translated_audio = gTTS(text=translated_text, lang=target, slow=False)
    translated_audio.save(r'static/audio_from_video/translated_audio.wav')
    audioclip = AudioFileClip(r'static/audio_from_video/translated_audio.wav')

    # adding audio to the video clip
    new_audioclip = CompositeAudioClip([audioclip])
    videoclip.audio = new_audioclip
    videoclip.write_videofile(r"static/audio_from_video/translated_video.mp4")
    
def audio_translator(text, target):
    print("inside audio traslate")
    """ Translate audio from source language to target language

    Args:
        text (str): transcription of audio file in source language
        target (str): target language for translation

    Returns (none): It generates audio file in target language and stores it locally
    """
    try:
        speak = gTTS(text=text, lang=target, slow=False)
    except:
        print("error")
    speak.save(r"static/translated_audio/captured_voice.mp3")

def text_translator(text, target):
    """Translate given text to target language

    Args:
        text (str): text to be translated
        target (str): target language

    Returns:
        str: translated text
    """
    print(target)
    translator = Translator()
    translation = translator.translate(text, dest=target)
    translated_text = translation.text
    print(target)
    print(translation.text)
    return translated_text

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
    