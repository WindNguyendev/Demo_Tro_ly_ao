# import smtplib
# import ssl
# from email.message import EmailMessage

# # Define email sender and receiver
# email_sender = 'pn2012001@gmail.com'
# email_password = 'dwyt kgmo yizj thln'
# email_receiver = 'laplalaplon111@gmail.com'

# # Set the subject and body of the email
# subject = 'Check out my new video!'
# body = """
# Xin chào! dạo này có khỏe không
# """
# em = EmailMessage()
# em['From'] = email_sender
# em['To'] = email_receiver
# em['Subject'] = subject
# em.set_content(body)

# # Add SSL (layer of security)
# context = ssl.create_default_context()

# # Log in and send the email
# with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
#     smtp.login(email_sender, email_password)
#     smtp.sendmail(email_sender, email_receiver, em.as_string())


from bs4 import BeautifulSoup
import requests


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

def find_weather(city_name):
   city_name = city_name.replace(" ", "+")
   print(city_name)
 
   try:
       res = requests.get(
           f'https://www.google.com/search?q=h%C3%A0+n%E1%BB%99i+weather&sca_esv=c27c31a5ed104b1d&rlz=1C1KNTJ_viVN1064VN1064&biw=1536&bih=738&sxsrf=ACQVn08wGOnFDi9PiBejbJvg6nHReAr4TA%3A1710993671050&ei=B7H7ZafVAtSA2roP8oeisAM&udm=&oq=h%C3%A0+n%E1%BB%99i+we&gs_lp=Egxnd3Mtd2l6LXNlcnAiDGjDoCBu4buZaSB3ZSoCCAAyBRAAGIAEMg4QLhiABBjHARivARiOBTIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeMgYQABgWGB5IlClQkgtYqCFwCHgBkAEGmAF5oAGvDaoBBDEyLja4AQPIAQD4AQH4AQKYAhSgAsgJwgIKEAAYRxjWBBiwA8ICDRAAGIAEGIoFGEMYsAPCAgoQIxiABBiKBRgnwgIMECMYgAQYigUYExgnwgIKEC4YgAQYigUYQ8ICDhAuGIAEGIoFGLEDGIMBwgIQEC4YgAQYigUYsQMYgwEYCsICCxAAGIAEGLEDGIMBwgIQEC4YgAQYigUYQxjHARivAcICChAAGIAEGIoFGEPCAg0QLhiABBiKBRhDGLEDwgIFEC4YgATCAggQLhiABBixA8ICBBAAGAPCAgcQABiABBgKwgIIEAAYgAQYywHCAgoQLhiABBjUAhgKwgILEC4YgAQYsQMYgwHCAgcQLhiABBgKwgIQEC4YgAQYChjHARivARiOBcICFBAuGIAEGJcFGNwEGN4EGOAE2AEBmAMAiAYBkAYKugYGCAEQARgUkgcEMTUuNaAHsMQB&sclient=gws-wiz-serp', headers=headers)
      
       print("Loading...")
 
       soup = BeautifulSoup(res.text, 'html.parser')
       location = soup.select('#wob_loc')[0].getText().strip()
       time = soup.select('#wob_dts')[0].getText().strip()
       info = soup.select('#wob_dc')[0].getText().strip()
       temperature = soup.select('#wob_tm')[0].getText().strip()
 
       print("Location: " + location)
       print("Temperature: " + temperature + "°C")
       print("Time: " + time)
       print("Weather Description: " + info)
   except:
       print("Please enter a valid city name")


city_name = input("Enter City Name: ")
city_name = city_name + " weather"
find_weather(city_name)