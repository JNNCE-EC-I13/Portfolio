from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/')
def home():
	return render_template("index.html")


@app.route('/<string:page_name>')
def rand(page_name):
	return render_template(page_name)


@app.route('/submit_form', methods=["POST"])
def submit():
	try:
		data = request.form.to_dict()
		print(data)
		# with open("submitedForms", 'a', newline='') as f:
		# 	f.write(f"Email: {data['email']} || Subject: {data['subject']} || Message: {data['message']}\n")
		with open('database.csv', 'a', newline='') as csvfile:
			writer = csv.writer(csvfile)
			writer.writerow([data["email"], data["subject"], data["message"]])
		return render_template("contact.html", submitted='yes', data=data)
	except Exception as e:
		with open("log.txt", 'a', newline='') as f:
			f.write(str(e)) 
			f.write('\n')
		return render_template("contact.html", submitted='no', data=data)


if __name__ == "__main__":
	app.run(debug=True, port=8888)
