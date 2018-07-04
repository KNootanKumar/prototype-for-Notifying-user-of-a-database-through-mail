import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sqlite3
import time

video = []

def new_video():
    l=0
    m=0
    k=0
    email_to = ""
    body=""

    #connecting to the database for subcribers mail id's
    conn =sqlite3.connect("Youtube_sub_mail.db")
    mail=conn.cursor()
    mail.execute("SELECT *FROM youtube_subscibers")
    #fetching details of all current users
    current_users=mail.fetchall()
    print(current_users)


    conn1 =sqlite3.connect("Youtube_videos.db")
    videolist=conn1.cursor()
    videolist.execute("SELECT *FROM youtube_videos")
    #fetching details of all videos
    current_videos=videolist.fetchall()
    print(current_videos)
    conn.commit()
    conn1.commit()
    conn.close()
    conn1.close()

    print("length of video" + str(len(video)))
    body=''
    if len(current_videos)!=0:
        if len(video)==0:
            print("length of video" + str(len(video)))
            print("video is empty")
            video=current_videos
            for c in current_videos:
                print("in if for loop")
                if len(body)==0:
                    body='Thank You for subscribing our channel here are our videos'
                    body = body + '\n' + 'tittle: ' + c[1] + '\n' + 'Url: ' +c[2]
                else :
                    body = body + "\n" + "tittle: " + c[1] + "\n" + "Url: " +c[2]
            k=1
            print("1" + body)
        elif video[-1]==current_videos[-1]:
            video = current_videos
            print("No new videos")
        else:
            print("video is not empty")
            l=0
            k=1
            for a in reversed(video):
                if l==0:
                    m=0
                    for b in reversed(current_videos):
                        if l==0:
                            if a!=b:
                                m=m+1
                            else:
                                l=l+1
            videos = current_videos
            for a in current_videos[m:]:
                print("in else for loop")
                if len(body)==0:
                    body='Thank You for subscribing our channel here are our videos'
                    body = body + '\n' + 'tittle: ' + a[1] + '\n' + 'Url: ' +a[2]
                else :
                    body = body + "\n" + "tittle: " + a[1] + "\n" + "Url: " +a[2]
            print(body)

    if k==1 and len(body)!=0:
        print("in if")
        msg = MIMEMultipart()
        msg["From"]="k.nootankumar1998@gmail.com"

        for a in current_users:
                if len(email_to)==0:
                    email_to=a[2]
                else :
                    email_to=email_to+',' + a[2]

        msg["To"]=email_to
        msg.attach(MIMEText(body,"plain"))
        text = msg.as_string()
        mail = smtplib.SMTP("smtp.gmail.com",587) #smtp server for google and prots are 578 or 465
        mail.ehlo()
        mail.starttls()#start encryption
        mail.login("k.nootankumar1998@gmail.com","Ganiroja@2")#username and password should be entered
        mail.sendmail("k.nootankumar1998@gmail.com",msg["To"].split(","),text)
        mail.close()
