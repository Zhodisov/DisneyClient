



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




from collections import defaultdict

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy.orm import load_only
from sqlalchemy.sql import func
from datetime import datetime, timedelta
from functools import wraps
from typing import Any, ByteString, Dict, List, Optional, Union
from utils import cryptjson
Base = declarative_base()
from data.config import Config
from data.map import Map
from data.mariadbutils import json_length
from data.soft import Soft
from data.user import User
import sqlalchemy
import sqlalchemy.orm
import os

MutableDict.associate_with(sqlalchemy.JSON)

date_format = "%Y-%m-%d %H:%M:%S"

class EventSystem:
    def __init__(self):
        self.subscribers = defaultdict(list)

    def subscribe(self, event_name, callback):
        self.subscribers[event_name].append(callback)

    def notify(self, event_name, data=None):
        for callback in self.subscribers[event_name]:
            callback(data)

class DBClient:
	def __init__(self, endpoint: str):
		self.event_system = EventSystem()

	def __init__(self, endpoint: str):
		engine = sqlalchemy.create_engine(endpoint, pool_pre_ping=True, pool_recycle=3600)
		# Base.metadata.create_all(engine)
		# self.add_column(engine, "users", sqlalchemy.Column("unknown_device_block", sqlalchemy.Boolean, default=bool(True)))

		Session = sqlalchemy.orm.sessionmaker(engine)
		self._session: sqlalchemy.orm.session.Session = Session()

		def commit(cls, func):
			@wraps(func)
			def wrapper(*args, **kwargs):
				result = func(*args, **kwargs)

				cls._session.commit()

				return result
			return wrapper

		for name in dir(self):
			obj = getattr(self, name)
			if callable(obj) and (name.startswith("del_") or name.startswith("set_")):
				setattr(self, name, commit(self, obj))

	def execute_with_reconnection(self, operation, *args, **kwargs):
		for _ in range(3):  # Trying up to 3 times.
			try:
				return operation(*args, **kwargs)
			except sqlalchemy.exc.OperationalError:
				# Handle the disconnection error by recreating the session.
				self._session = self.Session()

		# If we've tried 3 times and still have the error, raise it.
		raise

		self.del_unmodified()

	def get_date_diff(self, date: str) -> timedelta:
		if isinstance(date, str):
			date = datetime.strptime(date, date_format)
		return datetime.now() - date

	def add_column(self, engine, table_name, column):
		column_name = column.compile(dialect=engine.dialect)
		column_type = column.type.compile(engine.dialect)
		engine.execute("ALTER TABLE %s ADD COLUMN %s %s" % (table_name, column_name, column_type))

	def alter_column(self, engine, table_name, column):
		column_name = column.compile(dialect=engine.dialect)
		column_type = column.type.compile(engine.dialect)
		engine.execute("ALTER TABLE %s MODIFY COLUMN %s %s" % (table_name, column_name, column_type))

	def del_column(self, table, column_name):
		columns = table.columns
		result = [c for c in columns if c.name == column_name]
		if result:
			columns.remove(result[0])
		else:
			print(f"Column {column_name} doest not exist")

	def del_unmodified(self):
		for user in self._session.query(User).options(load_only(User.key, User.last_login)).all():
			if self.get_date_diff(user.last_login).days >= 60:
				if (_map := self.find_map_by_key(user.key, True)) is not None:
					self.delete(_map)

	def add(self, obj: Any):
		self.self.event_system.notify('data_added', obj)
		self._session.add(obj)

	def commit(self):
		try:
			self._session.commit()
		except Exception as e:
			self._session.rollback()
			raise e


	def delete(self, obj: Any):
		self.self.event_system.notify('data_deleted', obj)
		self._session.delete(obj)

	def find_config_by_key(self, key: str) -> Config:
		return self._session.query(Config).get(key)

	def find_map_by_key(self, key: str, check_exists: Optional[bool] = False) -> Map:
		if check_exists:
			return self._session.query(Map).options(load_only(Map.key)).get(key)
		return self._session.query(Map).get(key)

	def find_soft_by_key(self, key: str, check_exists: Optional[bool] = False) -> Soft:
		if check_exists:
			return self._session.query(Soft).options(load_only(Soft.key)).get(key)
		return self._session.query(Soft).get(key)

	def find_user_by_key(self, key: str, check_exists: Optional[bool] = False) -> User:
		if check_exists:
			return self._session.query(User).options(load_only(User.key)).get(key)
		return self._session.query(User).get(key)

	def load_maps(self, only_keys: Optional[bool] = False) -> List:
		if only_keys:
			return self._session.query(Map).options(load_only(Map.key)).all()
		return self._session.query(Map).all()

	def load_soft(self, more_than: Optional[int] = None, only_keys: Optional[bool] = False) -> List:
		if only_keys:
			return self._session.query(Soft).options(load_only(Soft.key)).all()
		return self._session.query(Soft).all()

	def load_users(self, only_keys: Optional[bool] = False) -> List[User]:
		if only_keys:
			return self._session.query(User).options(load_only(User.key)).all()
		return self._session.query(User).all()

	def del_user(self, key: str) -> bool:
		user = self.find_user_by_key(key)
		if user:
			self.delete(user)
			return True
		return False

	def set_config(self, key: str, tfm_menu: Dict) -> Config:
		config = self.find_config_by_key(key)
		if config:
			config.tfm_menu = tfm_menu
		else:
			config = Config(key=key, tfm_menu=tfm_menu)
			self.add(config)

		return config

	def set_map(self, key: str, data: ByteString) -> Map:
		_map = self.find_map_by_key(key)
		if _map:
			_map.data = data
		else:
			_map = Map(key=key, data=data)
			self.add(_map)

		return _map

	def set_soft(self, key: str, data: Optional[ByteString] = b"") -> Soft:
		soft = self.find_soft_by_key(key)
		if soft:
			if not soft.data:
				soft.data = data
			else:
				maps = cryptjson.json_unzip(data)
				soft_maps = cryptjson.json_unzip(soft.data)
				for code, info in maps.items():
					self.self.event_system.notify('data_set', key)
					if code.startswith("@") and bool(info):
						soft_maps[code] = info
					else:
						if code in soft_maps.keys():
							del soft_maps[code]
				soft.data = cryptjson.json_zip(soft_maps)
		else:
			soft = Soft(key=key, data=data)
			self.add(soft)

		return soft

	def set_user(self, key: str, level: Optional[str] = "GOLD_II", browser_access: Optional[bool] = True) -> User:
		level = level.upper()

		user = self.find_user_by_key(key)
		if user:
			user.level = level
			user.browser_access = browser_access
		else:
			user = User(key=key, level=level, browser_access=browser_access)
			self.add(user)

		return user

	def set_user_browser_token(self, key: str, token: Optional[str] = None) -> User:
		user = self.find_user_by_key(key)
		if user:
			user.update(browser_access=True, browser_access_token=token)
		return user

	def set_flash_token(self, key: str, token: Optional[str] = None) -> User:
		user = self.find_user_by_key(key)
		if user:
			user.update(flash_token=token)
		return user

client = DBClient(os.getenv("MARIADB_ENDPOINT"))

def execute_with_reconnection(self, operation, *args, **kwargs):
    MAX_RETRIES = 3
    for _ in range(MAX_RETRIES):
        try:
            result = operation(*args, **kwargs)
            return result
        except sqlalchemy.exc.OperationalError:
            self._session.rollback()
            self.reconnect()
    raise Exception("Failed to execute operation after multiple retries.")

def reconnect(self):
    self._session.close()
    self._session = self.Session()




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



