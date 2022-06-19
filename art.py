import pywhatkit

def image():
    image_path = input('Введи путь к изображению ') #file path
    image_path = image_path.replace('"', '')
    file_name = input('Введи имя будущего для файла ') #future file's name
    pywhatkit.image_to_ascii_art(img_path=image_path, output_file=file_name )

def main():
    image()

if __name__ == '__main__':
    main()
