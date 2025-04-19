import os 
import service.uploader as upload_file
import pyfiglet as pyf
from rich import print
from rich.console import Console
from rich.table import Table


def create_table(): 
    console = Console()
    tab = Table(title="Menu")
    tab.add_column("Key", style="cyan", no_wrap=False)
    tab.add_column("Description", justify="right" ,style="green", no_wrap=False)
        
    tab.add_row("1", "Upload Image")
    tab.add_row("2", "Exit")
        
    console.print(tab)

def list_task(): 
    while(1):
        create_table()
        choice = str(input("Choose your task to do: "))
        match choice: 
            case "1": 
                path = str(input("Input your path to upload to cloud: ")).replace('\\', '/').strip()
                if not os.path.exists(path): 
                    print("⚠️  Path not exist !")
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
    welcome_text = pyf.figlet_format("Upload Image", font="starwars")
    print(welcome_text)
    list_task()

if __name__ == "__main__": 
    main()