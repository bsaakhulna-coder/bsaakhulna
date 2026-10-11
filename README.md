# BSAA Khulna - Android APK - GitHub Actions Build (No Colab errors)

This builds APK automatically without sdkmanager 403 errors.

## How to get APK in 3 clicks:

1. Create new GitHub repository (https://github.com/new)
   - Name: bsaakhulna
   - Public

2. Upload these files to repo:
   - main.py
   - buildozer.spec
   - .github/workflows/build.yml

   You can drag-drop all files on GitHub website.

3. Go to Actions tab → Click "Build BSAA APK" → Click "Run workflow" (or it auto-runs on push)

4. Wait 15-20 minutes → Click on workflow run → Scroll down to Artifacts → Download "BSAA-Khulna-APK" → Inside is bsaakhulna-1.0-debug.apk

5. Install APK on phone

## Features:
- Logo left side top, Association name/address middle centered, vertical line
- Date left / Status right same line, To next line, Address next line - one line no wrap
- Bill PDF generation same as desktop
- Members list

No Colab, no sdkmanager error, no 403 error - GitHub handles SDK download.

## Copy existing database:
After install, copy your bsaa_outstanding.db to /storage/emulated/0/BSAA/ folder on phone using file manager.
