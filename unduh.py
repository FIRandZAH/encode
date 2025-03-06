import requests

url = "https://raw.githubusercontent.com/FIRandZAH/FIRZAH/refs/heads/main/encode"
filename = "encode"

response = requests.get(url, stream=True)
total_size = int(response.headers.get('content-length', 0))
chunk_size = 1024  

downloaded_size = 0
with open(filename, "wb") as file:
    for chunk in response.iter_content(chunk_size):
        if chunk:  
            file.write(chunk)
            downloaded_size += len(chunk)
            percent = (downloaded_size / total_size) * 100
            print(f"\rDownload progress: {percent:.2f}%", end="")

print("\nDownload selesai!")
