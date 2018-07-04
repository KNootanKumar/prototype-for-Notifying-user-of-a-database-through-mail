import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sqlite3
import time

class youtube:
    def __init__(self):
        self.user=[]
        self.video=[]

    def new_user(self):
        k=0
        i=0
        email_to = ""
        body=""

        print("length of user" + str(len(self.user)))
        if len(self.user)==0:
            print("length of user" + str(len(self.user)))
            print("user is empty")
            self.user=current_users
            k=1
            for a in current_users:
                if len(email_to)==0:
                    email_to=a[2]
                else :
                    email_to=email_to+',' + a[2]
        elif self.user[-1]==current_users[-1]:
            self.user = current_users
            print("No new user")
        else:
            print("user is not empty")
            j=0
            k=1
            for a in reversed(self.user):
                if j==0:
                    i=0
                    for b in reversed(current_users):
                        if j==0:
                            if a!=b:
                                i=i+1
                            else:
                                j=j+1
            self.user = current_users
            i=len(current_users)-i
            for a in current_users[i:]:
                if len(email_to)==0:
                    email_to=a[2]
                else :
                    email_to=email_to + "," + a[2]
        if k==1:
            msg = MIMEMultipart()
            msg["From"]=email #define email
            msg["To"]=email_to

            for c in current_videos:
                    if len(body)==0:
                        body='Thank You for subscribing our channel here are our videos'
                        body = body + '\n' + 'tittle: ' + c[1] + '\n' + 'Url: ' +c[2]
                    else :
                        body = body + "\n" + "tittle: " + c[1] + "\n" + "Url: " +c[2]

            msg.attach(MIMEText(body,"plain"))
            text = msg.as_string()
            mail = smtplib.SMTP("smtp.gmail.com",587) #smtp server for google and prots are 578 or 465
            mail.ehlo()
            mail.starttls()#start encryption
            mail.login(email,password)#username and password should be entered
            mail.sendmail(email,msg["To"].split(","),text)
            print("updates of videos are sent to new user sucessfully")
            mail.close()

    def new_video(self):
        l=0
        m=0
        k=0
        email_to = ""
        body=""
        print("length of video" + str(len(self.video)))
        body=''
        if len(current_videos)!=0:
            if len(self.video)==0:
                print("length of video" + str(len(self.video)))
                print("video is empty")
                self.video=current_videos
                for c in current_videos:
                    if len(body)==0:
                        body='Thank You for subscribing our channel here are our videos'
                        body = body + '\n' + 'tittle: ' + c[1] + '\n' + 'Url: ' +c[2]
                    else :
                        body = body + "\n" + "tittle: " + c[1] + "\n" + "Url: " +c[2]
                k=1
            elif self.video[-1]==current_videos[-1]:
                self.video = current_videos
                print("No new videos")
            else:
                print("video is not empty")
                l=0
                k=1
                for a in reversed(self.video):
                    if l==0:
                        m=0
                        for b in reversed(current_videos):
                            if l==0:
                                if a!=b:
                                    m=m+1
                                else:
                                    l=l+1
                self.video = current_videos
                m=len(current_videos)-m
                for a in current_videos[m:]:
                    if len(body)==0:
                        body='Thank You for subscribing our channel here are our videos'
                        body = body + '\n' + 'tittle: ' + a[1] + '\n' + 'Url: ' +a[2]
                    else :
                        body = body + "\n" + "tittle: " + a[1] + "\n" + "Url: " +a[2]

        if k==1 and len(body)!=0:
            print("in if")
            msg = MIMEMultipart()
            msg["From"]=email#define email

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
            mail.login(email,password)#username and password should be entered
            mail.sendmail(email,msg["To"].split(","),text)
            print("mail of new video sent sucessfully")
            mail.close()


h = youtube()

while(True):
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

    h.new_user()
    h.new_video()

    time.sleep(40)
