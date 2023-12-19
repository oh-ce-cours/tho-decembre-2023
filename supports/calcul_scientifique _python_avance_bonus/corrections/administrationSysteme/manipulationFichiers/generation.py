from pathlib import Path
import random
import hashlib
import shutil


def change_file_name(fname):
    """Returns a new filename with a random extension"""
    extension_list = [
        "dwg",
        "xcf",
        "jpg",
        "jpx",
        "png",
        "gif",
        "webp",
        "cr2",
        "tif",
        "bmp",
        "jxr",
        "psd",
        "ico",
        "heic",
        "3gp",
        "mp4",
        "m4v",
        "mkv",
        "webm",
        "mov",
        "avi",
        "wmv",
        "mpg",
        "flv",
        "aac",
        "mid",
        "mp3",
        "m4a",
        "ogg",
        "flac",
        "wav",
        "amr",
        "aiff",
        "br",
        "rpm",
        "dcm",
        "epub",
        "zip",
        "tar",
        "rar",
        "gz",
        "bz2",
        "7z",
        "xz",
        "pdf",
        "exe",
        "swf",
        "rtf",
        "eot",
        "ps",
        "sqlite",
        "nes",
        "crx",
        "cab",
        "deb",
        "ar",
        "Z",
        "lzo",
        "lz",
        "lz4",
        "woff",
        "woff2",
        "ttf",
        "otf",
        "wasm",
    ]
    new_name = hashlib.md5(open(fname, "rb").read()).hexdigest()[:8]
    new_extension = random.choice(extension_list)
    return f"{new_name}.{new_extension}"


files = list(Path("./originaux").glob("*"))
new_names = [change_file_name(f) for f in files]

new_folder = Path("./random_names")

for old_name, new_name in zip(files, new_names):
    old_path = old_name
    new_path = new_folder / new_name
    new_folder.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(old_path, new_path)

shutil.make_archive("fichiersVrac", format="gztar", root_dir=str(new_folder))
shutil.rmtree(str(new_folder))
