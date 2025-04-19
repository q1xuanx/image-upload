import os 
import service.uploader as upload_file

def main(): 
    print("Start tools")
    path = str(input("Input your path to upload to cloud: ")).replace('\\', '/').strip()
    
    if not os.path.exists(path): 
        print("Path not exist !")
        return

    upload = upload_file.uploader(path)

    images_list = upload.load_list_image_from_path()
    if len(images_list) == 0: 
        print("Folder not have file to upload !")
        return
    
    for image in images_list: 
        image = image.replace('\\', '/')
        print(f"\r {image}")
    print("Get list success")
    upload.upload_file(images_list)
    print("Done work to upload images")

if __name__ == "__main__": 
    main()