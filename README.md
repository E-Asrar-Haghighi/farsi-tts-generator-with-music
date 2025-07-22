# Farsi Text-to-Speech Generator (with Optional Background Music)

This project converts Farsi (Persian) text from a `.txt` file into natural-sounding speech using OpenAI's TTS API, and combines the audio into a single MP3 file. Optionally, you can mix the generated voiceover with background music for a richer audio experience.

## Features
- Reads Farsi text from a UTF-8 `.txt` file
- Splits long text into chunks for TTS API limits
- Generates MP3 audio for each chunk
- Merges all audio into one final MP3
- Logs chunk boundaries and handles errors
- **Optional:** Mixes the final voiceover with background music

## Requirements
- Python 3.8+
- OpenAI API key
- [ffmpeg](https://ffmpeg.org/) (required by pydub for audio processing)

## Setup
1. **Clone or download this repository.**
2. **Create and activate a virtual environment:**
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate
   ```
3. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```
4. **Set your OpenAI API key:**
   - Create a `.env` file in the project directory with this line:
     ```
     OPENAI_API_KEY=your-openai-api-key-here
     ```
5. **(Optional) Install ffmpeg:**
   - Download and install ffmpeg from [ffmpeg.org](https://ffmpeg.org/download.html) and ensure it is in your system PATH.

## Usage
### 1. Generate Voiceover from Farsi Text
1. Place your Farsi text in `farsi_text.txt` (UTF-8 encoding recommended).
2. Run the script:
   ```powershell
   python farsi_text_to_voice.py
   ```
3. The script will:
   - Split the text into chunks (if needed)
   - Generate `part1.mp3`, `part2.mp3`, ... in the project directory
   - Merge them into `farsi_text_full.mp3`

### 2. Mix Voiceover with Background Music (Optional)
1. Place your background music file as `background_music.mp3` in the project directory.
2. Run the mixing script:
   ```powershell
   python mix_with_music.py
   ```
3. The script will:
   - Adjust the volume of the voice and music
   - Loop and trim the music to match the voiceover length
   - Overlay the voice onto the music
   - Export the result as `farsi_text_full_with_music.mp3`

## Input/Output
- **Input:**
  - `farsi_text.txt` (Farsi text)
  - `background_music.mp3` (optional, for mixing)
- **Output:**
  - `part1.mp3`, `part2.mp3`, ... (audio chunks)
  - `farsi_text_full.mp3` (final combined audio)
  - `farsi_text_full_with_music.mp3` (final mix with background music)

## Troubleshooting
- Make sure your `.txt` file is UTF-8 encoded.
- If you get API errors, check your OpenAI API key and internet connection.
- If the audio is incomplete, check the script output for chunk logs and errors.
- If you get errors related to audio processing, ensure ffmpeg is installed and available in your PATH.

## License
This project is licensed under the MIT License. 

**Note:**
Use of the OpenAI API is subject to OpenAI’s own terms of service. You are responsible for ensuring compliance with those terms. 