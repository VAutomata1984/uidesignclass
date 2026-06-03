from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

# Started this on: 05/30/2026. 
# Finished this on: 06/3/2026.
# Code Author: Matthew Vollo
# UI Design HW 5 - Flask 


current_id = 4

sales = [
{
  "id": 1,
  "salesperson": "James D. Halpert",
  "client": "Shake Shack",
  "reams": 1000
},
{
  "id": 2,
  "salesperson": "Stanley Hudson",
  "client": "Toast",
  "reams": 4000
},
{
  "id": 3,
  "salesperson": "Michael G. Scott",
  "client": "Computer Science Department",
  "reams": 10000
},

]
clients = [
  "Shake Shack",
  "Toast",
  "Computer Science Department",
  "Teacher's College",
  "Starbucks",
  "Subsconsious",
  "Flat Top",
  "Joe's Coffee",
  "Max Caffe",
  "Nussbaum & Wu",
  "Taco Bell",
]

# ROUTES
@app.route('/')
def hello_world():
   return render_template('welcome.html')   


@app.route('/infinity')
def people():
    return render_template('log_sales.html', sales=sales, clients=clients)  


# AJAX FUNCTIONS
@app.route('/save_sale', methods=['GET','POST'])
def save_sale():
    global sales
    global clients 
    global current_id

    json_data = request.get_json()
    new_sale_data = json_data["new_sale"] 

    new_sale = {
        "id": current_id,
        "salesperson": new_sale_data["salesperson"],
        "client": new_sale_data["client"],
        "reams": new_sale_data["reams"]
    }

    current_id += 1
  
    sales.insert(0,new_sale)
    if new_sale_data["client"] not in clients:
      clients.append(new_sale_data["client"])
    
    return jsonify(sales=sales,clients=clients)

@app.route('/delete_sale', methods=['GET','POST'])
def delete_sale():
   global sales

   json_data = request.get_json()
   print(json_data)

   id_to_delete = json_data["id"] 

   for sale in sales:
      if sale["id"] == id_to_delete:
         sales.remove(sale)
         break

   return jsonify(sales=sales,clients=clients)

if __name__ == '__main__':
   app.run(debug = True)

