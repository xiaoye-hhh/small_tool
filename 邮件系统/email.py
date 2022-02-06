import smtplib
from email.mime.text import MIMEText

def send_email(from_addr, to_addr, passwd, subject, content):
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr

    s = smtplib.SMTP_SSL("smtp.qq.com", 465)
    s.login(from_addr, passwd)
    s.sendmail(from_addr, to_addr, msg.as_string())
    s.quit()


if __name__ == '__main__':
    send_email('3102406698@qq.com', '1318137184@qq.com', 'bbgrbchpzygsddia', 'from python', 'have a good night!')