from flask_restx import Namespace

from api.v1.resources.tasks.task import Task
from api.v1.resources.tasks.tasks import Tasks

ns = Namespace('tasks', description='Namespace for task management')
ns.add_resource(Tasks, '')
ns.add_resource(Task, '/<task_id>')

