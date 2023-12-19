import tkinter as tk
from PIL import Image,ImageTk
import requests
from io import BytesIO
import random
import imghdr
import threading
import queue

MIN_AWW = 2
MAX_AWW = 116
AWW_URL_BASE = "https://www.twolittlefleas.co.uk/happiness-generator/img/cute/image{}.jpg"


def get_new_image():
    nb = str(random.randint(MIN_AWW, MAX_AWW)).zfill(3)
    aww_url = AWW_URL_BASE.format(nb)
    print(aww_url)

    # twolitllefleas utilise des techniques pour eviter les botss
    # (et renvoyer un HTTP 302 si on a pas les bons headers)
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "fr,en-US;q=0.7,en;q=0.3",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
    }

    try:
        # on doit faire un truc compliqué et télécharger l'image petit à petit
        # je pense que c'est parce qu'elle est trop grosse et que ça tient pas
        # dans une requette HTTP classique
        response = requests.get(aww_url, stream=True, headers=headers)
        if response.status_code == 200:
            response.raw.decode_content = True

            # Grab first 100 bytes as potential image header
            header = response.raw.read(100)
            ext = imghdr.what(None, h=header)
            print("Found: " + ext)
            if ext != None:     # Proceed to other tests if we received an image at all
                data = header + response.raw.read()  # GET THE REST OF THE FILE
                data = BytesIO(data)
                im = Image.open(data)
                photo = ImageTk.PhotoImage(im)
                return photo
        else:
            print("Received error " + str(response.status_code))
    except requests.ConnectionError as e:
        print(e)


def update_image():
    image = None
    while not image:
        image=get_new_image()

    label.configure(image=image)
    label.image = image


#### comment empecher le freezing de l'appli

def download_to_queue():
    image = None
    while not image:
        image=get_new_image()
    exchange_queue.put(image)

def download_async():
    thread = threading.Thread(target=download_to_queue)
    thread.start()

def update_image_async():
    # cette fonction devrait être dans une classe...
    # comme je ne veux pas utiliser de variables globales, je
    # met l'état dans du téléchargement comme attribut de la fonction (...)
    # j'utilise settatr et gettatr pour pouvoiir y acceder alors que je ne sais
    # pas s'ils existent déjà...
    downloading = getattr(update_image_async, "downloading", False)
    if not downloading:
        setattr(update_image_async, "downloading", True)
        # on ne veut pas lancer pleins de téléchargement en parallèles,
        # surtout si c'est pour les perdre... d'où la variable downloading
        # pour faire du rate limiting
        download_async()
    try:
        image = exchange_queue.get(block=False)
    except queue.Empty:
        # let's try again later
        root.after(100, update_image_async)
        return

    setattr(update_image_async, "downloading", False)
    label.configure(image=image)
    label.image = image


#### fin freezing

exchange_queue = queue.Queue()

root = tk.Tk()
root.title("display image")
label = tk.Label(root)

image = None
while not image:
    image = get_new_image()
label.configure(image=image)
label.image = image

label.grid(column=0, row=0, sticky=tk.N+tk.S+tk.E+tk.W)

button = tk.Button(root, text="Update image", command=update_image)
button_async = tk.Button(root, text="Update image Async", command=update_image_async)
button.grid()
button_async.grid()

slider = tk.Scale(root, orient="horizontal")
slider.grid()

root.mainloop()