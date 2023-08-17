#modules
import imaplib
import email

#credentials
username ="manipulation.12347@gmail.com" #"tunah3412@gmail.com"

#generated app password
app_password="aqbrxtbinbkqiwku" #"jajdbrlgyzmeahqj"

# https://www.systoolsgroup.com/imap/
gmail_host= 'imap.gmail.com'


#set connection
mail = imaplib.IMAP4_SSL(gmail_host)

#login
mail.login(username, app_password)


#select inbox
mails = mail.select("INBOX")

selected_mails = mail.search(None,"UNSEEN")
for mm in selected_mails:
    typ, data = mail.fetch(b"1", '(RFC822)')

# Parse the email
msg = email.message_from_bytes(data[0][1])
print(msg['From'], ":", msg['Subject'])

