# Audio Transcription Web App

This Flask web application utilizes Whisper for audio transcription. It allows users to record audio, upload audio files, and transcribe them into text.

## Installation

1. Clone or download the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the Flask application using `python app.py`.

## Usage

- Access the web app through the browser.
- Use the provided interface to:
  - Record audio.
  - Upload audio files.
  - Transcribe uploaded or recorded audio into text.

## Routes

- **/** - Homepage with the main interface.
- **/save_audio** (POST) - Endpoint to save the uploaded audio file.
- **/transcribe_audio** (POST) - Endpoint to transcribe the saved audio file into text.

## Technologies Used

- Flask: Micro web framework for Python.
- Whisper: Library for audio transcription.

## Contributing

Feel free to contribute by forking the repository and creating pull requests with your enhancements or bug fixes.

## License

This project is licensed under [MIT License](LICENSE).
