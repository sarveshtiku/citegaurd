const form = document.getElementById('uploadForm');
form.onsubmit = async (event) => {
    event.preventDefault();
    const file = document.getElementById('fileInput').files[0];
    const formData = new FormData();
    formData.append('file', file);

    document.getElementById('result').innerHTML = "<p>Analyzing...</p>";

    try {
        const response = await fetch('/upload', {
            method: 'POST',
            body: formData,
        });
        const result = await response.json();
        console.log("Backend response:", result);  // Debug

        if (result.flagged_statements && result.flagged_statements.length > 0) {
            let output = "<h3>Flagged Statements:</h3><ul>";
            result.flagged_statements.forEach(flag => {
                output += `<li>${flag.text} (Confidence: ${flag.score.toFixed(2)})</li>`;
            });
            output += "</ul>";
            document.getElementById('result').innerHTML = output;
        } else if (result.error) {
            document.getElementById('result').innerHTML = `<p>Error: ${result.error}</p>`;
        } else {
            document.getElementById('result').innerHTML = "<p>No flagged statements found.</p>";
        }
    } catch (error) {
        console.error("Error:", error);
        document.getElementById('result').innerHTML = "<p>An error occurred while processing the file.</p>";
    }
};
