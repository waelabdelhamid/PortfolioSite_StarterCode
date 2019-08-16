# PortfolioSite_StarterCode
Source code for Build a Portfolio site Project.

The `Build a Portfolio Site` project consists of server-side code to run the web server, along with front-end code to display the portfolio main page which includes a `Logo`, `Title`, and highlighted the `Featured Work` with a respective box art imagery. Made with Python, Flask, Html, and CSS.

## Features

* Server utilizes the Python HTTP Server 1.1 with the Flask web development framework.
* Page utilizes a grid-based layout with styles making use of the Flexbox Layout Shifter Pattern.
* All content is responsive and displays on all display sizes includes: Desktop, Mobile: Google Nexus 5, Tablet: Apple iPad.
* Portfolio is a pure (HTML) structure, completely separated from design/style (CSS)
* Files are organized with a directory structure that separates files based on functionality. For example: static/ for stylesheets, images, JavaScript files, and templates/ for Html.

## Examples

Check [My Portfolio Site](https://portfolio-wael.herokuapp.com/) for an example of Build a Portfolio Site.

## Installation

* [Git bash](https://git-scm.com/downloads) is required for windows.
* [Python 2.7](https://www.python.org/downloads/release/python-2712/) or higher is required.

*Note: The next installation must be done from the shell like (terminal on Mac or Linux, git bash on windows)*
* [virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) is optional, but if you will use, you must Create& Activate the environment inside the cloned project folder.
* [Flask](https://flask.palletsprojects.com/en/1.0.x/installation/#python-version) is required.

## How To run this site

1. Fork the starter repo
2. Clone the remote to your local machine
3. Using the terminal, change directory to the cloned project folder, then type `python app.py` to lunch the server.
4. Once it is up and running, visit this URL http://localhost:8000/ to see the portfolio page.
5. To stop the portfolio server press [ctrl+c] from the terminal.

## Troubleshooting

**I'm getting an error about port 8000 is already in use.**
* Please run the server on another port: 5000 or 8080, for ex. from terminal, type `export PORT=5000` and try again.
