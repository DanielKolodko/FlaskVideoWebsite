from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Pass the YouTube video ID to the template
    video_id = "PAOA3fFs5kM"  # Extracted from https://www.youtube.com/watch?v=PAOA3fFs5kM
    return render_template('index.html', video_id=video_id)

if __name__ == "__main__":
    app.run(debug=True)
