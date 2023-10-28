



#                https://safemarket.xyz | https://safemarket.xyz/discord
#__| |_____________________________________________________________________________| |__
#__   _____________________________________________________________________________   __
#  | |                                                                             | |  
#  | | ____     _     _____  _____      __  __     _     ____   _  __ _____  _____ | |  
#  | |/ ___|   / \   |  ___|| ____|    |  \/  |   / \   |  _ \ | |/ /| ____||_   _|| |  
#  | |\___ \  / _ \  | |_   |  _|      | |\/| |  / _ \  | |_) || ' / |  _|    | |  | |  
#  | | ___) |/ ___ \ |  _|  | |___     | |  | | / ___ \ |  _ < | . \ | |___   | |  | |  
#  | ||____//_/   \_\|_|    |_____|    |_|  |_|/_/   \_\|_| \_\|_|\_\|_____|  |_|  | |  
#__| |_____________________________________________________________________________| |__
#__   _____________________________________________________________________________   __
#  | |                                                                             | |  
#                               https://github.com/Jodis974                           



from sqlalchemy.sql import func

from data import Base

import sqlalchemy

class User(Base):
    __tablename__ = "users"

    key =  sqlalchemy.Column(sqlalchemy.String(16), primary_key=True)
    level = sqlalchemy.Column(sqlalchemy.String(10), default=str("GOLD_II"))

    last_login = sqlalchemy.Column(sqlalchemy.TIMESTAMP, server_default=func.now())

    browser_access = sqlalchemy.Column(sqlalchemy.Boolean, default=bool(True))
    browser_access_token = sqlalchemy.Column(sqlalchemy.String(40))

    flash_token = sqlalchemy.Column(sqlalchemy.String(32))

    key_hidden = sqlalchemy.Column(sqlalchemy.Boolean, default=bool(False))

    connection_limit = sqlalchemy.Column(sqlalchemy.Integer, default=(int(2)))

    unknown_device_block = sqlalchemy.Column(sqlalchemy.Boolean, default=bool(True))



#                https://safemarket.xyz | https://safemarket.xyz/discord
#__| |_____________________________________________________________________________| |__
#__   _____________________________________________________________________________   __
#  | |                                                                             | |  
#  | | ____     _     _____  _____      __  __     _     ____   _  __ _____  _____ | |  
#  | |/ ___|   / \   |  ___|| ____|    |  \/  |   / \   |  _ \ | |/ /| ____||_   _|| |  
#  | |\___ \  / _ \  | |_   |  _|      | |\/| |  / _ \  | |_) || ' / |  _|    | |  | |  
#  | | ___) |/ ___ \ |  _|  | |___     | |  | | / ___ \ |  _ < | . \ | |___   | |  | |  
#  | ||____//_/   \_\|_|    |_____|    |_|  |_|/_/   \_\|_| \_\|_|\_\|_____|  |_|  | |  
#__| |_____________________________________________________________________________| |__
#__   _____________________________________________________________________________   __
#  | |                                                                             | |  
#                               https://github.com/Jodis974                           



