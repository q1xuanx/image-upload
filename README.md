# 🖼️ Cloudinary Image Uploader Tool

With a passion for collecting dog images but limited disk space, I built a lightweight Python tool that automatically uploads images from folders to Cloudinary and deletes them locally after upload. It features progress display, .env support, and easy customization.

---

## 🚀 Features

- ✅ Automatically detects and uploads `.png`, `.jpg`, `.jpeg`, `.webp` images from nested folders
- ☁️ Uploads to [Cloudinary](https://cloudinary.com/)
- 🔒 Reads credentials from `.env` file
- 🧼 Automatically deletes images after upload
- 📊 Real-time progress bar using `tqdm`
- 🧠 Simple CLI input — no UI required

---

## 🧱 Project Structure

```
upload_tool/
├── main.py                 # Entry point
├── service
├───── uploader.py             # Image uploader class
├── .env                    # Your secret Cloudinary config (not committed)
├── .gitignore              # Excludes /build, /dist, .env, etc.
```

---

## ⚙️ Requirements

- Python 3.8+
- Cloudinary account
- Packages:
  - `cloudinary`
  - `python-dotenv`
  - `tqdm`
  - `pyinstaller` (for build application)

---

## 📦 Installation

```bash
git clone https://github.com/q1xuanx/image-upload.git
cd image-upload
```

Create a `.env` file in the root folder:

```env
cloud_name=your_cloud_name
api_key=your_api_key
api_secret=your_api_secret
```

---

## 🛠️ How to Use

```bash
python main.py
```

You'll be prompted:

```text
📁 Input your folder path to upload to Cloudinary:
> C:/Users/ADMIN/Desktop/dogs
```

Then the tool will:
1. Find all images inside that folder (and subfolders)
2. Upload them to Cloudinary
3. Delete each image after a successful upload

---

## 🧪 Example Output

```
🚀 Start upload tool
📁 Input your folder path to upload to Cloudinary:
> ./uploads

✅ Get list success

Uploading images: 100%|████████████████████████| 15/15 [00:05<00:00, 2.85it/s]
✅ All done!
```

---

## 🧊 Build to .exe (Optional)

If you want to share the tool as a standalone Windows `.exe`:

```bash
pip install pyinstaller
pyinstaller --onefile --icon=cloud-upload-alt.ico main.py
```

> Output will be in `/dist/main.exe`

---

## 🙈 .gitignore Sample

```gitignore
.env
__pycache__/
*.pyc
build/
dist/
*.spec
.venv/
.vscode/
```

---

## 📄 License

MIT License. Free to use and modify.
