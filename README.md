#!/bin/bash

# CiteGuard Installation and Usage Script
# ---------------------------------------

# ✨ **CiteGuard**: Your companion for research integrity!
# Upload a PDF research paper, and CiteGuard will process it to flag problematic claims or references.

echo "🚀 Quick Start Guide for CiteGuard"

# Step 1: Clone the repository
echo "✨ Step 1: Cloning the repository..."
git clone https://github.com/yourusername/citeguard.git
cd citeguard || exit
echo "Repository cloned successfully."

# Step 2: Create a new branch for your feature
echo "✨ Step 2: Creating a new branch for your feature..."
git checkout -b feature-name
echo "Branch created successfully."

# Step 3: Install dependencies
echo "✨ Step 3: Installing dependencies..."
pip install -r requirements.txt
echo "Dependencies installed successfully."

# Step 4: Run the Flask app
echo "✨ Step 4: Running the Flask app..."
python app.py &
FLASK_PID=$!
echo "Flask app is running in the background."

# Step 5: Open the app in your browser
echo "✨ Step 5: Access the app in your browser at http://127.0.0.1:5000"

# What is CiteGuard
echo "✨ What is CiteGuard?"
echo "Upload a PDF research paper, and CiteGuard will process it to flag problematic claims or references."

# Why CiteGuard
echo "🤔 Why Choose CiteGuard?"
echo " - 🕒 Saves Time: Automates tedious validation tasks for peer reviewers."
echo " - 🔒 Enhances Credibility: Helps researchers ensure the integrity of their work."
echo " - 🌍 Supports Collaboration: Trusted by researchers worldwide for its accuracy and simplicity."

# Tech Stack
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
echo " 2. Create a branch:"
echo "    git checkout -b feature-name"
echo " 3. Make your changes and commit them:"
echo "    git commit -m 'Added a new feature'"
echo " 4. Push your changes:"
echo "    git push origin feature-name"
echo " 5. Open a pull request on GitHub."

# Feedback & Support
echo "📢 Feedback & Support:"
echo " - Open an issue on the GitHub page for questions or suggestions."
echo " - Contact us directly at contact@citeguard.com."

# Wrap-up
echo "💻 Start Your Journey Towards Research Integrity with CiteGuard!"
echo "Clone the repo now and get started:"
echo "git clone https://github.com/yourusername/citeguard.git"

# End message
echo "🎉 All done! Visit http://127.0.0.1:5000 to start using CiteGuard."
echo "To stop the Flask server, use the command: kill $FLASK_PID"
