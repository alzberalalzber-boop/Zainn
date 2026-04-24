[app]

# (str) Title of your application
title = Zain Tools

# (str) Package name
package.name = zaintools

# (str) Package domain (needed for android packaging)
package.domain = com.zain

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json

# (str) Application versioning (method 1)
version = 1.0.0

# (list) Application requirements
requirements = python3,kivy,requests

# (str) Supported orientation (portrait, landscape or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 30

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android architecture to build for
android.archs = arm64-v8a

# (bool) Automatically accept SDK license
android.accept_sdk_license = True

# (str) Path to custom icon (optional, remove if not used)
icon.filename = zain_logo.png

# (str) Path to custom splash screen image (optional)
presplash.filename = zain_logo.png

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = off, 1 = on)
warn_on_root = 1
