from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder="public")

@app.route("/")
def home():
    return app.send_static_file("index1.html")

@app.route("/download")
def download_file():
    # Envía el Excel desde public/files
    return send_from_directory(
        directory=os.path.join(app.root_path, "public", "files"),
        path="C:/Users/llede/Downloads/EJEPLO/Predicciones_Abandono_2034.xlsx",
        as_attachment=True,
        download_name="Predicciones_abandono_2034.xlsx"
    )

if __name__ == "__main__":
    app.run(debug=True)
