import requests
import datetime
import smtplib
import ssl
import os
import json
import time

period = 10  # in seconds
pincode = "000000"
date = datetime.date.today().strftime("%d-%m-%Y")
url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin"

sender_email = "<sender>@gmail.com"
receiver_email = [
    "<receiver1>@gmail.com",
    "<receiver2>@gmail.com",
    "<receiver3>@gmail.com"
    # You can add more
]
password = os.environ['MAIL_PASSWORD']

while True:
    response = requests.get(url, {
        "pincode": pincode,
        "date": date
    }, headers={
        "accept": "application/json",
        "accept-language": "en-US",
        "user-agent": "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51"
    })

    centers = response.json().get('centers')
    results = []

    for center in centers:
        name = center.get('name')
        for session in center.get('sessions'):
            if session.get('min_age_limit') < 45 and \
                    session.get('available_capacity') > 0:
                result = {
                    "name": center.get('name'),
                    "date": session.get('date'),
                    "available_capacity": session.get("available_capacity"),
                    "vaccine": session.get("vaccine"),
                    "min_age": session.get("min_age_limit")
                }
                results.append(result)

    if len(results) > 0:
        print("Slots available")
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        results_str = json.dumps(results, indent=2)
        message = "Subject: Vaccine slot available. Hurry!\n\n" +\
            results_str +\
            "\n\nStay safe :)"

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)

    time.sleep(period)

