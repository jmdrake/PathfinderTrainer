# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
def index():
    return dict()

def error():
    return dict()

@auth.requires_login()
def trainee_manage():
    form = SQLFORM.smartgrid(db.t_trainee,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def track_manage():
    form = SQLFORM.smartgrid(db.t_track,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def requirement_manage():
    form = SQLFORM.smartgrid(db.t_requirement,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def completion_manage():
    form = SQLFORM.smartgrid(db.t_completion,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def classcard():
    rows = db().select(
        db.requirement.ALL, db.completion.ALL,
        left=db.completion.on(db.requirement.id == db.completion.requirement_id))
    return locals()
