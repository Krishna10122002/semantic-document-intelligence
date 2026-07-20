import os

def save_file(upload_file, folder):
    os.makedirs(folder, exist_ok=True)

    filepath = os.path.join(folder, upload_file.filename)

    with open(filepath, "wb") as f:
        f.write(upload_file.file.read())

    return filepath
