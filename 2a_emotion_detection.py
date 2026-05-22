import requests
import json

def emotion_detector(text_to_analyze):
    """
    Sends input text to the IBM Watson NLP Emotion Predict service,
    extracts the individual emotion scores, and determines the dominant emotion.
    """
    # Define the target URL for the Watson Emotion Predict API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Configure the stock English workflow model metadata header
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    # Construct the input application payload structure
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    # Send the POST request to the Watson microservice
    response = requests.post(url, json=payload, headers=headers)
    
    # Parse the text response into a python dictionary json format
    formatted_response = json.loads(response.text)
    
    # Navigate the nested dictionary to extract the primary emotion scores
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # Find the key with the maximum value to identify the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Format and return the precise output dictionary expected by subsequent tasks
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
