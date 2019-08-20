# PortfolioSite_StarterCode
Source code for Build a Portfolio site Project.

The site display the portfolio main page which includes a `Logo`, `Title`, and highlighted the `Featured Work` with a respective box art imagery. it is a pure Html & CSS, the Page utilizes a grid-based layout with styles making use of the Flexbox Layout Shifter Pattern. Made with Python 2.7, Flask, Html, and CSS.

## Features

* Built in web server.
* All content is responsive and displays on all display sizes includes: Desktop, Mobile: Google Nexus 5, Tablet: Apple iPad.

## Examples

Check [My Portfolio Site](https://portfolio-wael.herokuapp.com/) for an example of Build a Portfolio Site.

## Installation

* [Python 2.7](https://www.python.org/downloads/release/python-2712/). *If you are on Windows, please refer to: [Install and configure python for Windows](http://rockos.co.jp:3009/runestone/static/pip2/Installation/pythonInstall.html#install-and-configure-python-for-windows)*
* [Flask](https://flask.palletsprojects.com/en/1.0.x/), can be installed from the shell like (`terminal` on Mac or Linux), from `git bash` on Windows , also you can check out the documentation for [Install Flask](https://flask.palletsprojects.com/en/1.0.x/installation/#install-flask) for another installation options.
  * If you are on Mac or Linux, then:
    ```
    sudo python2 -m pip install werkzeug==0.8.3
    sudo python2 -m pip install flask==0.9
    sudo python2 -m pip install Flask-login==0.1.3
    ```
  * On Windows, as an administrator:
    ```
    python -m pip install werkzeug==0.8.3
    python -m pip install flask==0.9
    python -m pip install Flask-login==0.1.3
    ```

## Usage

1. Download the files from GitHub.
2. Using the shell, change directory to the project folder, and start the portfolio server:
  1. On Mac or Linux, type:
    ```
    python2 app.py
    ```
  2. On Windows:
    ```
    python app.py
    ```
4. Visit this URL http://localhost:8000/ to see the portfolio page.
5. To stop the portfolio server, press [ctrl+c] from the shell.

## Troubleshooting

**I'm getting an error about port 8000 is already in use.**
* Please run the server on another port: 5000 or 8080, for ex. from the shell, type `export PORT=5000` and try again.
