# Imported Modules
from datetime import datetime

# Table for Songs
db.define_table('songs',
                Field('song_title', required=True),
                Field('id', db.auth_user, default=auth.user_id),
                Field('note_list_e', 'text'),
                Field('note_list_b', 'text'),
                Field('note_list_g', 'text'),
                Field('note_list_d', 'text'),
                Field('note_list_a', 'text'),
                Field('note_list_lowE', 'text'),
                Field('note_count', 'integer'),
                Field('last_name', 'text'),
                Field('first_name', 'text'),
                Field('comments', 'text'),
                Field('date_created', 'datetime', default=request.now, requires=IS_DATE(format='%d-%m-%Y')),)

db.define_table('comments',
                Field('static_comment_id', 'text'),
                Field('enter_comment', required=True),
                Field('comment_date', 'datetime', default=request.now, requires=IS_DATE(format='%d-%m-%Y')),)

db.define_table('placeholder',
                Field('static_id', 'text'),
                Field('BUFFER_note_list_e', 'text'),
                Field('BUFFER_note_list_b', 'text'),
                Field('BUFFER_note_list_g', 'text'),
                Field('BUFFER_note_list_d', 'text'),
                Field('BUFFER_note_list_a', 'text'),
                Field('BUFFER_note_list_lowE', 'text'),
                Field('note_count', 'integer'),)

db.songs.id.writable = False
db.songs.id.readable = False
db.songs.comments.writable = False
db.songs.comments.readable = False
db.songs.comments.default = " "
db.songs.id.readable = False
db.songs.note_count.writable = False
db.songs.note_count.readable = False
db.songs.note_list_e.writable = False
db.songs.note_list_e.readable = False
db.songs.note_list_e.default = "null_e"
db.songs.note_list_b.writable = False
db.songs.note_list_b.readable = False
db.songs.note_list_b.default = "null_b"
db.songs.note_list_g.writable = False
db.songs.note_list_g.readable = False
db.songs.note_list_g.default = "null_g"
db.songs.note_list_d.writable = False
db.songs.note_list_d.readable = False
db.songs.note_list_d.default = "null_d"
db.songs.note_list_a.writable = False
db.songs.note_list_a.readable = False
db.songs.note_list_a.default = "null_a"
db.songs.note_list_lowE.writable = False
db.songs.note_list_lowE.readable = False
db.songs.note_list_lowE.default = "null_lowE"
db.songs.date_created.writable = False
db.songs.date_created.readable = False
db.songs.last_name.writable = False
db.songs.last_name.readable = False
db.songs.last_name.default = "None"
db.songs.first_name.writable = False
db.songs.first_name.readable = False
db.songs.first_name.default = "None"

db.comments.static_comment_id.writable = False
db.comments.static_comment_id.readable = False
db.comments.static_comment_id.default = "STATIC_COMMENT"
db.comments.comment_date.writable = False
db.comments.comment_date.readable = False


db.placeholder.static_id.default = "STATIC"

