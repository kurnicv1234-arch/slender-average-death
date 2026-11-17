SLENDER: AVERAGE DEATH — сборка Android APK (Android 16 / API 36)
=================================================================

В проект включён исходный игровой файл без изменения игровой логики:
  main.py                 — игра Pygame + NumPy
  buildozer.spec          — настройки Android-сборки (target API 36)
  .github/workflows/...   — автоматическая сборка APK через GitHub Actions

ВАЖНО
-----
В этой среде удалось проверить синтаксис Python, но Android SDK/NDK и Buildozer
не установлены, поэтому готовый APK здесь не собран. ZIP — это готовый проект
для сборки; APK появится после успешного запуска сборки ниже.

СПОСОБ 1. Сборка в облаке через GitHub (подходит, если у тебя только телефон)
-----------------------------------------------------------------------------
1. Создай новый пустой репозиторий на https://github.com/.
2. Распакуй содержимое ZIP и загрузи ВСЕ файлы и папки проекта в репозиторий.
3. Открой вкладку Actions и запусти workflow "Build Android APK" через
   Run workflow (или сделай push — workflow запускается автоматически).
4. Дождись зелёного статуса. Открой завершённый запуск → Artifacts →
   slender-android-apk. Скачай ZIP-артефакт и распакуй его.
5. Установи APK на телефон. При первой установке Android может попросить
   разрешить установку приложений из используемого браузера/файлового менеджера.

СПОСОБ 2. Сборка на Linux / WSL Ubuntu
--------------------------------------
Нужны Java 17, Git, Python 3.12, Android SDK/NDK (Buildozer скачает их сам).

  sudo apt update
  sudo apt install -y git zip unzip openjdk-17-jdk python3-pip \
      python3-venv autoconf libtool pkg-config zlib1g-dev \
      libncurses5-dev libncursesw5-dev libtinfo6 cmake libffi-dev \
      libssl-dev automake autopoint gettext
  python3 -m venv .venv
  source .venv/bin/activate
  pip install --upgrade pip setuptools
  pip install buildozer cython==0.29.34
  buildozer android debug

APK после успешной сборки:
  bin/*.apk

ЗАМЕТКИ
-------
* Сборка Pygame/NumPy для Android компилирует нативные библиотеки и может
  занять много времени при первом запуске.
* Конфигурация рассчитана на ARM64 и ARMv7 телефоны и экран в альбомной
  ориентации. В игре сохранён внутренний кадр 16:9.
* В исходнике предусмотрена необязательная музыка soundtrack.ogg. Если хочешь
  включить саундтрек, положи soundtrack.ogg рядом с main.py до сборки.
  Без этого файла игра должна запускаться без фоновой музыки.
* Реальную производительность, звук и сенсорное управление нужно проверить
  на устройстве. Успешная компиляция сама по себе не гарантирует корректную
  работу конкретной версии Pygame на каждом телефоне.
