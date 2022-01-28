# Work From Airbnb API

Work from home api is a simple Flask api that checks if a given Airbnb listing has at least one of the following elements: "Table, Desk, Office chair" using Google vision API to analyse the pictures.

This app was created to explore Google Vision API, Docker, Unit testing and Heroku.
The use case is something I actually need when browsing Airbnb listing. I need to make sure I can work from the place.


## Installation

Create and activate a virtual environment.

```bash
python3 -m venv env
source env/bin/activate
```


Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Litreview.

```bash
pip3 install -r requirements.txt
```

## Usage

Launch the server:

```bash
python3 work_from_home_api/app.py
```
Visit the website in your browser at:
```
http://127.0.0.1:8000/
```

Add the url of the listing you want to inspect to the url:
(you can leave the search parameters in the url)
```
http://127.0.0.1:8000/https://www.airbnb.fr/rooms/36216130/photos?guests=1&adults=1
```
The API returns the found furniture:

```
Table, Office chair
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
