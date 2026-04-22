import os
import zipfile
import requests
import threading
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from android.permissions import request_permissions, Permission

RESOURCES_URL = "https://dl.dropboxusercontent.com/scl/fi/5tusptt3gnxduba54vbny/resources.zip?rlkey=uajfwbhcy9yoox12tmnoo5lh8"
RESOURCES_DIR = "/sdcard/zain_resources"
ZIP_PATH = "/sdcard/resources.zip"

class MainApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.label = Label(text="Initializing...", size_hint_y=0.6)
        self.btn = Button(text="Retry", size_hint_y=0.2, on_press=self.start_download)
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.btn)
        self.btn.opacity = 0
        self.btn.disabled = True
        request_permissions([Permission.WRITE_EXTERNAL_STORAGE], self.on_permissions)
        return self.layout

    def on_permissions(self, permissions, grants):
        if all(grants):
            self.label.text = "Checking resources..."
            if os.path.exists(RESOURCES_DIR):
                self.run_core()
            else:
                self.start_download(None)
        else:
            self.label.text = "Storage permission denied. App cannot continue."
            self.btn.opacity = 1
            self.btn.disabled = False

    def start_download(self, instance):
        self.label.text = "Downloading resources..."
        self.btn.opacity = 0
        self.btn.disabled = True
        threading.Thread(target=self.download_file).start()

    def download_file(self):
        try:
            response = requests.get(RESOURCES_URL, stream=True)
            total_size = int(response.headers.get('content-length', 0))
            downloaded = 0
            with open(ZIP_PATH, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
                    downloaded += len(chunk)
                    progress = (downloaded / total_size) * 100 if total_size else 0
                    Clock.schedule_once(lambda dt, p=progress: self.update_progress(p))
            Clock.schedule_once(lambda dt: self.extract_zip())
        except Exception as e:
            Clock.schedule_once(lambda dt: self.download_failed(str(e)))

    def update_progress(self, progress):
        self.label.text = f"Downloading... {progress:.1f}%"

    def download_failed(self, error):
        self.label.text = f"Download failed: {error[:50]}"
        self.btn.opacity = 1
        self.btn.disabled = False

    def extract_zip(self):
        self.label.text = "Extracting resources..."
        try:
            with zipfile.ZipFile(ZIP_PATH, 'r') as zip_ref:
                zip_ref.extractall(RESOURCES_DIR)
            os.remove(ZIP_PATH)
            self.label.text = "Resources ready."
            Clock.schedule_once(lambda dt: self.run_core())
        except Exception as e:
            self.label.text = f"Extraction failed: {str(e)[:50]}"
            self.btn.opacity = 1
            self.btn.disabled = False

    def run_core(self):
        self.label.text = "Starting core service..."
        core_path = os.path.join(RESOURCES_DIR, "main_core.py")
        if os.path.exists(core_path):
            import subprocess
            try:
                subprocess.Popen(["python", core_path])
                self.label.text = "Core service running."
            except Exception as e:
                self.label.text = f"Failed to start core: {str(e)[:50]}"
                self.btn.opacity = 1
                self.btn.disabled = False
        else:
            self.label.text = "Core script not found."
            self.btn.opacity = 1
            self.btn.disabled = False

if __name__ == "__main__":
    MainApp().run()
