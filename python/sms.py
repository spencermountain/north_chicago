import collections

from twilio.rest import TwilioRestClient
from sms_cfg import TW_CLIENT_ID, TW_SECRET_KEY, TW_APP_ID

RecievedText = collections.namedtuple("RecievedText", ["sender", "sid"])

class TwilioClient(object):
    CORP_FMT = '''Company: {:.2f}
Last price: {:.2f}
Ask: {:.2f}
Bid: {:.2f}'''
    COUNTRY_FMT = '''Country: {}
Population: {:.0f}
Unemployment rate: {:.3f}'''
    BASE_FMT = '''
    <?xml version="1.0" encoding="UTF-8"?>
    <Response>
    <Message>{}.</Message>
    </Response>
    '''

    REJ_FMT = BASE_FMT.format("Nothing recognized.")
    PRIV_FMT = BASE_FMT.format(
        "This company is not privately traded.")
    OUR_NUM = "+16466473401"


    def __init__(self,
                 tw_client_id=TW_CLIENT_ID,
                 tw_secret_key=TW_SECRET_KEY,
                 tw_app_id=TW_APP_ID):
        self.acc_sid = tw_app_id
        self.twilio = TwilioRestClient(tw_client_id, tw_secret_key)

    @staticmethod
    def _plusify(num):
        return ("+{}" if not "+" in num else "{}").format(num)

    def get_media(self, recvd):
        return self.twilio.media(recvd.sid)


    def _message(self, recvd, body):
        message = self.twilio.messages.create(
                    body=body,
            to=self._plusify(recvd.sender),
            from_=self.OUR_NUM)

        print "sent message: ", message

    def reject(self, recvd):
        self._message(recvd, self.REJ_FMT)

    def private(self, recvd):
        self._message(recvd, self.PRIV_FMT)

    def accept(self, recvd, info):
        print "trying to accept ", info
        self._message(recvd,
                      self.CORP_FMT.format(
                          info['security'],
                          info['PX_LAST'],
                          info['PX_ASK'],
                          info['PX_BID']))
    def country(self, recvd, best_match, info):
        self._message(recvd,
                      self.COUNTRY_FMT.format(
                          best_match,
                          info['WPOP'],
                          info['UNEMP']))
