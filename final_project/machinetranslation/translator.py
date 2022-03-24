'''New module'''
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
VERSION= '2018-05-01'
AUTHENTICATOR = IAMAuthenticator(apikey)

language_translator = LanguageTranslatorV3(
    version= VERSION, authenticator=AUTHENTICATOR
)

language_translator.set_service_url(url)
language_translator.set_disable_ssl_verification(False)


def english_to_french(english_text):
    '''En - Fr '''
    
    if english_text is None:
        return ''

    french = language_translator.translate(text=english_text,model_id='en-fr')
    translation = french.get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    '''Fr - En '''
    
    if french_text is None:
        return ''
    
    english = language_translator.translate(text=french_text,model_id='fr-en')
    translation = english.get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
