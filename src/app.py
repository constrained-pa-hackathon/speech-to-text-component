from speech_to_text import main as stt
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/speech_to_text", methods=["POST"])
def speech_to_text():
    print(request.headers)
    print(request.files)
    wav_file = request.files['sentence-audio']
    sentence_text = stt(wav_file)
    sentence_text = {"output_text": sentence_text}
    print(sentence_text)
    return jsonify(sentence_text)

if(__name__ == "__main__"):
    app.run(port=4444)
