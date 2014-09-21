import collections

from twilio.rest import TwilioRestClient
from sms_cfg import TW_CLIENT_ID, TW_SECRET_KEY, TW_APP_ID

RecievedText = collections.namedtuple("RecievedText", ["sender", "sid"])

class TwilioClient(object):
    CORP_FMT = '''Ticker: {}
    Ask: {}
    Bid: {}
    Volatility: {}'''
    BASE_FMT = '''
    <?xml version="1.0" encoding="UTF-8"?>
    <Response>
    <Message>{}.</Message>
    </Response>
    '''

    REJ_FMT = BASE_FMT.format("No object recognized.")
    OUR_NUM = "+16466473401"


    def __init__(self,
                 tw_client_id=TW_CLIENT_ID,
                 tw_secret_key=TW_SECRET_KEY,
                 tw_app_id=TW_APP_ID):
        self.acc_sid = tw_app_id
        self.twilio = TwilioRestClient(tw_client_id, tw_secret_key)


    def get_media(self, recvd):
        return self.twilio.media(recvd.sid)
