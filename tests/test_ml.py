from flask import json, request, jsonify
# test post form
def test_index_get(client):
    response = client.get('/')
    assert response.status_code == 200
def test_prediction(client):
    response = client.post('/result', data={'Pregnancies': '6', 'Glucose': '148', 'BloodPressure': '72', 'SkinThickness': '35', 'Insulin': '0', 'BMI': '33.6', 'DiabetesPedigreeFunction': '0.627', 'Age': '50'})
    resp_data = response.get_json()
    assert resp_data['prediction'] == 1