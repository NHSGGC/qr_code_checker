# If modifying these scopes, delete the file token.pickle.
SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/gmail.send'
]

EMAIL_BODY = """\
<html>
  <head></head>
  <body>
    <p>
        Hi,<br>
        The following links are currently not working:<br>
    </p>
    <ul>
    {}
    </ul>
    <br>
    <p>
        Best,<br>
        <br>
        Will
    </p>
  </body>
</html>
"""

EMAIL_SUBJECT = "QR Code links failing"
# EMAIL_TO = "Alison.Cairns@glasgow.ac.uk"
EMAIL_TO = "wahhill@gmail.com"
EMAIL_BCC = ['wahhill@gmail.com', 'frances.oleary@hotmail.co.uk']
