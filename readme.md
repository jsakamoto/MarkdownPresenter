Markdown Presenter
==================

This is what I use for giving simple, quick-to-produce presentations. Rather than fighting with keynote or powerpoint for hours, I can whip up a presentation in minutes using markdown.

Demo and usage
--------------
Check out a demo
[here](http://jsakamoto.github.com/MarkdownPresenter/Presenter.html).

Markdown Presenter may work well on iPhone/iPad, Android, and PC Desktop browsers (Chrome, Firefox, IE - if you want touch support, you can chose IE10 on Windows8 -).

Use the arrow keys on your keyboard or swipe horizontally on touch screen to switch between slides.

You can reload the presentation at any time - staying on the same
slide number - by pressing the spacebar.

If you whould like to get fade in/out effect on switching between slides, type 'e' then 'f' key on your keyboard.  
To reset this transition effect, type 'e' then 'n'.


Installing
----------
You need to install this on a web server, otherwise it won't be able
to open the presentation.md file via AJAX. So, if you're on a Mac,
copy it to your `~/Sites/MyPresentation` folder. Then open your web
browser to http://localhost/~myusername/MyPresentation/Presenter.html.

On Linux or Mac you have also likely Python installed and can start
its built-in web server in this directory by running `python -m SimpleHTTPServer`.

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
