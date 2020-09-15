import smtplib as s
ob=s.SMTP("smtp.gmail.com",587)
ob.starttls()
ob.login("your mail id","your password")
subject="Sending email using python"
body="this message is sent to you via python!,i hope u r doing well and staying safe\n""good luck"
message="Subject:{}\n\n{}".format(subject,body)
# print(message)
listofadd=["your recipient",'your recipient','your recipient',]

ob.sendmail("your mail id",listofadd,message)
print("message send successfully")

quit()
