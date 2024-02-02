import smtplib
my_email = "ayushkumar@gmail.com"
password = "123456"

connection = smtplib.SMTP("smpt.gmail.com",587)
connection.starttls()
connection.login(user = my_email,password=password)

connection.sendmail(from_addr=my_email,to_addrs="recieptemail@gmail.com",msg = "Hello world")

connection.close()