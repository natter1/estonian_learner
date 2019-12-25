from gtts import gTTS
from io import BytesIO

# tts = gTTS('hello')
# tts.save('hello.mp3')
word = "olema"
tts = gTTS(word, lang="et")
tts.save(word + ".mp3")

mp3_fp = BytesIO()
tts.write_to_fp(mp3_fp)

from pydub import AudioSegment
from pydub.playback import play

# simpleaudio needs to be installed for playback but not imported
#import simpleaudio.functionchecks as fc
#fc.LeftRightCheck.run()

# song = AudioSegment.from_wav("3.wav")
song = AudioSegment.from_mp3(word+".mp3")
# song.export("3.wav", format="wav")
play(song)


