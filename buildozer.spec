[app]
title = ChiruVoiceAssistant
package.name = chiru
package.domain = org.chiru
source.include_exts = py
version = 1.0
requirements = python3,kivy,pyttsx3,speechrecognition
orientation = portrait
fullscreen = 1
android.permissions = RECORD_AUDIO,INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
