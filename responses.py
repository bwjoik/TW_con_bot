from random import choice , randint
from dotenv import  set_key
from C_crawler_ver2 import get_new_judgment,J_URL_compare,get_text
import os
def get_response(user_input:str) -> str:

    lowered: str = user_input.lower()

    if lowered == '':
        return 'You need to say something'
    
    elif   "newcj" in lowered:
        new_CJ_url = J_URL_compare()
        return new_CJ_url
    else:
        #do nothing

        pass


