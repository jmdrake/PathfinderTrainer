### we prepend t_ to tablenames and f_ to fieldnames for disambiguity


########################################
db.define_table('t_track',
    Field('f_title_string', type='string',
          label=T('Title String')),
    Field('f_description', type='text',
          label=T('Description')),
    auth.signature,
    format='%(f_title_string)s',
    migrate=settings.migrate)

db.define_table('t_track_archive',db.t_track,Field('current_record','reference t_track',readable=False,writable=False))

########################################
db.define_table('t_requirement',
    Field('f_level_string', type='string',
          label=T('Level String')),
    Field('f_title_string', type='string',
          label=T('Title String')),
    Field('f_description', type='text',
          label=T('Description')),
    Field('f_upload', type='boolean',
          label=T('Upload')),
    auth.signature,
    format='%(f_level_string)s',
    migrate=settings.migrate)

db.define_table('t_requirement_archive',db.t_requirement,Field('current_record','reference t_requirement',readable=False,writable=False))

########################################
db.define_table('t_trainee',
    Field('f_name', type='string',
          label=T('Name')),
    Field('f_phonenumbers', type='list:string',
          label=T('Phonenumbers')),
    Field('f_email', type='string',
          label=T('Email')),
    Field('f_address', type='string',
          label=T('Address')),
    auth.signature,
    format='%(f_name)s',
    migrate=settings.migrate)

db.define_table('t_trainee_archive',db.t_trainee,Field('current_record','reference t_trainee',readable=False,writable=False))

########################################
db.define_table('t_completion',
    Field('f_trainee_id', type='reference t_trainee',
          label=T('Trainee Id')),
    Field('f_completed', type='date',
          label=T('Completed')),
    Field('f_requirement_id', type='reference t_requirement',
          label=T('Requirement Id')),
    auth.signature,
    format='%(f_trainee_id)s',
    migrate=settings.migrate)

db.define_table('t_completion_archive',db.t_completion,Field('current_record','reference t_completion',readable=False,writable=False))
