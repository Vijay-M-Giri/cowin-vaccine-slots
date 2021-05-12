# Cowin vaccine slots alert

Sends email alerts when the vaccine slots are available.

[API](https://apisetu.gov.in/public/marketplace/api/cowin/)
**Please note that the slot data might be up to 30 minutes old. This is a limitation in Cowin API**

## Steps

- One sender email address and password is required
- If you are using Gmail address then get 'app password'. Follow the steps [here](https://support.google.com/accounts/answer/185833?hl=en). For others, the password of the email account may suffice.
- Set the above password as environment variable
  - `$> MAIL_PASSWORD=<your password>`
  - `$> export MAIL_PASSWORD`
- Set `sender_email`, `receiver_email`, `pincode` in `slots.py`
- Set `period` in `slots.py`. Note that the period should be **more than 5 secs.** (Limitation in Cowin API)
- Run the script
  - `$> nohup python3 slots.py &`

