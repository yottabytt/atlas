

class QueueJob(object):
    """Create and posts a message indicated that a job is the queue

    Arguments:
        message_router {MessageRouter} -- The message router with which to push the message with
        pipeline_context {PipelineContext} -- The pipeline context associated with the job
    """

    def __init__(self, message_router, foundations_job):
        self._message_router = message_router
        self._foundations_job = foundations_job

    def push_message(self):
        """See above
        """

        message = self._message()
        self._message_router.push_message('queue_job', message)

    def _message(self):
        message = {
            'job_id': self._foundations_job.job_id,
            'project_name': self._foundations_job.project_name,
            'job_parameters': self._foundations_job.provenance.job_run_data,
            'user_name': self._foundations_job.user_name,
            'annotations': self._foundations_job.provenance.annotations,
        }

        return message
