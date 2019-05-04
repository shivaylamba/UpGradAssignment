from flask import Flask, request, jsonify, render_template
import Product
import ProductSchema
import config
from flask_mail import Mail, Message
import mail

app = config.app
db = config.db



# Init schema
product_schema = ProductSchema.ProductSchema(strict=True)
products_schema = ProductSchema.ProductSchema(many=True, strict=True)


# index page route
@app.route('/')
def index():
    allproducts = products_schema.dump(Product.Product.query.all()).data
    return render_template('main.html', allproducts=allproducts)


# Create a Product
@app.route('/product', methods=['POST'])
def add_product():
    name = request.json['name']
    image = request.json['image']
    price = request.json['price']

    new_product = Product.Product(name, price, image)

    db.session.add(new_product)
    db.session.commit()

    return product_schema.jsonify(new_product)


# search route
@app.route('/search/<search_term>', methods=['GET'])
def search(search_term):
    result_products = Product.Product.query.filter(Product.Product.name.like('%' + search_term + '%')).all()
    result = products_schema.dump(result_products)
    return jsonify(result.data)


# Get All Products
@app.route('/product', methods=['GET'])
def get_products():
    all_products = Product.Product.query.all()
    result = products_schema.dump(all_products)
    return jsonify(result.data)


# Get Single Products
@app.route('/product/<id>', methods=['GET'])
def get_product(id):
    # product = Product.Product.query.get(id)
    productdata = product_schema.dump(Product.Product.query.get(id)).data
    return render_template('product.html', product=productdata)
    # return product_schema.jsonify(product)


# Update a Product
@app.route('/product/<id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get(id)

    name = request.json['name']
    image = request.json['image']
    price = request.json['price']

    product.name = name
    product.image = image
    product.price = price

    db.session.commit()

    return product_schema.jsonify(product)


# Delete Product
@app.route('/product/<id>', methods=['DELETE'])
def delete_product(id):
    product = Product.Product.query.get(id)
    db.session.delete(product)
    db.session.commit()

    return product_schema.jsonify(product)


@app.route('/send-mail/<id>/<remail>')
def send_mail(id, remail):
    print(id, remail)
    productdata = product_schema.dump(Product.Product.query.get(id)).data
    msg = Message("Product Detils",
                  sender="rahul04jain90@gmail.com",
                  recipients=[remail])
    msg.body = "Here are the Product details that you wanted!"
    msg.html = render_template('product.html', product=productdata)

    mail.mail.send(msg)
    return 'Mail sent!'

# Run Server
if __name__ == '__main__':
    app.run(debug=True)
