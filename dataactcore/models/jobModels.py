""" These classes define the ORM models to be used by sqlalchemy for the job tracker database """

import sqlalchemy
from sqlalchemy import Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from jobTrackerInterface import JobTrackerInterface


Base = declarative_base()
class JobStatus(Base):
    __tablename__ = 'job_status'

    job_id = Column(Integer, primary_key=True)
    filename = Column(Text)
    status_id = Column(Integer)
    type_id = Column(Integer)
    resource_id = Column(Integer)

class JobDependency(Base):
    __tablename__ = 'job_dependency'

    dependency_id = Column(Integer, primary_key=True)
    job_id = Column(Integer)
    prerequisite_id = Column(Integer)

class Status(Base):
    __tablename__ = 'status'
    STATUS_DICT = None
    STATUS_LIST = ["waiting","running","finished"]

    status_id = Column(Integer, primary_key=True)
    name = Column(Text)
    description = Column(Text)
    session = None

    @staticmethod
    def getStatus(statusName):
        if(Status.STATUS_DICT == None):
            # Pull status values out of DB
            for status in Status.STATUS_LIST:
                Status.STATUS_DICT[status] = Status.setStatus(status)
        if(not statusName in Status.STATUS_DICT):
            raise ValueError("Not a valid job status")
        return Status.STATUS_DICT[statusName]


    @staticmethod
    def setStatus(name):
        """  Get an id for specified status, if not unique throw an exception

        Arguments:
        name -- Name of status to get an id for

        Returns:
        status_id of the specified status
        """
        if(Status.session == None):
            Status.session = JobTrackerInterface().getSession()
        queryResult = Status.session.query(Status.status_id).filter(Status.name==name).all()
        if(len(queryResult) != 1):
            # Did not get a unique result
            raise ValueError("Database does not contain a unique ID for status "+name)
        else:
            return queryResult[0].status_id

class Type(Base):
    __tablename__ = 'type'
    TYPE_DICT = None
    TYPE_LIST = ["file_upload", "csv_record_validation","validation","external_validation"]

    @staticmethod
    def getType(typeName):
        if(Type.TYPE_DICT == None):
            # Pull status values out of DB
            for type in Type.TYPE_LIST:
                Type.TYPE_DICT[type] = Type.setType(type)
        if(not typeName in Type.TYPE_DICT):
            raise ValueError("Not a valid job type")
        return Type.TYPE_DICT[typeName]

    @staticmethod
    def setType(name):
        """  Get an id for specified type, if not unique throw an exception

        Arguments:
        name -- Name of type to get an id for

        Returns:
        type_id of the specified type
        """
        if(Status.session == None):
            Status.session = JobTrackerInterface().getSession()
        queryResult = Status.session.query(Type.type_id).filter(Type.name==name).all()
        if(len(queryResult) != 1):
            # Did not get a unique result
            raise ValueError("Database does not contain a unique ID for type "+name)
        else:
            return queryResult[0].type_id

    type_id = Column(Integer, primary_key=True)
    name = Column(Text)
    description = Column(Text)

class Resource(Base):
    __tablename__ = 'resource'

    resource_id = Column(Integer, primary_key=True)