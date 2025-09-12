import zipfile
import os

def read_zip_file(zip_path, filename_inside_zip):
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            if filename_inside_zip in zip_ref.namelist():
                with zip_ref.open(filename_inside_zip) as f:
                    content = f.read().decode('utf-8')
                    print(" Файлын агуулга (zip дотор):")
                    print(content)
                    return content
            else:
                print(f" {filename_inside_zip} файл zip дотор олдсонгүй.")
    except FileNotFoundError:
        print(f" {zip_path} файл олдсонгүй.")
    except zipfile.BadZipFile:
        print(f" {zip_path}  zip файл биш байна.")
    except IOError as e:
        print(f" I/O алдаа: {e}")


def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            print("Файлын агуулга:")
            print(content)
            return content
    except FileNotFoundError:
        print(f" '{filename}' файл олдсонгүй.")
    except IOError as e:
        print(f" IO алдаа: {e}")

def main():
    file_path = input("Файлын замыг оруулна уу (txt эсвэл zip): ").strip()

    if not os.path.exists(file_path):
        print(" Файл олдсонгүй.")
        return

    if file_path.endswith(".zip"):
        filename_inside_zip = input(" Zip доторх унших файлын нэрийг оруулна уу (жишээ нь: shuleg.txt): ").strip()
        read_zip_file(file_path, filename_inside_zip)
    else:
        read_file(file_path)

if __name__ == "__main__":
    main()
