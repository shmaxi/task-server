from redis import Redis


class RedisHelper:
	def __init__(self, host: str, port: int):
		self.engine = Redis(host=host, port=port)

	def set_key(self, key: str, value: str, ttl: int = None):
		self.engine.set(key, value, ex=ttl)

	def get_key(self, key: str):
		return self.engine.get(key).decode()

	def does_key_exist(self, key: str) -> bool:
		return self.engine.exists(key)

	def get_all(self):
		all_key_values = {}
		for key in self.engine.scan_iter('*'):
			all_key_values[key] = self.engine.get(key).decode()

		return all_key_values

	def delete_key(self, key):
		self.engine.delete(key)

