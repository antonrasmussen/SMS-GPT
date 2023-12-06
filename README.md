# SMS-to-GPT API Bridge (Python & Twilio)
A Simple App to Query Chat-GPT using SMS

## Overview

This project allows users to interact with the GPT API via SMS using Python and Twilio. Users can send an SMS starting with "GPT:" followed by their query, and the system processes this request through the GPT API, returning the response as an SMS.

## Features

- **Twilio SMS Integration**: Seamless handling of SMS interactions.
- **GPT API Integration**: Query processing through the GPT API.
- **Security and Rate Limiting**: Basic security measures and usage limitations.

## Prerequisites

- A Twilio account and a Twilio phone number.
- Access to the GPT API.
- A server environment for hosting the application (e.g., Heroku, AWS).
- Python 3.x.

## Installation

1. **Clone the Repository**

`git clone https://github.com/yourusername/sms-to-gpt-api-python.git
cd sms-to-gpt-api-python`

2. **Install Dependencies**

`pip install -r requirements.txt`


3. **Environment Setup**
- Set up your Twilio account SID, Auth Token, and phone number.
- Configure your GPT API key.
- Example `.env` file:
  ```
  TWILIO_ACCOUNT_SID=your_account_sid
  TWILIO_AUTH_TOKEN=your_auth_token
  TWILIO_PHONE_NUMBER=your_twilio_phone_number
  GPT_API_KEY=your_gpt_api_key
  ```

4. **Running the Application**

`python chatSMS.py`


## Usage

1. **Send an SMS**
- Format: `GPT:<Your Query>`
- Send this message to the Twilio phone number.

2. **Receive a Response**
- The system processes your query and sends back a response via SMS.


## License

Distributed under the MIT License. See `LICENSE` for more information.


