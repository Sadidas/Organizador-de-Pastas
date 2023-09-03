import os
from pathlib import Path

listadepastas = {
    "Imagens": [".jpg", ".jpeg", ".png", ".ico"],
    "Vídeos": [".wmv", ".mp4", ".mp3", ".mkv", ".mov", ".wav", ".wpeg"],
    "ZIPS": [".zip", ".iso", ".rar", ".7z"],
    "Documentos": [".docx", ".txt", ".pdf", ".pptx", ".xlsx", ".doc", ".webp", ".ttf"],
    "Aplicativos": [".exe", ".apk", ".pk3"],
    "Gifs": [".gif"],
    "Arduino": [".ino"],
}

File_Format_Dictionary = {
    final_file_format: directory
    for directory, file_format_stored in listadepastas.items()
    for final_file_format in file_format_stored
}
for entry in os.scandir():
    if entry.is_dir():
        continue
    file_path = Path(entry)
    final_file_format = file_path.suffix.lower()
    if final_file_format in File_Format_Dictionary:
        directory_path = Path(File_Format_Dictionary[final_file_format])
        os.makedirs(directory_path, exist_ok=True)
        os.rename(file_path, directory_path.joinpath(file_path))

try:
    os.makedirs("Pasta lixo! (Apagar depois)")
except ValueError:
    print("Erro em criar um nova pasta!")

for dir in os.scandir():
    try:
        if dir.is_dir():
           os.rmdir(dir)
        else:
            os.rename(os.getcwd() + '/' + str(Path(dir)), os.getcwd() + '/Pasta lixo! (Apagar depois)/' + str(Path(dir)))
    except ValueError:
        print("Erro ao criar uma nova pasta chamada Pasta lixo! (Apagar depois). Já deve existir!")