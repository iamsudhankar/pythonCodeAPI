from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/getResponse', methods=['POST'])
def submit_form():
    try:
        # Get the form data from the request
        data = request.form

        # Process the form data (you can perform any logic here)
        result = {}
        for key, value in data.items():
            result[key] = value

        # Return a JSON response with the result
        return jsonify({"message": "Form data submitted successfully", "data": result})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5002) 
