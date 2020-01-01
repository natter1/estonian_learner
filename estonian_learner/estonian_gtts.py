"""
@author: Nathanael Jöhrmann
"""

# pydub seems to need simpleaudio module installed (not imported) for playback to work
from io import BytesIO

from gtts import gTTS
# import ffmpeg
# import scipy
from pydub import AudioSegment
from pydub.playback import play


def main():
    text = "olema"
    mp3_fp = gtts_as_mp3_bytes_io(text)

    song = AudioSegment.from_file(mp3_fp, format="mp3")
    play(song)


def gtts_as_mp3_bytes_io(text: str, language: str = "et") -> BytesIO:
    """

    :param text: text for google text to speech
    :param language: language shortcut
    :return:
    """
    tts = gTTS(text, lang=language)
    mp3_fp = BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)  # !!!

    return mp3_fp

def gtts_save_as_mp3(text: str, language: str = "et"):
    """
    :param text: text for google text to speech
    :param language: language shortcut
    :return: None
    """
    tts = gTTS(text, lang=language)
    tts.save(text + ".mp3")


# simpleaudio needs to be installed for playback but not imported
# import simpleaudio.functionchecks as fc
# fc.LeftRightCheck.run()

# song = AudioSegment.from_mp3(word+".mp3")
# song.export("3.wav", format="wav")
# song = AudioSegment.from_file(word+".mp3")

# import simpleaudio as sa
# sa.PlayObject(mp3_fp)


if __name__ == '__main__':
    main()
