import os 
import service.uploader as upload_file

def list_task(): 
    while(1):
        print("1. Upload image")
        print("2. Exit")
        choice = str(input("Choose your task to do: "))
        match choice: 
            case "1": 
                path = str(input("Input your path to upload to cloud: ")).replace('\\', '/').strip()
                if not os.path.exists(path): 
                    print("Path not exist !")
                    continue
                upload = upload_file.uploader(path)

                images_list = upload.load_list_image_from_path()
                if len(images_list) == 0: 
                    print("⚠️  Folder not have file to upload !")
                    continue
                for image in images_list: 
                    image = image.replace('\\', '/')
                    print(f"\r {image}")
                print("✅  Get list success")
                upload.upload_file(images_list)
                print("✅  Done work to upload images")
            case "2": 
                return
        
def main(): 
    print("Start tools")
    list_task()

if __name__ == "__main__": 
    main()