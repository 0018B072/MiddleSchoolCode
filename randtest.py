import smtplib

content = 'example email stuff here'
#426
mail = smtplib.SMTP('smtp.gmail.com',587)

mail.ehlo()

mail.starttls()

mail.login('S3oul.exe@gmail.com', 'Korea|s^he&e$t')

mail.sendmail('S3oul.exe@gmail.com','1oatbread@gmail.com', content)

mail.close()

