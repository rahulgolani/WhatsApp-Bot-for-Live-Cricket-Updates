import requests
import json
import pprint
from datetime import datetime
class Score:

    def __init__(self):
        '''Initializing all the required endpoints '''
        self.getAllMatches="http://cricapi.com/api/matches/"
        self.getScore="http://cricapi.com/api/cricketScore"
        self.apiKey="Your ApiKey"
        self.uniqueId=""

    def getUniqueId(self):
        uriParams={"apikey":self.apiKey}
        resp=requests.get(self.getAllMatches,params=uriParams)
        respDict=resp.json()
        uIdFound=0
        #pprint.pprint(respDict)
        for i in respDict['matches']:
            if (i['team-1']=='Australia' or i['team-2']=='Australia' and i['matchStarted']):
                #todaysDate=datetime.today().strftime('%Y-%m-%d')
                '''
                if todaysDate==i['date'].split('T')[0]:
                    self.uniqueId=i['unique_id']
                '''
                self.uniqueId=i['unique_id']
                uIdFound=1
                break
        if uIdFound==0:
            self.uniqueId=-1
            print('No Matches Today')
            return

        #print(self.uniqueId)
        sendData=self.getScoreCurrent(self.uniqueId)
        return sendData

    def getScoreCurrent(self,uniqueId):
        data=""
        uriParams={"apikey":self.apiKey,"unique_id":uniqueId}
        resp=requests.get(self.getScore,params=uriParams)
        data_json=resp.json()
        #print(data_json)
        try:
            data="Here's the score: \n"+data_json["stat"]+'\n'+data_json['score']
        except KeyError as e:
            print(e)
        return data


if __name__ == '__main__':
    score=Score()
    updates=score.getUniqueId()
    from twilio.rest import Client
    a_sid="Your Account SID"
    auth_token="Your Account Auth Token"
    client=Client(a_sid,auth_token)
    message=client.messages.create(body=updates,from_='whatsapp:+14155238886',to='whatsapp:your whatsApp number')
