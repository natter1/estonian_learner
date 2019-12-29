# pydub seems to need simpleaudio module for playback to work
from gtts import gTTS
from io import BytesIO
# import ffmpeg
# import scipy
from pydub import AudioSegment
from pydub.playback import play

word = "olema"
tts = gTTS(word, lang="et")
# tts.save(word + ".mp3")

mp3_fp = BytesIO()
tts.write_to_fp(mp3_fp)
mp3_fp.seek(0)  # !!!


# simpleaudio needs to be installed for playback but not imported
#import simpleaudio.functionchecks as fc
#fc.LeftRightCheck.run()

# song = AudioSegment.from_mp3(word+".mp3")
# song.export("3.wav", format="wav")
# song = AudioSegment.from_file(word+".mp3")

song = AudioSegment.from_file(mp3_fp, format="mp3")
play(song)

# import simpleaudio as sa
#sa.PlayObject(mp3_fp)