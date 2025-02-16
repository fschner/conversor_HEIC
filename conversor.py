import os
from PIL import Image
import pillow_heif

def convert_heic_to_png(directory='.'):  
    # Garante que o pillow-heif está registrado corretamente
    pillow_heif.register_heif_opener()

    # Percorre todos os arquivos no diretório atual
    for filename in os.listdir(directory):
        if filename.lower().endswith('.heic'):
            heic_path = os.path.join(directory, filename)
            png_path = os.path.join(directory, f"{os.path.splitext(filename)[0]}.png")

            try:
                # Abre a imagem HEIC e salva como PNG
                with Image.open(heic_path) as img:
                    img.save(png_path, 'PNG')
                print(f"[✔️] Convertido: {filename} -> {png_path}")
            except Exception as e:
                print(f"[❌] Erro ao converter {filename}: {e}")

if __name__ == '__main__':
    convert_heic_to_png()
