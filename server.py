"""
Runs the Emotion Detector Flask application.

This module starts the Flask server and deploys the Emotion Detector 
API locally at http://localhost:5000. When executed, it initializes 
the Flask app and handles incoming requests for emotion analysis.
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emototion Detector")

@app.route("/")
def render_index_page():
    """Render and return the main index page of the web application."""
    return render_template("index.html")

@app.route("/emotionDetector")
def sent_detector():
    """
    Analyze the input text for emotions and return the detected emotion
    scores.

    This route receives text from the query parameter 'textToAnalyze',
    processes it using the emotion detector, and returns a formatted
    response showing the emotion scores and dominant emotion.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statemenet, the system response is"
        f" 'anger': {response['anger']}, 'disgust': {response['disgust']},"
        f" 'fear': {response['fear']}, 'joy': {response['joy']} and"
        f" 'sadness': {response['sadness']}. The dominant emotion"
        f" is <b> {response['dominant_emotion']} </b>"
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
