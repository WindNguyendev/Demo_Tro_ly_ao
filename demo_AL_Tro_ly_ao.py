import os
import playsound
import speech_recognition as sr
import time
import sys
import ctypes
import wikipedia
import datetime
import json
import re
import webbrowser
import smtplib
import requests
import urllib
import urllib.request as urllib2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import strftime
from gtts import gTTS
from youtube_search import YoutubeSearch

wikipedia.set_lang('vi')
language = 'vi'
path = ChromeDriverManager().install()

def speak(text):
    print("Bot: {}".format(text))
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("sound.mp3")
    playsound.playsound("sound.mp3", False)
    os.remove('sound.mp3')


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Tôi: ", end='')
        audio = r.listen(source, phrase_time_limit=5)
        try:
            text = r.recognize_google(audio, language="vi-VN")
            print(text)
            return text
        except:
            print("...")
            return 0

def stop():
    speak("Hẹn gặp lại bạn sau!")

def get_text():
    for i in range(3):
        text = get_audio()
        if text:
            return text.lower()
        elif i < 2:
            speak("Bot không nghe rõ. Bạn nói lại được không!")
    time.sleep(2)
    stop()
    return 0


def hello(name):
    day_time = int(strftime('%H'))
    if day_time < 12:
        speak("Chào buổi sáng bạn {}. Chúc bạn một ngày tốt lành.".format(name))
    elif 12 <= day_time < 18:
        speak("Chào buổi chiều bạn {}. Bạn đã dự định gì cho chiều nay chưa.".format(name))
    else:
        speak("Chào buổi tối bạn {}. Bạn đã ăn tối chưa nhỉ.".format(name))


def get_time(text):
    now = datetime.datetime.now()
    if "giờ" in text:
        speak('Bây giờ là %d giờ %d phút' % (now.hour, now.minute))
    elif "ngày" in text:
        speak("Hôm nay là ngày %d tháng %d năm %d" %
              (now.day, now.month, now.year))
    else:
        speak("Bot chưa hiểu ý của bạn. Bạn nói lại được không?")

def open_application(text):
    if "google" in text:
        speak("Mở Google Chrome")
        os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe')
    elif "word" in text:
        speak("Mở Microsoft Word")
        os.startfile('C:\Program Files\Microsoft Office\\root\Office16\\WINWORD.EXE')
    elif "excel" in text:
        speak("Mở Microsoft Excel")
        os.startfile('C:\Program Files\Microsoft Office\\root\Office16\EXCEL.EXE')
    else:
        speak("Ứng dụng chưa được cài đặt. Bạn hãy thử lại!")


def open_website(text):
    reg_ex = re.search('mở (.+)', text)
    if reg_ex:
        domain = reg_ex.group(1)
        url = 'https://www.' + domain
        webbrowser.open(url)
        speak("Trang web bạn yêu cầu đã được mở.")
        return True
    else:
        return False

def open_google_and_search(text):
    search_for = text.split("kiếm", 1)[1]
    speak('Okay!')
    A = "+".join(search_for.split())
    B = "https://www.google.com/search?q="
    url = B+A
    webbrowser.open_new(url)

def smtplid_sendEmail(content,from_email):
    import smtplib
    import ssl
    from email.message import EmailMessage

        # Define email sender and receiver
    email_sender = 'pn2012001@gmail.com'
    email_password = 'dwyt kgmo yizj thln'
    email_receiver = from_email

        # Set the subject and body of the email
    subject = 'Test trợ lý ảo'
    body = content
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

        # Add SSL (layer of security)

        # Log in and send the email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())


def send_email(text):
    speak('Bạn gửi email cho ai nhỉ')
    recipient = get_text()
    if 'yến' in recipient:
        speak('Nội dung bạn muốn gửi là gì')
        content = get_text()
        from_email = 'laplalaplon111@gmail.com'

        smtplid_sendEmail(content,from_email)

        speak('Email của bạn vùa được gửi! Vui lòng kiểm tra lại Email')
    elif 'chồng' in recipient:
        speak('Nội dung bạn muốn gửi là gì')
        content = get_text()
        from_email = 'lennguyn999@gmail.com'
        smtplid_sendEmail(content,from_email)

        speak('Email của bạn vùa được gửi! Vui lòng kiểm tra lại Email')

    else:
        speak('Bot không hiểu bạn muốn gửi email cho ai. Bạn nói lại được không?')


def play_song():
    speak('Xin mời bạn chọn tên bài hát')
    mysong = get_text()

    from youtubesearchpython import VideosSearch
    videosSearch = VideosSearch(mysong, limit = 2)
    A = videosSearch.result()
    webbrowser.open_new("https://www.youtube.com/watch?v="+A["result"][0]["id"])
    speak('Bài hát đã được mở')



def assistant():
    speak("Xin chào, bạn tên là gì nhỉ?")
    name = get_text()
    if name:
        speak("Chào bạn {}".format(name))
        speak("Bạn cần Bot Alex có thể giúp gì ạ?")
        while True:
            text = get_text()
            if not text:
                break
            elif "dừng" in text or "tạm biệt" in text or "chào robot" in text or "ngủ thôi" in text:
                stop()
                break
            elif "có thể làm gì" in text:
                help_me()
            elif "chào trợ lý ảo" in text:
                hello(name)
            elif "hiện tại" in text:
                get_time(text)
            elif "mở" in text:
                if 'mở google và tìm kiếm' in text:
                    open_google_and_search(text)
                elif "." in text:
                    open_website(text)
                else:
                    open_application(text)
            elif "email" in text or "mail" in text or "gmail" in text:
                send_email(text)
            elif "thời tiết" in text:
                current_weather()
            elif "chơi nhạc" in text:
                play_song()
            elif "hình nền" in text:
                change_wallpaper()
            elif "đọc báo" in text:
                read_news()
            elif "định nghĩa" in text:
                tell_me_about()
            else:
                speak("Bạn cần Bot giúp gì ạ?")

assistant()