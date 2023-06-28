from flask import Flask, request, render_template
# from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd


app = Flask(__name__)
model = pickle.load(open("flight.pkl", "rb"))


@app.route("/")
# @cross_origin()
def index():
    return render_template("index.html")

@app.route("/predict", methods = ["GET", "POST"])
# @cross_origin()
def predict():
    if request.method == "POST":

        # Date_of_Journey
        date_dep = request.form["departure"]
        journey_day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
        journey_month = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").month)
        # print("Journey Date : ",Journey_day, Journey_month)

        # Departure
        dep_hour = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").hour)
        dep_min = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").minute)
        # print("Departure : ",Dep_hour, Dep_min)

        # Arrival
        date_arr = request.form["arrival"]
        arrival_hour = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").hour)
        arrival_min = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").minute)
        # print("Arrival : ", Arrival_hour, Arrival_min)

        # Duration
        Duration_hour = abs(arrival_hour - dep_hour)
        Duration_mins = abs(arrival_min - dep_min)
        # print("Duration : ", dur_hour, dur_min)

        # Total Stops
        Total_Stops = int(request.form["stopage"])
        # print(Total_stops)



        airline=request.form['airline']
        if(airline=='Vistara'):
            Airline_Vistara = 1
            Airline_Air_India = 0
            Airline_IndiGo = 0
            Airline_AirAsia = 0
            Airline_GO_FIRST = 0
            Airline_SpiceJet = 0
            Airline_AkasaAir = 0
            Airline_AllianceAir = 0
            Airline_StarAir = 0

        elif (airline=='Air_India'):
            Airline_Vistara = 0
            Airline_Air_India = 1
            Airline_IndiGo = 0
            Airline_AirAsia = 0
            Airline_GO_FIRST = 0
            Airline_SpiceJet = 0
            Airline_AkasaAir = 0
            Airline_AllianceAir = 0
            Airline_StarAir = 0

        elif (airline=='Indigo'):
            Airline_Vistara = 0
            Airline_Air_India = 0
            Airline_IndiGo = 1
            Airline_AirAsia = 0
            Airline_GO_FIRST = 0
            Airline_SpiceJet = 0
            Airline_AkasaAir = 0
            Airline_AllianceAir = 0
            Airline_StarAir = 0
            
        elif (airline=='AirAsia'):
            Airline_Vistara = 0
            Airline_Air_India = 0
            Airline_IndiGo = 0
            Airline_AirAsia = 1
            Airline_GO_FIRST = 0
            Airline_SpiceJet = 0
            Airline_AkasaAir = 0
            Airline_AllianceAir = 0
            Airline_StarAir = 0
            
        elif (airline=='GO_FIRST'):
            Airline_Vistara = 0
            Airline_Air_India = 0
            Airline_IndiGo = 0
            Airline_AirAsia = 0
            Airline_GO_FIRST = 1
            Airline_SpiceJet = 0
            Airline_AkasaAir = 0
            Airline_AllianceAir = 0
            Airline_StarAir = 0
            
        elif (airline=='SpiceJet'):
            Airline_Vistara = 0
            Airline_Air_India = 0
            Airline_IndiGo = 0
            Airline_AirAsia = 0
            Airline_GO_FIRST = 0
            Airline_SpiceJet = 1
            Airline_AkasaAir = 0
            Airline_AllianceAir = 0
            Airline_StarAir = 0

        elif (airline=='AkasaAir'):
            Airline_Vistara = 0
            Airline_Air_India = 0
            Airline_IndiGo = 0
            Airline_AirAsia = 0
            Airline_GO_FIRST = 0
            Airline_SpiceJet = 0
            Airline_AkasaAir = 1
            Airline_AllianceAir = 0
            Airline_StarAir = 0

        elif (airline=='AllianceAir'):
            Airline_Vistara = 0
            Airline_Air_India = 0
            Airline_IndiGo = 0
            Airline_AirAsia = 0
            Airline_GO_FIRST = 0
            Airline_SpiceJet = 0
            Airline_AkasaAir = 0
            Airline_AllianceAir = 1
            Airline_StarAir = 0

        else:
            Airline_Vistara = 0
            Airline_Air_India = 0
            Airline_IndiGo = 0
            Airline_AirAsia = 0
            Airline_GO_FIRST = 0
            Airline_SpiceJet = 0
            Airline_AkasaAir = 0
            Airline_AllianceAir = 0
            Airline_StarAir = 1


        Source = request.form["source"]
        if (Source == 'Bangalore'):
            Source_Bangalore = 1
            Source_Delhi = 0
            Source_Mumbai = 0
            Source_Chennai = 0

        elif (Source == 'Delhi'):
            Source_Bangalore = 0
            Source_Delhi = 1
            Source_Mumbai = 0
            Source_Chennai = 0

        elif (Source == 'Mumbai'):
            Source_Bangalore = 0
            Source_Delhi = 0
            Source_Mumbai = 1
            Source_Chennai = 0

        else:
            Source_Bangalore = 0
            Source_Delhi = 0
            Source_Mumbai = 0
            Source_Chennai = 1


        Source = request.form["destination"]
        if (Source == 'Mumbai'):
            Destination_Mumbai = 1
            Destination_Delhi = 0
            Destination_Kolkata = 0
            Destination_Hyderabad = 0
            Destination_Bangalore = 0
        
        elif (Source == 'Delhi'):
            Destination_Mumbai = 0
            Destination_Delhi = 1
            Destination_Kolkata = 0
            Destination_Hyderabad = 0
            Destination_Bangalore = 0

        elif (Source == 'Kolkata'):
            Destination_Mumbai = 0
            Destination_Delhi = 0
            Destination_Kolkata = 1
            Destination_Hyderabad = 0
            Destination_Bangalore = 0

        elif (Source == 'Hyderabad'):
            Destination_Mumbai = 0
            Destination_Delhi = 0
            Destination_Kolkata = 0
            Destination_Hyderabad = 1
            Destination_Bangalore = 0

        else:
            Destination_Mumbai = 0
            Destination_Delhi = 0
            Destination_Kolkata = 0
            Destination_Hyderabad = 0
            Destination_Bangalore = 1

        prediction=model.predict([[
            Total_Stops,
            journey_day,
            journey_month,
            dep_hour,
            dep_min,
            arrival_hour,
            arrival_min,
            Duration_hour,
            Duration_mins,
            Airline_Vistara,
            Airline_Air_India,
            Airline_IndiGo,
            Airline_AirAsia,
            Airline_GO_FIRST,
            Airline_SpiceJet,
            Airline_AkasaAir,
            Airline_AllianceAir,
            Source_Bangalore,
            Source_Delhi,
            Source_Mumbai,
            Destination_Mumbai,
            Destination_Delhi,
            Destination_Kolkata,
            Destination_Hyderabad,
        ]])

        output=round(prediction[0],2)

        return render_template('predict.html',prediction_text="Your Flight price is Rs. {}".format(output))

    return render_template("predict.html")

if __name__ == "__main__":
    app.run(debug=True)
