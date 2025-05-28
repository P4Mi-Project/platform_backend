import dotenv
import os
import requests

dotenv.load_dotenv()

class EmailService:
    def __init__(self):
        self.api_key = os.environ["mail_gun_api"]
    def send_mentor_user_message_notification(self,name,sender_name,body) -> bool:
        try:
            requests.post(
            "https://api.mailgun.net/v3/sandbox86a3ad1769e043478133e037653d303a.mailgun.org/messages",
            auth=("api", self.api_key),
            data={"from": "Mailgun Sandbox <postmaster@sandbox86a3ad1769e043478133e037653d303a.mailgun.org>",
                "to": f"{name} <msmasud578@gmail.com>",
                "subject": f"You got a new message from : {sender_name}",
                "text": body,
            
                })
            return True
        except:
            import traceback; traceback.print_exc()
            return False
        
# if __name__ == "__main__":
#     email_service = EmailService()
#     email_service.send_message()