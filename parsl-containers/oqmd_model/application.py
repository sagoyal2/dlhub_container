import json
from home_run.models import ScikitLearnModel

# Create the flask app
from sklearn.externals import joblib

def predict(data):
    # Load in options form disk
    with open('options.json') as fp:
        options = json.load(fp)

    # Instantiate a HRModel for sklearn type
    ml = ScikitLearnModel(**options)

    #@app.route("/", methods=["POST"])
    #def slash_post():
    #body = request.get_json()
    return ml.run(data)
    # return json.dumps(ml.run(data))
    
#if __name__ == "__main__":
#    app.run(debug=True)
