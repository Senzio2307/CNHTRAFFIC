from flask import Flask, request, send_file
import pandas as pd
import io

app = Flask(__name__)

@app.route('/download', methods=['GET'])
def download_file():
    url = request.args.get('url')
    format = request.args.get('format')

    # Simuleer het ophalen van data
    data = {
        "Datum": ["2024-04-01", "2024-04-02"],
        "Activiteit": ["Laden", "Lossen"],
        "Locatie": ["Zedelgem", "Gent"]
    }

    df = pd.DataFrame(data)

    if format == 'excel':
        output = io.BytesIO()
        df.to_excel(output, index=False)
        output.seek(0)
        return send_file(output, download_name="planning.xlsx", as_attachment=True)

    return "Ongeldig formaat of formaat nog niet geïmplementeerd", 400

if __name__ == '__main__':
    app.run(debug=True)