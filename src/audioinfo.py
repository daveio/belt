import os
import click
from mutagen.flac import FLAC
from mutagen.mp3 import MP3
from mutagen.mp4 import MP4
from pathlib import Path

decoders = {".flac": FLAC, ".mp3": MP3, ".m4a": MP4}


def get_audioinfo(path: click.Path) -> str:
    for dirpath, _, filenames in os.walk(path):
        for filename in filenames:
            file_path = Path(os.path.join(dirpath, filename))
            ext = file_path.suffix
            if ext not in decoders:
                pass
            else:
                size = file_path.stat().st_size
                decoder = decoders.get(ext.lower())
                audio = decoder(file_path)
                if ext.lower() == ".mp3":
                    print(f"{file_path}:{audio.info.sample_rate}:16:{size}")
                else:
                    print(
                        f"{file_path}:{audio.info.sample_rate}:{audio.info.bits_per_sample}:{size}"
                    )


def compose_audioinfo(path: click.Path) -> str:
    return get_audioinfo(path)
