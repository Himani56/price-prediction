from flask import Flask,request,jsonify,render_template
from doubt import abc

app = Flask(__name__)
obj = abc()


@app.route("/home")
def home():
    global obj
    response = jsonify({
        'locations': obj.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response
    
    


@app.route("/get_location_names")
def get_location_names():
    global obj
    response = jsonify({
        'locations': obj.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/predict_home_price',methods=['POST'])
def predict_home_price():
    global obj
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])
    response = jsonify(({
        'estimated_price': obj.get_estimated_price(location,total_sqft,bhk,bath)

    }))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__=="__main__":
    print("Starting Flask server for Price Prediction")
    obj.load_saved_artifacts()
    app.run()
