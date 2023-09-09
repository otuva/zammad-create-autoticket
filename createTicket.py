from zammad_py import ZammadAPI

# Initialize the client with the URL, username, and password
# Note the Host URL should be in this format: 'https://zammad.example.org/api/v1/'
client = ZammadAPI(url='https://<HOST>/api/v1/', username='bot', password="<PASS>")

# disable ssl check
client.session.verify = False

# Create a ticket
params = {
   "title": "AUTOMATED TITLE",
   "group": "Users",
   "customer": "bot",
   "article": {
      "body": "This ticket is created by a bot",
      "type": "note",
      "internal": False
   }
}

new_ticket = client.ticket.create(params=params)
