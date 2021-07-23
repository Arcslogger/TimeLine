from flask import Flask,render_template,request

import methods as methods

#cd Documents\Ivans Documents\Code\TimeLine
    #or make sure ur cmd prompt is in the timeline folder
#set FLASK_APP=main.py
#set FLASK_DEBUG=1
#flask run

app = Flask(__name__)

#route and url for the home page
@app.route('/')
def index():
    return render_template("index.html")

#route and url for the explore page
@app.route('/explore', methods=["POST","GET"])
def explore():
    #check if the form received input
    if request.method == "POST":
        
        #Gets the address from the address input field
        address = str(request.form["address"])

        #Gets the location type and formats the string into a tag for the API
        type = str(request.form["place"])
        typeTag = ""
        typeTag = type.lower()
        typeTag = typeTag.replace(" ","_")

        #Gets the radius from the slider input
        radius = str(request.form["radius"])

        #Calls the backend python method, that takes the 3 parameters and write all open locations with their
        # busyness and ratings in that radius into a json file
        #See methods.py for the full method
        methods.writeFile(methods.query(typeTag,address,radius))
        
        #Refreshes the page with the current search results saved
        return render_template("explore.html",addressSave=address,typeSave=type,radiusSave=radius)
    else:
        #if no input, refresh the page with no change
        return render_template("explore.html",radiusSave=5000)

#route and url for the about page
@app.route("/about")
def about():
    return render_template("about.html")

#Runs the app
if __name__=="__main__'":
    app.run(debug=True)

