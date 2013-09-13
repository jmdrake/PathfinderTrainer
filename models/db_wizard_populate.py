from gluon.contrib.populate import populate
if db(db.auth_user).isempty():
     populate(db.auth_user,10)
     populate(db.t_track,10)
     populate(db.t_requirement,10)
     populate(db.t_trainee,10)
     populate(db.t_completion,10)
