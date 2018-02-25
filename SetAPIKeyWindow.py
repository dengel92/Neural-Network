import pyforms
from pyforms import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlButton


class SetAPIKeyWindow(BaseWidget):

    def __init__(self):
        BaseWidget.__init__(self, 'API Key')

        self.__APIKeyField = ControlText('API Key')
        self.__saveKey     = ControlButton('Save')

        self.__saveKey.value = self.__SaveKey
    def __SaveKey(self):
        APIKey.api_keys = self.__APIKeyField.value
        print(APIKey.api_keys)
        self.close()
class APIKey(object):
    def __init__(self, api_key):
        self.api_keys = api_key

if __name__ == "__main__": pyforms.start_app(SetAPIKeyWindow)