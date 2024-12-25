import os
import click
from textwrap import dedent
from mutagen.flac import FLAC
from mutagen.mp3 import MP3
from mutagen.mp4 import MP4

decoders = {"flac": FLAC, "mp3": MP3, "m4a": MP4}


def get_audioinfo(path: click.Path) -> str:
    for dirpath, _, filenames in os.walk(path):
        for filename in filenames:
            ext = os.path.splitext(filename)[1][1:]
            file_path = os.path.join(dirpath, filename)
            if ext not in decoders:
                pass
            else:
                decoder = decoders.get(ext)
                audio = decoder(file_path)
                if ext == "mp3":
                    print(f"{file_path} : {audio.info.sample_rate}Hz")
                else:
                    print(
                        f"{file_path} : {audio.info.sample_rate}Hz : {audio.info.bits_per_sample}-bit"
                    )


def compose_audioinfo(path: click.Path) -> str:
    return get_audioinfo(path)
