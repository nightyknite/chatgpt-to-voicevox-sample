
from pathlib import Path
from voicevox_core import VoicevoxCore, METAS
import simpleaudio, tempfile

def speak(text, speaker_id):
    file_path = "output.wav"
    core = VoicevoxCore(open_jtalk_dict_dir=Path("open_jtalk_dic_utf_8-1.11"))
    if not core.is_model_loaded(speaker_id):
        core.load_model(speaker_id)
    wave_bytes = core.tts(text, speaker_id)
    with tempfile.TemporaryDirectory() as tmp:
        with open(f"{tmp}/{file_path}", "wb") as f:
            f.write(wave_bytes)
            # wavファイルを再生する
            wav_obj = simpleaudio.WaveObject.from_wave_file(f"{tmp}/{file_path}")
            play_obj = wav_obj.play()
            play_obj.wait_done()

if __name__ == "__main__": 
    speak("犬はなんと鳴きますか？", 0)