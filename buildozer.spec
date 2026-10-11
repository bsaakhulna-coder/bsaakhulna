[app]
title = BSAA Khulna
package.name = bsaakhulna
package.domain = org.bsaa.khulna
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.3.0,reportlab,androidstorage4kivy
orientation = portrait
fullscreen = 0
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.accept_sdk_license_agreement = True
p4a.branch = develop
p4a.fork = kivy

[buildozer]
log_level = 2
warn_on_root = 1
