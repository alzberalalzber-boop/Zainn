[app]
# (1) Version Fix
title = Ghost C2
package.name = ghostc2
package.domain = org.ghostc2
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 0.1

# (2) Dependencies Fix - Using pycryptodomex for stability
requirements = python3,kivy==2.3.0,requests,pycryptodomex,android,certifi

orientation = portrait
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# (3) Android SDK/NDK Fix for 2026 standards
android.api = 33
android.minapi = 21
android.sdk_api = 33
android.ndk = 25b
android.ndk_api = 21

# (4) Build Architecture
android.archs = arm64-v8a
android.private_storage = True
android.accept_sdk_license = True
android.skip_update = False

[buildozer]
log_level = 2
warn_on_root = 1
