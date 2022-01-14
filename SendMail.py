#! /usr/bin/python3
import smtplib

def sentmail():
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print('Email sent!')


gmail_user = 'xxx@gmail.com'
gmail_password = 'pasword'

sent_from = gmail_user
to = ['yyy@gmail.com']
subject = 'YOUR BAG IS AVAILABLE!!'
body = 'GO GET IT NOW!!! Link: https://m.en.mlb-korea.com/product/monogram-hobo-bag-new-york-yankees/2449/'
# body = test.body
email_text = """\
From: %s
To: %s
Subject: %s
%s 
""" % (sent_from, ", ".join(to), subject, body)

if __name__ == "__main__":
    sentmail()
