# Ability to download a specific versionCode of apk

## Using Google Play Unofficial Python API

[Forked Google Play Unofficial Python API](https://github.com/egirault/googleplay-api)

An unofficial Python API that let you search, browse and download Android apps from Google Play (formerly Android Market).

This library is inspired by those projects, working with the old version of the API:

* [Android Market Python API](https://github.com/liato/android-market-api-py)
* [Android Market Java API](http://code.google.com/p/android-market-api/)

### Disclaimer
**This is not an official API. I am not afiliated with Google in any way, and am not responsible of any damage that could be done with it. Use it at your own risk.**

### Dependencies
* [Python 2.5+](http://www.python.org)
* [Protocol Buffers](http://code.google.com/p/protobuf/)

### Requirements
You must edit `config.py` before using the provided scripts (`search.py`, `download.py`, `apishell.py`, etc.). First, you need to provide your phone's `androidID`:

    ANDROID_ID      = None # "xxxxxxxxxxxxxxxx"

To get your `androidID`, use `*#*#8255#*#*` on your phone to start *Gtalk Monitor*. The hex string listed after `aid` is your `androidID`.

In order to authenticate to Google Play, you also need to provide either your Google login and password, or a valid subAuthToken.

## Usage

### Downloading apps

Downloading an app is really easy, just provide its package name. I only tested with free apps, but I guess it should work as well with non-free as soon as you have enough money on your Google account.

    $ python download.py com.google.android.gm
    Downloading 2.7MB... Done

    $ file com.google.android.gm.apk
    com.google.android.gm.apk: Zip archive data, at least v2.0 to extract

#### Downloading specific versionCode of apps

    $ python download.py com.facebook.katana 288859

    $ aapt d badging com.facebook.katana.vc288859.apk |grep pack
    package: name='com.facebook.katana' versionCode='288859' versionName='3.5' platformBuildVersionName=''

## License

This project is released under the BSD license.

