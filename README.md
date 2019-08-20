# PortfolioSite_StarterCode
Source code for `Build a Portfolio site` Project.

The portfolio site includes a `Logo`, `Title`, and `Featured Work` highlighted with a respective box art imagery. it is a pure Html & CSS, utilizes a grid-based layout with styles making use of the flexbox.

## Features

* Built in web server.
* All content is responsive and displays on all display sizes.

## Examples

Check [My Portfolio Site](https://portfolio-wael.herokuapp.com/) for an example of Build a Portfolio Site.

## Installation

* Install Python from the python web site https://www.python.org
* Install Flask using Python's package manager pip from the shell like (`terminal` on Mac or Linux), or from `git bash` on Windows
  * If you are on Mac or Linux, then:
    ```
    sudo python3 -m pip install werkzeug==0.8.3
    sudo python3 -m pip install flask==0.9
    sudo python3 -m pip install Flask-login==0.1.3
    ```
  * On Windows, as an administrator:
    ```
    python -m pip install werkzeug==0.8.3
    python -m pip install flask==0.9
    python -m pip install Flask-login==0.1.3
    ```

## Usage

1. Download the files from GitHub.
2. To start the portfolio web server Using the terminal, CD to the project folder, then type `python3 app.py`, or on Windows by typing `python app.py`
3. Visit this URL http://localhost:8000/ to see the portfolio web page.
4. To stop the portfolio web server, press [ctrl+c] from the terminal.

## Troubleshooting

**I'm getting an error about port 8000 is already in use.**
* Please run the server on another port: 5000 or 8080, for ex. from the terminal, type `export PORT=5000` and try again.
