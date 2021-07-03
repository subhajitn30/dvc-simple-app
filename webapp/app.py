from logging import error
from flask import Flask, render_template, request, jsonify
import os
from flask.wrappers import Response
import yaml
import joblib
import numpy as np


param_path= "C:/Users/subha/Data_Science/mlflow_DVC/simple_app/params.yaml"
webapp_root="C:/Users/subha/Data_Science/mlflow_DVC/simple_app/webapp"

static_dir=os.path.join(webapp_root,"static")
template_dir=os.path.join(webapp_root,"templates")

app=Flask(__name__, static_folder=static_dir, template_folder=template_dir)

def read_param(config_path):
    with open(config_path) as yaml_file:
        config=yaml.safe_load(yaml_file)
    return config

def predict(data):
    config=read_param(param_path)
    model_dir_path=config["webapp_model_dir"]
    model=joblib.load(model_dir_path)
    prediction=model.predict(data)
    print(prediction)
    return prediction[0]

def api_response(request):
    try:
        data=np.array([list(request.json.values())])
        response=predict(data)
        response={'response':response}
        return response
    except Exception as e:
        print(e)
        error={"error": "Something went wrong!! Please try again"}
        return error






@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            if request.form:
                data=dict(request.form).values()
                data=[list(map(float,data))]
                response=predict(data)
                return render_template("index.html", response=response)
            elif request.json:
                response=api_response(request)
                return jsonify(response)
        except Exception as e:                                              ## Exception handling
            print(e)
            error={"error": "Something went wrong!! Please try again"}
            return render_template("404.html",error=error)
    else:
        print(template_dir)
        return render_template("index.html")

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

