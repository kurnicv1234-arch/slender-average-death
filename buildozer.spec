[app]
# Slender: Average Death — Android package
title = Slender: Average Death
package.name = slenderaveragedeath
package.domain = org.slenderaveragedeath
source.dir = .
source.include_exts = py,ogg,png,jpg,jpeg,wav,ttf,txt
version = 1.0.0

# Python + Pygame + NumPy; SDL2 bootstrap is used by python-for-android.
requirements = python3,pygame,numpy

orientation = landscape
fullscreen = 1

# Android 16 target (API 36); Android 6.0+ minimum.
android.api = 36
android.minapi = 23
android.ndk = 28c
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True
android.allow_backup = False

# Current stable python-for-android line; Python 3.12 is selected by p4a.
p4a.bootstrap = sdl2
p4a.fork = kivy
p4a.branch = master

# Avoid unused permissions. No network permission is required by this game.

[buildozer]
log_level = 2
warn_on_root = 1
