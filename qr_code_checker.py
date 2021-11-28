import base64
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json

from googleapiclient.discovery import build
import httpx

from auth import authenticate_google_credentials
from settings import EMAIL_BODY, EMAIL_SUBJECT, EMAIL_TO, EMAIL_BCC


def send_email(creds, body):
    email = MIMEMultipart()
    email['To'] = EMAIL_TO
    email['Bcc'] = ", ".join(EMAIL_BCC)
    email['Subject'] = EMAIL_SUBJECT
    body = MIMEText(body, 'html')
    email.attach(body)

    text = {'raw': base64.urlsafe_b64encode(email.as_bytes()).decode()}

    # Call the Gmail API
    service = build('gmail', 'v1', credentials=creds)
    message = (service.users().messages().send(userId="me", body=text)
               .execute())
    print('Message Id: %s' % message['id'])
    return message


if __name__ == "__main__":
    timestamp = datetime.datetime.now().ctime()
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:70.0) Gecko/20100101 Firefox/70.0'}
        with open("sites.json", 'r') as f:
            data = json.load(f)
            out = ''
            for category, urls in data.items():
                for url in urls:
                    print(url)
                    resp = httpx.get(url, headers=headers, timeout=60)
                    if resp.status_code != 200:
                        out += "<li><b>{}</b>: {} (status {})</li>".format(category, url, resp.status_code)
        if out:
            creds = authenticate_google_credentials()
            body = EMAIL_BODY.format(out)
            send_email(creds, body)
            with open("qr_checks.txt", 'w') as f:
                f.write(timestamp)
    except Exception as e:
        with open("qr_errors.txt", 'w') as f:
            f.write("{}: {}".format(timestamp, e))
