import logging

from flask import request
from flask_restx import Resource, Namespace

from api.v1.models.tasks import Task
from api.v1.modules.authorization import login_required

ns = Namespace('tasks', description='Namespace for task management')
log = logging.getLogger(__name__)
TASKS_DAL = Task()


class Task(Resource):
    @ns.doc()
    @login_required
    def get(self, task_id):
        try:
            task_data = TASKS_DAL.get_task_details(task_id)
            if task_data:
                return task_data, 200
        except Exception as e:
            log.exception(e)
            return "Could not retrieve task. Please try again later.", 500

        return f"No task of ID {task_id} could be found.", 404

    @ns.doc()
    @login_required
    def put(self, task_id):
        try:
            json_content = request.json

            if json_content is None:
                return "Please specify task data in json format", 400
            else:
                task_data = json_content

            TASKS_DAL.update_task(task_id, task_data)
            return 200
        except Exception as e:
            log.exception(e)
            return "Could not update task. Please try again later.", 500

    @ns.doc()
    @login_required
    def delete(self, task_id):
        try:
            TASKS_DAL.delete_task(task_id)
        except Exception as e:
            log.exception(e)
            return "Could not delete task. Please try again later.", 500

        return 200

