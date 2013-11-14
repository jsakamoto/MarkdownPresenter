import webbrowser
import SimpleHTTPServer
import threading
import urllib
from zipfile import ZipFile
import os

tagname = "1.0"
zipname = "markdown-presenter-" + tagname + ".zip"
url = "https://github.com/jsakamoto/MarkdownPresenter/releases/download/v." + tagname + "/" + zipname

# download zip archive of Markdown Presenter.
zippath = urllib.urlretrieve(url)[0] # download a zip file as a randomly named tempfile

# extract the zip.
ZipFile(zippath).extractall()

# clean up zip.
os.remove(zippath)

# launch default web browser to open Markdown Presenter
# after one shot timer to wait for warming up HTTP daemon.
threading.Timer(1.0, webbrowser.open, ["http://localhost:8000/Presenter.html"]).start()

# start mini HTTP daemon.
SimpleHTTPServer.test()
