import json

from uuid import uuid4

from api.v1 import CURRENT_CONFIG
from utils.redis_helper import RedisHelper


class Task:
    def __init__(self):
        self.redis_connection = RedisHelper(
            CURRENT_CONFIG.REDIS_HOST,
            CURRENT_CONFIG.REDIS_PORT
        )

    def create_task(self, task_details):
        new_task_id = str(uuid4())
        self.redis_connection.set_key(new_task_id, json.dumps(task_details))
        return new_task_id

    def get_all_tasks(self):
        return {
            key.decode(): json.loads(value)
            for key, value in self.redis_connection.get_all().items()
        }

    def get_task_details(self, task_id):
        if self.redis_connection.does_key_exist(task_id):
            return json.loads(self.redis_connection.get_key(task_id))

        return None

    def update_task(self, task_id, task_details):
        if task_details:
            self.redis_connection.set_key(task_id, json.dumps(task_details))

    def delete_task(self, task_id):
        self.redis_connection.delete_key(task_id)

