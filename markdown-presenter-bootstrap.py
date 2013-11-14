import webbrowser
import SimpleHTTPServer
import threading
import time
import urllib
from zipfile import ZipFile
import os
import tempfile
import shutil
import atexit

tagname = "1.0"
zipname = "markdown-presenter-" + tagname + ".zip"
url = "https://github.com/jsakamoto/MarkdownPresenter/releases/download/v." + tagname + "/" + zipname

# create a tempdir to retrieve materials
tempdir = tempfile.mkdtemp()
# by the way, tempdirs should be taken care by yourself
atexit.register(lambda:shutil.rmtree(tempdir))

# download zip archive of Markdown Presenter and extract it into tempdir.
zippath = os.path.join(tempdir, zipname)
urllib.urlretrieve(url, zippath)
ZipFile(zippath).extractall(tempdir) # expect that zipfile is GC'ed(and eventually relevant system resources are closed as well) immediately

# launch default web browser to open Markdown Presenter
# after one shot timer to wait for warming up HTTP daemon.
threading.Timer(1.0, lambda:webbrowser.open("http://localhost:8000/Presenter.html")).start()

# Move to the tempdir
os.chdir(tempdir)

# start mini HTTP daemon.
SimpleHTTPServer.test()
