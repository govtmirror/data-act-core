from dataactcore.models.jobModels import JobStatus, JobDependency, Submission
from dataactcore.models.jobTrackerInterface import JobTrackerInterface

def clearJobs():
    """Use this instead of setupJobTracker.py if an app is currently running."""
    jobDb = JobTrackerInterface()
    jobDb.session.query(JobDependency).delete()
    jobDb.session.query(JobStatus).delete()
    jobDb.session.query(Submission).delete()
    jobDb.session.commit()
    jobDb.session.close()

if __name__ == '__main__':
    clearJobs()