# hangouts_bot
Hangouts bot to automate attendance.  
Students can sleep through their early morning online lectures, while this python bot automatically logs them in and sends "Present" to record their attendance. 

to run:

  - download chromedriver, unzip, move to /usr/local/bin (mac os / linux)
  - pip install selenium
  - create a secrets.py file with variables:

email = "your_email"  
password = "your_password"  
send_to = "receivers_email"  
message = "Present"
