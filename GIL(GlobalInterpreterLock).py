import threading
import requests

def download_url(url):
    response = requests.get(url)  # El GIL se libera durante la espera I/O
    return response.text

urls = ["https://developer.mozilla.org/es/docs/Web/JavaScript", "https://developer.mozilla.org/es/docs/conflicting/Web/JavaScript/JavaScript_technologies_overview"]
threads = [threading.Thread(target=download_url, args=(url,)) for url in urls]

print(threads)

print("Starting download")
for thread in threads:
    thread.start()
    
    
    print("Thread finished")


print("Download finished")