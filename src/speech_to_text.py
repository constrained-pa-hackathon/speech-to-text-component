import speech_recognition as sr
import pocketsphinx as ps
import pyaudio as pa
import json

def main(aud):
    rec = sr.Recognizer()
    json_text = rec.recognize_google(aud)
    print(json_text)
    # sentence = rec.recognize_google(aud)
    # sentence_dict = {'sentence': sentence}
    # print(json.dumps(sentence_dict))
    return json_text


if __name__ == '__main__':
    main()