[app]
title = Zain Tools
package.name = zaintools
package.domain = com.zain
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 1.0.0
requirements = python3,kivy,requests
orientation = portrait
fullscreen = 0
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE
android.api = 30
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.copy_libs = 0
android.skip_update = True
android.add_aidl = False
icon.filename = zain_logo.png
presplash.filename = zain_logo.png
[buildozer]
log_level = 2
warn_on_root = 1
