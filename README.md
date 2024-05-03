# Bulk SMS Sender

## Introduction

This is a user-friendly Python Application built with Tkinter that enables users to send bulk sms Messages with the help of Africa's talking API.

## Features

- <b>CSV File Upload:</b> Easily uploads a csv file containing phone numbers.
- <b>Africa's talking API Integration:</b> This enables reliable and scalable SMS messaging.
- <b>Customizable Messaging:</b> Tailor your messages to suit your audience with the ability to compose custom messages directly within the application.

## Prerequisites

- Python3 installed on your system.
- Africa's Talking API Credentials(Username and API key).
- Python Packages: `tkinter`, `africastalking`, `PIL`, and `dotenv`.

## Installation

1. Clone this repository:
   `git clone https://github.com/TechDanny/Send-bulk-SMS.git`
2. Navigate to the project directory:
   `cd Send-bulk-SMS`
3. Install the required Python packages:
   `pip install -r requirements.txt`
4. Configure API Credentials:
   Create a `.env` file in the project directory and the following:
   `AFRICASTALKING_USERNAME=your_username`
   `AFRICASTALKING_API_KEY=your_api_key`

## Usage

1. Run the application by executing the `python3 app.py` file.
2. Provide API Credentials: `Enter your Africa's Talking API username`
3. Compose Your Message.
4. Upload CSV File.
5. Send SMS Messages.
