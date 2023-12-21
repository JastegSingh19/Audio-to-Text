from flask import Flask, render_template, request
import whisper
import os
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save_audio', methods=['POST'])
def save_audio():
    if 'audio' in request.files:
        audio_file = request.files['audio']
        if audio_file.filename != '':
            audio_file.save('final_audio.wav')  # Change the path as needed
            return 'Audio saved successfully.', 200
    return 'No audio file received.', 400
@app.route('/transcribe_audio', methods=['POST'])
def transcribe_audio():
    if not (os.path.exists('final_audio.wav')):
        return "No audio file"

    model = whisper.load_model("base")
    result = model.transcribe('final_audio.wav')
    transcription = result["text"]
    print(transcription)
    os.remove('final_audio.wav')
    return transcription

if __name__ == '__main__':
    app.run(debug=True)
