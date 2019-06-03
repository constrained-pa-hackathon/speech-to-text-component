from speech_to_text import main as stt
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/speech_to_text", methods=["POST"])
def speech_to_text():
    wav_file = request.files['sentence_audio']
    sentence_text = stt(wav_file)
    sentence_text = {"text": sentence_text}
    return jsonify(sentence_text)


app.run(port=4444)