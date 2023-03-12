import numpy as np
from pickle import load
from flask import Flask, render_template, request, redirect, url_for
import warnings
warnings.filterwarnings('ignore')


app = Flask(__name__)

model = load(open('mdl/pipe_final_model.bin', 'rb'))

@app.route('/')
def home():
  return render_template('index.html', output_price=False)

@app.route("/predict", methods=["POST"])
def predict():
  try:
    brand = str(request.form.get("brand")).lower().strip()
    typa = str(request.form.get("typa")).lower().strip()
    cpu = " ".join(str(request.form.get("cpu")).lower().split()).strip()
    ram = int(str(request.form.get("ram")))
    sc_res = str(request.form.get("sc_res")).lower().strip()
    sc_size = float(str(request.form.get("sc_size")).lower().strip())
    touch_screen = {"yes": 1, "no": 0}[str(request.form.get("touchscreen")).lower()]
    ips = {"yes": 1, "no": 0}[str(request.form.get("ips")).lower()]
    gpu = " ".join(str(request.form.get("gpu")).lower().split()).strip()
    os = str(request.form.get("os")).lower().strip()
    NVMe = str(request.form.get("NVMe")).lower().strip()
    SSD = str(request.form.get("SSD")).lower().strip()
    HDD = str(request.form.get("HDD")).lower().strip()
    weight = float(str(request.form.get("weight")).lower().strip())


    NVMe = int(NVMe) if NVMe.isdigit() else 0
    SSD = int(SSD) if SSD.isdigit() else 0
    HDD = int(HDD) if HDD.isdigit() else 0
    ppi = sum(map(lambda x:x**2, map(int, sc_res.split("x")))) ** 0.5 / sc_size

    output = int(np.exp(model.predict([[brand, typa, cpu, ram, gpu, os, weight, ppi, NVMe, SSD, HDD, touch_screen, ips]])[0]))
    error = False
  except:
    output = False
    error = True

  return render_template('index.html', output_price=output, error=error)
  


if __name__ == "__main__":
    app.run(debug=True)

    
  
