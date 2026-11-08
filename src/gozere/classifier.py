from pathlib import Path

FILE_TYPES = {
    ".md": "Markdown",
    ".txt": "Text",
    ".pdf": "Document",
    ".docx": "Document",
    ".png": "Image",
    ".jpg": "Image",
    ".webp": "Image",
    ".gif": "Image",
    ".svg": "Vector", # Vector image, mathematical, numeric, coded ?
    ".ico": "Image", # Is image type?
    ".mp4": "Video",
    ".mkv": "Video",
    ".mp3": "Audio",
    ".wav": "Audio",
    ".zip": "Archive",
    ".7z": "Archive",
    ".py": "Code",
    ".ps1": "Code",
    ".css": "Code", # is this code? generally used for style.css which does follow a form of code?
    ".js": "", # can leave empty?
    ".ts": "", # can leave empty?
    ".dll": "", # was this binary?, windows file?
    ".exe": "Executable", # Executable?
    ".bat": "Code", # or executable?
    ".json": "Data",
    ".csv": "Data",
    ".xml": "Workbook", # is this not data? or is specifying the data like the diff of .md vs .txt
}

def classify(file: Path) -> str:
    extension = file.suffix.lower()
    return FILE_TYPES.get(extension, "Unkown")
