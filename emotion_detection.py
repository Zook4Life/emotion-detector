import requests
import json

def emotion_detector(text_to_analyze):
    # URL of the Watson NLP emotion predictor service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Headers required by the Watson NLP API
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Payload format matching the Watson NLP runtime requirements
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Sending the POST request to the API
    response = requests.post(url, json=myobj, headers=headers)
    
    # Parsing the response text into a dictionary
    formatted_response = json.loads(response.text)
    
    # Extracting the target emotion metrics from the JSON structure
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']
    
    # Finding the highest scoring emotion
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Constructing the final required output format
    result = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }
    
    return result
