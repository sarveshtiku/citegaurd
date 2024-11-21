from flask import Flask, render_template, request, jsonify
import os
import PyPDF2
from transformers import pipeline
from pdf2image import convert_from_path  # For OCR
import pytesseract
from PIL import Image

app = Flask(__name__, template_folder="templates", static_folder="static")
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Load the NLP model
analyzer = pipeline("text-classification", model="textattack/bert-base-uncased-snli")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    # Save the uploaded file
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)
    print(f"File uploaded: {filepath}")  # Debug

    # Extract text from the PDF
    text = extract_text(filepath)
    if not text or text.strip() == "":
        print("Failed to extract text!")  # Debug
        return jsonify({"error": "Failed to extract text from the PDF."}), 500

    print(f"Extracted text: {text[:500]}...")  # Debug

    # Analyze the text
    flagged_statements = analyze_text(text)
    print(f"Flagged statements: {flagged_statements}")  # Debug

    return jsonify({"flagged_statements": flagged_statements})

def extract_text(pdf_path):
    try:
        with open(pdf_path, 'rb') as f:
            pdf_reader = PyPDF2.PdfReader(f)
            text = "".join([page.extract_text() for page in pdf_reader.pages])
            if text.strip():  # If text is found
                print("Text extracted using PyPDF2.")  # Debug
                return text.strip()

        # Fallback to OCR if no text found
        print("No text found with PyPDF2. Attempting OCR...")
        images = convert_from_path(pdf_path)
        ocr_text = ""
        for image in images:
            ocr_text += pytesseract.image_to_string(image)
        print("Text extracted using OCR.")  # Debug
        return ocr_text.strip()

    except Exception as e:
        print(f"Error extracting text: {e}")  # Debug
        return None

def analyze_text(text):
    sentences = text.split('. ')
    flagged = []
    for sentence in sentences:
        if sentence.strip():
            print(f"Analyzing sentence: {sentence}")  # Debug
            try:
                result = analyzer(sentence)
                print(f"Result: {result}")  # Debug
                if result[0]['label'] == 'CONTRADICTION' and result[0]['score'] > 0.8:
                    flagged.append({"text": sentence, "score": result[0]['score']})
            except Exception as e:
                print(f"Error analyzing sentence: {e}")  # Debug
    print(f"Final flagged statements: {flagged}")  # Debug
    return flagged

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
