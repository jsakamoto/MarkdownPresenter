Markdown Presenter
==================

This is what I use for giving simple, quick-to-produce presentations. Rather than fighting with keynote or powerpoint for hours, I can whip up a presentation in minutes using markdown.

Demo and usage
--------------
Check out a demo
[here](http://jsakamoto.github.com/MarkdownPresenter/Presenter.html).

#### Supported devices and browsers
Markdown Presenter may work well on iPhone/iPad, Android, and PC Desktop browsers (Chrome, Firefox, IE - if you want touch support, you can chose IE10+ on Windows8+ -).  
![slide index at dropdown](http://jsakamoto.github.io/MarkdownPresenter/iphone.png)

#### Switching between slides
Use the **arrow keys** on your keyboard or **swipe horizontally** on touch screen to switch between slides.

#### Reloading
You can reload the presentation at any time - staying on the same
slide number - by pressing the spacebar.

The other way, you can enable **"Auto Reload"** mode by typing `A` key.  
In "Auto Reload" mode, Markdown Presenter is watching the change of `presentation.md` and reload it automatically.

#### Transition effect
If you whould like to get fade in/out effect on switching between slides, type 'e' then 'f' key on your keyboard.  
To reset this transition effect, type 'e' then 'n'.

#### Direct page jump
You can jump to the any slide which you want to show directly by 3 ways as follow:

1. by PowerPoint compatibe keyboard shortcut, such as '2','1','Enter' then jump to the slide at 21.
2. by chosing slide index from drop down list at bottom-right of the browser window.  
![slide index at dropdown](http://jsakamoto.github.io/MarkdownPresenter/slide-index-at-dropdown.png)
3. by specification hash tag of URL.  
![slide index at hashtag](http://jsakamoto.github.io/MarkdownPresenter/slide-index-at-hashtag.png)

Quick start for Windows OS users
----------
Open a command prompt and paste the text from below and press enter.

    @powershell -nop -ex unrestricted -c "iex ((new-object net.webclient).DownloadString('http://goo.gl/2JUSZU'))"

Then begin the download all files to needed into current directory.  
And after complete all downloads, mini http server is start automatically and open "Markdown Presenter" view by default browser.

You can edit and save ```presentation.md``` by any text editor, and reloead presentation by hit space key.

Look YouTube video:
[http://youtu.be/XxVSwx4ZhOk](http://youtu.be/XxVSwx4ZhOk)

Quick start for MacOS or Linux OS users
----------
Open a terminal and paste the text from below and press enter.

    python -c "exec('try:import urllib2 as m\nexcept:import urllib.request as m');exec(m.urlopen('http://goo.gl/ncwVU2').read())"

Then begin the download all files to needed into current directory.  
And after complete all downloads, mini http server is start automatically and open "Markdown Presenter" view by default browser.

You can edit and save ```presentation.md``` by any text editor, and reloead presentation by hit space key.

Manual Installing
----------

At first, download zip ball from [here](https://github.com/jsakamoto/MarkdownPresenter/archive/master.zip), and extract the zip file.

> **Notice** If you use Windows OS, then unblock download flag of the zip file before extract it from the property window in Windows Explorer.

You need to install this on a web server, otherwise it won't be able
to open the presentation.md file via AJAX.

###MacOS or Linux OS
So, if you're on a Mac,
copy it to your `~/Sites/MyPresentation` folder. Then open your web
browser to http://localhost/~myusername/MyPresentation/Presenter.html.

On Linux or Mac you have also likely Python installed and can start
its built-in web server in this directory by running bellow:

    python -c "exec('try:import SimpleHTTPServer as m\nexcept:import http.server as m');m.test(HandlerClass=m.SimpleHTTPRequestHandler)"

###Windows OS

####Tiny web server which is bundled with Markdown Presenter
You can use tiny web server 'httpd.ps1' writen by Windows PowerShell script which is bundled with Markdown Presenter source code.

After extract zip ball, there is a ```start-presenter-for-windows.bat```.  
Double click it, then mini http server 'httpd.ps1' is start and open the presentation by default web browser automatically.

####IIS or IIS express
If you use [IIS](http://www.iis.net/) or [IIS express](http://www.iis.net/learn/extensions/introduction-to-iis-express/iis-express-overview) copy all the MarkdownPresenter files to the webfolder (normally `C:\Inetpub\wwwroot\<SiteFolder>` on IIS and `C:\Users\<User>\Documents\My Web Sites\<WebSite>` on IIS express). 

Also make sure that a MIME mapping for the .md extension is added. Either add the following mimeMap element to the `applicationhost.config` or the `web.config` file:

    <system.webServer>
      <!-- there might be other configuration here. -->
      <staticContent>
        <!-- there might be other configuration here. -->
        <mimeMap fileExtension=".md" mimeType="text/plain" />
      </staticContent>
    </system.webServer>

Markdown file
-------------
The presentation.md file is where you put your presentation. All you need to do to separate slides is a paragraph with an exclamation mark, eg:

    This is a slide
    Blah blah blah

    !

    This is another slide
    Yada yada yada

Printing Support
-----

Markdown Presenter can print out the all slides to any printer from browser printing feature. 

![printing](http://jsakamoto.github.io/MarkdownPresenter/printing.png)

The keys to get fine result is follow:

- Layout - Landscape
- Margins - No margin
- Options - Enable to printing background colors

And you can print out as a PDF file, so you can also upload and publish your slides to "slideshare.com".

How it works
------------
The `Presenter.html` fetches the `presentation.md` from the server via
Ajax, uses [Showdown.js](https://github.com/coreyti/showdown) to
transform it into HTML, splits it on `<p>!</p>` into individual
slides, and displays the current slide.

Note: Showdown
[supports custom extensions](https://github.com/coreyti/showdown#creating-markdown-extensions)
that can either
[replace](https://github.com/coreyti/showdown#regexreplace) parts of
the content based on a regular expression or
[transform the whole text](https://github.com/coreyti/showdown#filter).
There are some
[extensions already available](https://github.com/coreyti/showdown/tree/master/src/extensions),
for example
[prettify](https://github.com/coreyti/showdown/blob/master/src/extensions/prettify.js)
that adds support for syntax highlighting or
[support for tables](https://github.com/coreyti/showdown/blob/master/src/extensions/table.js).

The current version of the bundled Showdown.js is 0.3.1 from Nov 2012.

Related
-------
- [Reveal.js](https://github.com/hakimel/reveal.js/): full-featured
  HTML+JS presentation framework with support for Markdown in
  individual slides
- [PageDown](http://code.google.com/p/pagedown/wiki/PageDown) - Stack
  Overflow's clone of Showdown
- [gitpitch](https://github.com/gitpitch/gitpitch) - turns PITCHME.md in the root of a git repository into an online presentation at https://gitpitch.com/ or a local offline presentation
