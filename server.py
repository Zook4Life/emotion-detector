from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initialize the Flask application
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    """
    Analyzes the text passed via the query parameter and returns
    a formatted string containing emotion scores and the dominant emotion.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Pass the text to the detector function
    response = emotion_detector(text_to_analyze)
    
    # Extract scores and dominant emotion from the response dictionary
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    
    # Handle case where text might be blank or invalid
    if dominant_emotion is None:
        return "Invalid text! Please try again."
        
    # Construct the final display string as required by the lab layout
    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Renders the main application HTML interface.
    """
    return render_template('index.html')

if __name__ == "__main__":
    # Run the application on localhost port 5000
    app.run(host="0.0.0.0", port=5000)
