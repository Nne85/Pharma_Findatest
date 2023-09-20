#!/usr/bin/python3

from flask import Flask, render_template
from models import storage
from models.pharmacy_store import PharmacyStore
from models.drugs import Drug

app = Flask(__name__)

"""@app.route("/")
def test():
    return "<p>This is a Test script</p>"
"""

@app.route('/drugs_by_pharmacies', strict_slashes=False)
def display_drugs_by_pharmacies():
    pharmacies = storage.all(PharmacyStore).values()
    pharmacies = [pharmacy for pharmacy in pharmacies if pharmacy and pharmacy.name is not None]
    pharmacies = sorted(pharmacies, key=lambda x: x.name)
    return render_template('drugs_by_pharmacies.html', pharmacies=pharmacies)


@app.route('/index', strict_slashes=False)
def display_drugs():
    return render_template('index.html')



@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
