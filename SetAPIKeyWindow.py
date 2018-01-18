import pyforms
from pyforms import BaseWidget
from pyforms.Controls import ControlText
from pyforms.Controls import ControlButton
from SetAPIKey import APIKey

class SetAPIKeyWindow(APIKey, BaseWidget):

    def __init__(self):
        APIKey.__init__(self, '')
        BaseWidget.__init__(self, 'API Key')

        self.__APIKeyField = ControlText('API Key')
        self.__saveKey     = ControlButton('Save')

        self.__saveKey.value = self.__SaveKey
    def __SaveKey(self):
        APIKey.api_keys = self.__APIKeyField.value
        self.close()

if __name__ == "__main__": pyforms.start_app(SetAPIKeyWindow)