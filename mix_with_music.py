import os
from pydub import AudioSegment

base_dir = "change it to your base directory adress"

try:
    # Load voiceover and background music
    voice = AudioSegment.from_mp3(os.path.join(base_dir, "farsi_text_full.mp3"))
    music = AudioSegment.from_mp3(os.path.join(base_dir, "background_music.mp3"))

    # Adjust volumes
    voice = voice + 6  # make voice slightly louder
    music = music - 15  # reduce music volume (make it background)

    # Loop music if shorter than voice
    while len(music) < len(voice):
        music += music

    # Trim music to length of voice
    music = music[:len(voice)]

    # Overlay
    final_mix = music.overlay(voice)

    # Export final mixed MP3
    output_path = os.path.join(base_dir, "farsi_text_full_with_music.mp3")
    final_mix.export(output_path, format="mp3")
    print(f"✅ Mixed version saved with background music: {output_path}")

except Exception as e:
    print(f"Error: {e}") 
