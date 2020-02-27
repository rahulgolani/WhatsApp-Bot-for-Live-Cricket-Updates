from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from score import getMessage

app=Flask(__name__)

@app.route('/whatsapp',methods=['POST'])
def replyWithMessage():
    team_name=request.values.get('Body')
    print('Message Sent',team_name)
    message=getMessage(team_name)
    response=MessagingResponse()
    response.message(message)
    return str(response)

if __name__ == '__main__':
    app.run()
