from flask import json, request, jsonify
# test post form
def test_index_get(client):
    response = client.get('/')
    assert response.status_code == 200
def test_prediction(client):
    response = client.post('/result', json={'Pregnancies': '6', 'Glucose': '148', 'BloodPressure': '72', 'SkinThickness': '35', 'Insulin': '0', 'BMI': '33.6', 'DiabetesPedigreeFunction': '0.627', 'Age': '50'})
    data = response.get_json()
    #assert data['prediction'] == 1