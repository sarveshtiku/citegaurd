#!/bin/bash

# Welcome to CiteGuard Installation Script!

# Step 1: Clone the repository
echo "Cloning the CiteGuard repository..."
git clone https://github.com/yourusername/citeguard.git
cd citeguard || exit

# Step 2: Create a new branch for your feature
echo "Creating a new branch for your feature..."
git checkout -b feature-name

# Step 3: Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Step 4: Run the Flask app
echo "Starting the Flask app..."
python app.py

# Step 5: Open the app in your browser
echo "Access the app at: http://127.0.0.1:5000"

# Info: About CiteGuard
echo "✨ What is CiteGuard?"
echo "Upload a PDF research paper, and CiteGuard will process it to flag problematic claims or references."

# Info: Why Choose CiteGuard
echo "🤔 Why CiteGuard?"
echo " - 🕒 Saves Time: Automates tedious validation tasks for peer reviewers."
echo " - 🔒 Enhances Credibility: Helps researchers ensure the integrity of their work."
echo " - 🌍 Supports Collaboration: Trusted by researchers worldwide for its accuracy and simplicity."

# Info: Tech Stack
echo "🛠️ Tech Stack:"
echo " - Frontend: HTML, CSS, JavaScript"
echo " - Backend: Flask (Python)"
echo " - AI/NLP: Hugging Face Transformers"
echo " - PDF Tools: PyPDF2, Tesseract OCR"

# Repository Overview
echo "📦 Repository Overview:"
echo " - /static/: Contains CSS and JavaScript files for the web interface."
echo " - /templates/: HTML templates for rendering web pages."
echo " - /uploads/: Folder for temporary file storage during analysis."
echo " - app.py: Main Flask application handling file uploads and AI processing."
echo " - requirements.txt: List of dependencies for the project."

# How to Contribute
echo "❤️ How to Contribute:"
echo " 1. Fork the repository."
echo " 2. Create your branch:"
echo "    git checkout -b feature-name"
echo " 3. Make your changes and commit them:"
echo "    git commit -m 'Added a new feature'"
echo " 4. Push your branch to your forked repository:"
echo "    git push origin feature-name"
echo " 5. Submit a pull request on the original repository."

# Feedback & Support
echo "📢 Feedback & Support:"
echo "Got questions? Open an issue on the GitHub page."
echo "For direct inquiries, reach out to the team at: contact@citeguard.com"

# Wrap-up
echo "💻 Start Your Journey Towards Research Integrity with CiteGuard!"
echo "📂 Clone the repo now and get started!"
