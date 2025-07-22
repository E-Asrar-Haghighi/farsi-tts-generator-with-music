import openai
from dotenv import load_dotenv
import os
from pydub import AudioSegment

# Set base directory for all file operations
base_dir = r"C:\Users\lasra\Desktop\Youtube_voice_to_farsi"

# Load API key from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Read text from file
input_path = os.path.join(base_dir, "farsi_text.txt")
with open(input_path, "r", encoding="utf-8") as file:
    full_text = file.read()

# Improved split_text: split by paragraphs for natural breaks
# and log chunk boundaries and lengths

def split_text(text, max_chars=4096):
    paragraphs = text.split('\n\n')  # Split by paragraphs
    chunks, current = [], ""
    for para in paragraphs:
        if len(current) + len(para) + 2 <= max_chars:
            current += para + "\n\n"
        else:
            if current:
                chunks.append(current.strip())
            current = para + "\n\n"
    if current:
        chunks.append(current.strip())
    return chunks

chunks = split_text(full_text)

# Log chunk boundaries and lengths
for idx, chunk in enumerate(chunks):
    print(f"Chunk {idx+1}: {len(chunk)} characters\n{repr(chunk[:100])}...\n")

# Generate and save each chunk with error handling
output_files = []
for idx, chunk in enumerate(chunks):
    try:
        response = openai.audio.speech.create(
            model="tts-1",
            voice="onyx",  # male-sounding, soothing
            input=chunk
        )
        filename = os.path.join(base_dir, f"part{idx + 1}.mp3")
        with open(filename, "wb") as f:
            f.write(response.content)
        output_files.append(filename)
        print(f"Saved: {filename}")
    except Exception as e:
        print(f"Error processing chunk {idx+1}: {e}")

# Merge all MP3 files into one
final = AudioSegment.empty()
for filename in output_files:
    final += AudioSegment.from_mp3(filename)

# Export combined file
final_output = os.path.join(base_dir, "farsi_text_full.mp3")
final.export(final_output, format="mp3")
print(f"✅ Done! Saved as {final_output}") 