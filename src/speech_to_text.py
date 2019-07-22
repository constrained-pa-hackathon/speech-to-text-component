import speech_recognition as sr
import json
#import time
import datetime as dt

def main(octet_stream):
    time_stamp = dt.datetime.now()
    my_audio_file_name = "audio_%s.wav"%(time_stamp.strftime("%Y-%m-%d--%H-%M-%S"))
    my_audio_file_name = "audio3.wav"
    rec = sr.Recognizer()
    byte_array = bytearray(octet_stream.stream.read())
    new_file = open(my_audio_file_name, 'wb')
    new_file.write(byte_array)
    new_file.close()
    new_file = sr.AudioFile(my_audio_file_name)
    with new_file as src:#my_audio_file_name) as src:
        audio = rec.record(src)
        json_text = " "
        try:
            json_text = rec.recognize_google(audio, language = 'en-US')
        except:
            json_text = " " 
        return json_text
    return None
    # sentence = rec.recognize_google(aud)
    # sentence_dict = {'sentence': sentence}
    # print(json.dumps(sentence_dict))



if __name__ == '__main__':
    main()
