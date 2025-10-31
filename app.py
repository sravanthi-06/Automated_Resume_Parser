from flask import Flask, render_template, request
from parser import parse_resume
import os
from fpdf import FPDF  # To create a sample resume PDF

# Initialize Flask app
app = Flask(__name__)

# Define upload folder for resumes
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Create a sample resume PDF automatically (if not exists)
sample_resume_path = os.path.join(UPLOAD_FOLDER, "sample_resume.pdf")
if not os.path.exists(sample_resume_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="John Doe", ln=True, align='L')
    pdf.cell(200, 10, txt="Email: john.doe@example.com", ln=True, align='L')
    pdf.cell(200, 10, txt="Phone: +91 9876543210", ln=True, align='L')
    pdf.cell(200, 10, txt="Education: B.Tech in Computer Science", ln=True, align='L')
    pdf.cell(200, 10, txt="Skills: Python, Flask, Machine Learning, SQL", ln=True, align='L')
    pdf.cell(200, 10, txt="Experience: 1 year as Python Developer Intern", ln=True, align='L')
    pdf.output(sample_resume_path)

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        # Get uploaded file from HTML form
        file = request.files["resume"]

        if file and file.filename.endswith(".pdf"):
            # Save uploaded file to uploads folder
            file_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(file_path)

            # Call the resume parser function
            data = parse_resume(file_path)

            # Render the template with parsed data
            return render_template("index.html", data=data)
        else:
            return render_template("index.html", data="Please upload a valid PDF file.")

    # Default page load (GET method)
    return render_template("index.html", data=None)

if __name__ == "__main__":
    # Run Flask app
    app.run(debug=True)
