import sys
import subprocess
import os

def install_and_import():
    try:
        import rembg
        from PIL import Image
    except ImportError:
        print("Installing rembg and Pillow...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "rembg", "Pillow", "onnxruntime"])
        import rembg
        from PIL import Image
    return rembg, Image

rembg, Image = install_and_import()

input_path = r"C:\Users\eumar\.gemini\antigravity\brain\0ecd7452-f3f9-4b99-89eb-98fb9e7e0a92\media__1774465747481.png"
output_path = r"c:\Users\eumar\Downloads\unicoweb.com.br\assets\marcos_antonio.png"

os.makedirs(os.path.dirname(output_path), exist_ok=True)

print("Starting background removal...")
with open(input_path, 'rb') as i:
    input_data = i.read()
    output_data = rembg.remove(input_data)
    with open(output_path, 'wb') as o:
        o.write(output_data)

print(f"Image processed and saved to {output_path}")
