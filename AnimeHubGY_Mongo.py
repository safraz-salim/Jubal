from flask import Flask, jsonify, request, render_template

import mongoengine as db
import json

# Create Flask application object
app = Flask(__name__)


# Create connection to CKCS145 MongoDB database
client = db.connect('AnimeHubGY', username='', password='')

"""

{
"customerName":"Jason Keener",
"customerAddress":"1 Region Street",
"customerRegion":"Carribean",
"customerEmail":"jk@georgetown.gy",
"customerPhoneNo":"123-1122",
"packageNo":2,
"totalPrice":0
}

"""

# Data Class for accessing MongoDB collection
class Order(db.Document):
    name = db.StringField()
    email = db.StringField()
    
    customerName = db.StringField()
    customerAddress = db.StringField()
    customerRegion = db.StringField()
    customerEmail = db.StringField()
    customerPhoneNo = db.StringField()
    packageNo = db.IntField()
    totalPrice = db.IntField()
    
    meta = {'collection': 'Order', 'allow_inheritance': False}
    
    
# http://localhost:5000/test
@app.route('/test')
def test() :
    
    return 'Successful reply from test route!!!' 
    

# http://localhost:5000/
@app.route('/')
def default() :
    
    return render_template('orderform-v4-AJAX.html')


# A route to list all users.
# http://localhost:5000/order/list
@app.route('/order/list', methods = ['GET']) #Enable GET and POST
def list_all():	
    
    return json.loads( Order.objects.to_json() ) 


# http://localhost:5000/order/new
@app.route('/order/new', methods = ['POST'] )  
def place_order() :	

    """
    if(request.method == 'GET'):
    return render_template('orderform-v4-AJAX.html')
    """
  
    # following code will execute for POST requests

    customer_name_val = request.form.get('customerName')
    customer_address_val = request.form.get('customerAddress')
    customer_region_val = request.form.get('customerRegion')
    customer_email_val = request.form.get('customerEmail')
    customer_phone_val = request.form.get('customerPhoneNo')
    package_no_val = request.form.get('packageNo')
  
    # Debug
    print( customer_name_val )
    print( customer_address_val )
    print( customer_region_val )
    print( customer_email_val, customer_phone_val )
    print( package_no_val )

    newOrder = Order(customerName=customer_name_val, customerAddress=customer_address_val, customerRegion=customer_region_val, customerEmail=customer_email_val, customerPhoneNo=customer_phone_val, packageNo=package_no_val, totalPrice=0 )   
    newOrder.save()

    return 'Order has been placed'

if __name__ == '__main__':
    app.run( host='0.0.0.0', debug=True)
