#!/usr/bin/env python

# Do not remove
GOOGLE_LOGIN = GOOGLE_PASSWORD = AUTH_TOKEN = None

import sys
from pprint import pprint

from config import *
from googleplay import GooglePlayAPI
from helpers import sizeof_fmt

if (len(sys.argv) < 2):
    print "Usage: %s packagename [filename] [versionCode]"
    print "Download an app."
    print "If filename is not present, will write to packagename.apk."
    sys.exit(0)

packagename = sys.argv[1]

if (len(sys.argv) == 3):
    filename = sys.argv[2]
else:
    filename = packagename + ".apk"

# Connect
api = GooglePlayAPI(ANDROID_ID)
api.login(GOOGLE_LOGIN, GOOGLE_PASSWORD, AUTH_TOKEN)

# Get the version code and the offer type from the app details
m = api.details(packagename)
if m == False:
    print 'error in api.details'
    exit(1)

doc = m.docV2
vc = doc.details.appDetails.versionCode

# Set the version code
if (len(sys.argv) == 3):
    vc = int(sys.argv[2])
else:
    vc = doc.details.appDetails.versionCode

# Genarate the filename with version code
if (len(sys.argv) == 4):
    filename = sys.argv[3] + ".vc" + str(vc) + ".apk"
else:
    filename = packagename + ".vc" + str(vc) + ".apk"

ot = doc.offer[0].offerType

# Download
print "versionCode:%d Downloading %s..." % (vc,
        sizeof_fmt(doc.details.appDetails.installationSize),)
data = api.download(packagename, vc, ot)
if data == False:
    print 'error in api.download'
    sys.exit(1)

open(filename, "wb").write(data)
print "Done"

