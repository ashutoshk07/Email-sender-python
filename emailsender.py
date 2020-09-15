import smtplib as s
ob=s.SMTP("smtp.gmail.com",587)
ob.starttls()
ob.login("ashu2000toshkumar@gmail.com","Madhav@143")
subject="Sending email using python"
body="this message is sent to you via python!,i hope u r doing well and staying safe\n""good luck"
message="Subject:{}\n\n{}".format(subject,body)
# print(message)
listofadd=["kumar143ashutosh@gmail.com",'nileshraj73@gmail.com','nb15905@gmail.com',]

ob.sendmail("ashu2000toshkumar@gmail.com",listofadd,message)
print("message send successfully")

quit()
