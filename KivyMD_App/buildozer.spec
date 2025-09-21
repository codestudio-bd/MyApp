[app]
# (str) Title of your application
title = MyKivyMDApp

# (str) Package name
package.name = mykivymdapp

# (str) Package domain (reverse DNS style)
package.domain = org.example

# (str) Source code filename
source.include_exts = py,png,jpg,kv,atlas
source.dir = .

# (list) Application requirements
requirements = python3,kivy,kivymd

# (str) Supported orientation (portrait, landscape, all)
orientation = portrait

# (bool) Whether the application should be fullscreen or not
fullscreen = 0

# (str) Icon of the application
icon.filename = %(source.dir)s/icon.png

# (str) Version
version = 0.1

# (bool) Copy the .py files into the .apk instead of compiling
# (useful for debugging)
#android.copy_libs = 1

# (list) Permissions
android.permissions = INTERNET

# (bool) Presplash screen
presplash.filename = %(source.dir)s/presplash.png

# (str) Android API to use
android.api = 33
android.minapi = 21
android.ndk = 25b

# (str) Android architecture
android.arch = arm64-v8a

# (str) Python-for-Android bootstrap
# Use "sdl2" for most apps
android.bootstrap = sdl2

# (str) Application entry point
# By default it's main.py, but your file is kivymd.py
# So we need to tell Buildozer
# rename your file to main.py OR specify this:
# (you can keep kivymd.py and rename later)
# android.entrypoint = org.kivy.android.PythonActivity