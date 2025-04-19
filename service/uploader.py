import os
from dotenv import load_dotenv
import cloudinary
import cloudinary.uploader
import os
from tqdm import tqdm

load_dotenv()
cloudinary.config (
    cloud_name = os.getenv("cloud_name"), 
    api_key = os.getenv("api_key"),
    api_secret = os.getenv("api_secret"),
    secure = True
)

class uploader: 

    def __init__(self, path):
        self.path = path

    def load_list_image_from_path (self): 
        image_path = []

        for folder_name, subfolders ,filenames in os.walk(self.path): 
            for filename in filenames: 
                if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
                    full_path = os.path.join(folder_name, filename)
                    image_path.append(full_path)
        return image_path
    
    def upload_file(self, image_list):
        for i in tqdm(image_list, desc="Uploading image"):
            public_id = os.path.splitext(os.path.basename(i))[0] 
            try:
                upload_result = cloudinary.uploader.upload(i, 
                                                        public_id=public_id,
                                                        resource_type="image", 
                                                        transformation={
                                                            "fetch_format": "auto", 
                                                            "quality": "auto"
                                                            }
                                                        )
                print(f"✅  Uploaded: {public_id}")
                os.remove(i)
            except Exception as e: 
                print(f"\n ❌ Failed to upload {i}: {e}")