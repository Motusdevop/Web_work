from flask import Flask, render_template, request, url_for, redirect
from os import getcwd

folder = getcwd()
app = Flask(__name__, template_folder=folder, static_folder=folder)

devops = dict()
bulg = dict()

devops["Фёдоров Руслан"] = "Главный разработчик"

@app.route("/")
def index():
    return render_template("index.html", devops=devops, bulg=bulg)


@app.route("/admin", methods=['post', 'get'])
def admin():
    if request.method == "GET":
        return render_template("admin.html")
    else:
        name = request.form.get("name")
        otdel = request.form.get("otdel")
        work = request.form.get("work")
        if otdel == "1":
            devops[name] = work
        else:
            bulg[name] = work
        return redirect(url_for("admin"))

if __name__ == "__main__":
    app.run()
