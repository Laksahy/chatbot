from flask import Flask, request, render_template
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, Float
from boss.claas_1 import Product

app = Flask(__name__)

# create the engine and session
engine = create_engine('sqlite:///mydatabase.db', echo=True)
Session = sessionmaker(bind=engine)

@app.route('/')
def index():
    return render_template('home_1.html')

@app.route('/product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        # retrieve the submitted form data
        name_1 = request.form['name']
        price_1 = request.form['price']

        # create a new Product object with the form data
        product = Product(name=name_1, price=price_1)

        # add the new product to the database
        session = Session()
        session.add(product)
        session.commit()

        return "Product added successfully!"

    # if the request method is GET, show the form to the user
    return render_template('add_product.html')
if __name__ == '__main__':
     #app.run(debug = True,port=8080)
     app.run(host='0.0.0.0')