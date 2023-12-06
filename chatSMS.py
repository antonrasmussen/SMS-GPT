# chatSMS.py

from twilio.rest import Client
import os
import openai
from flask import Flask, request

# Load environment variables
TWILIO_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
TWILIO_PHONE_NUMBER = os.environ['TWILIO_PHONE_NUMBER']
GPT_API_KEY = os.environ['GPT_API_KEY']

# Initialize Twilio client
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Initialize Flask app for receiving SMS
app = Flask(__name__)

# Initialize OpenAI
openai.api_key = GPT_API_KEY

def send_sms(to, message):
    """Send an SMS response using Twilio."""
    twilio_client.messages.create(
        body=message,
        from_=TWILIO_PHONE_NUMBER,
        to=to
    )

def query_gpt(prompt):
    """Query the GPT API with the given prompt."""
    response = openai.ChatCompletion.create(
        model="gpt-4",  # specify the model here
        messages=[{"role": "system", "content": "You are a helpful assistant."}, 
                  {"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content']

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Handle incoming SMS messages and respond with GPT-generated text."""
    incoming_msg = request.values.get('Body', '').strip()
    from_number = request.values.get('From', '')

    # Check if message starts with 'GPT:'
    if incoming_msg.startswith('GPT:'):
        prompt = incoming_msg[4:].strip()  # Extract the actual prompt
        gpt_response = query_gpt(prompt)
        send_sms(from_number, gpt_response)

    return "OK", 200

if __name__ == "__main__":
    app.run(debug=True)
