Dialogger: Dark Days Ahead
=========

This is a fork of [Dialogger](https://github.com/etodd/dialogger) to support dialog tree generation for [Cataclysm: Dark Days Ahead](https://github.com/CleverRaven/Cataclysm-DDA).

[![Dialogger](http://i.imgur.com/ojQbysnl.png)](http://i.imgur.com/ojQbysn.png)

Dialogger is a simple dialogue graph editor that saves your dialog graph as JSON.

It uses [JointJS](http://www.jointjs.com/).

Read more about the rationale
[here](http://etodd.io/2014/05/16/the-poor-mans-dialogue-tree/).

Dialogger: Dark Days Ahead departs from Dialogger development by eschewing [NW.js](http://nwjs.io/) in order to keep dependencies and execution model simple.
This can be revisited as needed, the current system doesn't even work.

Running
-------

Visit https://cleverraven.github.io/dialogger/ to edit Cataclysm: Dark Days Ahead dialog graphs.

To work on D:DDA, clone this repository and serve the pages with a minimal webserver such as a Python [SimpleHTTPServer](https://docs.python.org/2/library/simplehttpserver.html).

The MIT License
---------------

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
