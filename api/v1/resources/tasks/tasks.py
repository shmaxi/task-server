import logging

from flask import request
from flask_restx import Resource, Namespace

from api.v1.models.tasks import Task
from api.v1.modules.authorization import login_required

ns = Namespace('tasks', description='Namespace for task management')
log = logging.getLogger(__name__)
TASKS_DAL = Task()


class Tasks(Resource):
    @ns.doc()
    @login_required
    def get(self, **kwargs):
        try:
            all_tasks = TASKS_DAL.get_all_tasks()
            if all_tasks:
                return all_tasks, 200
        except Exception as e:
            log.exception(e)
            return "Could not fetch tasks. Please try again later.", 500

        return "No tasks were found", 404

    @ns.doc()
    @login_required
    def post(self, **kwargs):
        try:
            json_content = request.json

            if json_content is None:
                return "Please specify task data in json format", 400
            else:
                task_data = json_content

            new_task_id = TASKS_DAL.create_task(task_data)
            return new_task_id, 201
        except Exception as e:
            log.exception(e)
            return "Could not create task. Please try again later.", 500

