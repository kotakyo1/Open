import pywhatkit

def image():
    image_path = input('введи путь к изображению ')
    pywhatkit.image_to_ascii_art(img_path=image_path)

def main():
    image()

if __name__ == '__main__':
    main()