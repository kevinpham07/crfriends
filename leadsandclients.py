from flask import Flask, render_template, redirect, request
from mysqlconnection import connectToMySQL
app = Flask(__name__)

mysql = connectToMySQL("lead_gen_business")

@app.route("/")
def index():
	lead = mysql.query_db("SELECT COUNT(leads.leads_id) AS leads, CONCAT_WS(' ',clients.first_name, clients.last_name) AS full_names FROM leads JOIN sites ON leads.site_id = sites.site_id JOIN clients on clients.client_id = sites.client_id GROUP BY CONCAT_WS(' ',clients.first_name, clients.last_name)")
	return render_template("leadsandclients.html", l = lead)

if __name__ == "__main__":
	app.run(debug = True)