# Slender: Average Death — Android project

This project packages the supplied Python/Pygame game as an Android application.
The gameplay source in `main.py` is preserved; the Android packaging files are
provided alongside it.

## Project contents

- `main.py` — game source (Pygame + NumPy)
- `buildozer.spec` — Android package/build configuration (target API 36)
- `.github/workflows/build-android.yml` — cloud APK build workflow
- `requirements-desktop.txt` — dependencies for running the game on a computer

## Build an APK using GitHub (recommended if you only have a phone)

1. Create an empty GitHub repository.
2. Upload the **contents** of this project folder to the repository root.
3. Open **Actions** → **Build Android APK** → **Run workflow**.
   A push to `main` or `master` also starts the workflow automatically.
4. Wait for the workflow to finish successfully.
5. Open the completed run and download the `slender-android-apk` artifact.
   Extract the downloaded artifact ZIP to get the APK.
6. Transfer the APK to your Android phone and install it. Android may ask you
   to allow app installation from the file manager or browser you used.

## Build locally on Linux / WSL Ubuntu

Install Java 17, Git, Python 3.12, and the system packages required by
Buildozer/python-for-android. Then run:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
python -m pip install buildozer cython==0.29.34
buildozer -v android debug
```

The APK should be placed in `bin/` after a successful build.

## Run on a desktop for testing

```bash
python -m pip install -r requirements-desktop.txt
python main.py
```

## Important notes

- The app is configured for landscape orientation and Android API 36, with
  Android 6.0 (API 23) as the minimum version.
- The build targets ARM64 and ARMv7 devices.
- The game has touch controls: the left side is the movement joystick and the
  right side is for looking around. Object inspection supports touch gestures.
- `soundtrack.ogg` is optional. Put it beside `main.py` before building if you
  have a soundtrack; the game is designed to continue without it.
- This source package is **not an APK**. The APK must be produced by a successful
  Buildozer / GitHub Actions build. The current build environment does not have
  Buildozer or the Android SDK/NDK installed, so an APK has not been compiled
  or device-tested here.
