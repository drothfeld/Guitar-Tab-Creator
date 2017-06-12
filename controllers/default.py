# Imported Modules
from datetime import datetime


def index():
    note_list_e = ['e01', 'e02', 'e03', 'e04', 'e05', 'e06']
    note_list_b = ['b01', 'b02', 'b03', 'b04', 'b05', 'b06']
    note_list_g = ['g01', 'g02', 'g03', 'g04', 'g05', 'g06']
    note_list_d = ['d01', 'd02', 'd03', 'd04', 'd05', 'd06']
    note_list_a = ['a01', 'a02', 'a03', 'a04', 'a05', 'a06']
    note_list_E = ['E01', 'E02', 'E03', 'E04', 'E05', 'E06']
    song_list = db().select(db.songs.ALL, orderby=~db.songs.date_created)
    song_form = SQLFORM(db.songs)
    if song_form.process().accepted:
        db(db.songs.last_name == "None").update(last_name=auth.user.last_name)
        db(db.songs.first_name == "None").update(first_name=auth.user.first_name)
        cond1 = (db.placeholder.static_id == "STATIC")
        selected_buffer = db(cond1).select()
        for n in selected_buffer:
            buffer_e = n.BUFFER_note_list_e
            buffer_b = n.BUFFER_note_list_b
            buffer_g = n.BUFFER_note_list_g
            buffer_d = n.BUFFER_note_list_d
            buffer_a = n.BUFFER_note_list_a
            buffer_E = n.BUFFER_note_list_lowE
        db(db.songs.note_list_e == "null_e").update(note_list_e=buffer_e)
        db(db.songs.note_list_b == "null_b").update(note_list_b=buffer_b)
        db(db.songs.note_list_g == "null_g").update(note_list_g=buffer_g)
        db(db.songs.note_list_d == "null_d").update(note_list_d=buffer_d)
        db(db.songs.note_list_a == "null_a").update(note_list_a=buffer_a)
        db(db.songs.note_list_lowE == "null_lowE").update(note_list_lowE=buffer_E)
        redirect(URL('default', 'view_songs'))
    return dict(song_list=song_list, song_form=song_form, note_list_e=note_list_e,
                note_list_b=note_list_b, note_list_g=note_list_g, note_list_d=note_list_d,
                note_list_a=note_list_a, note_list_E=note_list_E)


def view_songs():
    song_list = db().select(db.songs.ALL, orderby=~db.songs.date_created)
    return dict(song_list=song_list)


def view_songs_tab():
    song_id = request.args(0)
    cond1 = (db.songs.id == song_id)
    selected_song = db(cond1).select()
    comment_form = SQLFORM(db.comments)
    if comment_form.process().accepted:
        cond2 = (db.comments.static_comment_id == "STATIC_COMMENT")
        selected_comment = db(cond2).select()
        for m in selected_song:
            current_comments = m.comments
        for c in selected_comment:
            buffer_comment = str(current_comments) + "• " + auth.user.first_name + ' ' + auth.user.last_name +\
                             " @ " + str(c.comment_date) + "\n" + str(c.enter_comment) + "\n" + "\n"
        db(db.songs.id == song_id).update(comments=buffer_comment)
        redirect(URL('default', 'view_songs_tab', args=song_id))
    return dict(selected_song=selected_song, comment_form=comment_form, song_id=song_id)


@auth.requires_signature()
def note_list_insert():
    notes_e = request.vars.e_notes
    notes_b = request.vars.b_notes
    notes_g = request.vars.g_notes
    notes_d = request.vars.d_notes
    notes_a = request.vars.a_notes
    notes_E = request.vars.E_notes
    db.placeholder.update_or_insert(
        (db.placeholder.static_id == 'STATIC'),
        BUFFER_note_list_e=notes_e,
        BUFFER_note_list_b=notes_b,
        BUFFER_note_list_g=notes_g,
        BUFFER_note_list_d=notes_d,
        BUFFER_note_list_a=notes_a,
        BUFFER_note_list_lowE=notes_E
    )
    return 'ok'


def delete_song():
    song = db.songs(request.args(0))
    db(db.songs.id == song.id).delete()
    redirect(URL('default', 'view_songs'))


def download():
    song_id = request.args(0)
    cond1 = (db.songs.id == song_id)
    selected_song = db(cond1).select()
    for d in selected_song:
        song_title = d.song_title
        song_author_last_name = d.last_name
        song_author_first_name = d.first_name
        song_date_created = d.date_created
        song_notes_e = d.note_list_e
        song_notes_b = d.note_list_b
        song_notes_g = d.note_list_g
        song_notes_d = d.note_list_d
        song_notes_a = d.note_list_a
        song_notes_lowE = d.note_list_lowE
    file_name = 'attachment;filename=' + song_title + ' TAB [GTC].txt'
    # Setting up csv/text file for download code from:
    # https://groups.google.com/forum/#!topic/web2py/GH2HVCGPMKo [thstart, 12/22/11]
    response.headers['Content-Type'] = 'text'
    attachment = file_name
    response.headers['Content-Disposition'] = attachment
    content = 'This TAB was created using Guitar Tab Creator (GTC) \n \n' + \
              'Title: ' + song_title + '\nCreated by: ' +  \
              song_author_first_name + ' ' + song_author_last_name + \
              '\nCreated on: ' + str(song_date_created) + '\n\nTAB: \n \n' + \
              'e|-' + song_notes_e + '\n' + 'B|-' + song_notes_b + '\n' + \
              'G|-' + song_notes_g + '\n' + 'D|-' + song_notes_d + '\n' + \
              'A|-' + song_notes_a + '\n' + 'E|-' + song_notes_lowE + '\n'
    raise HTTP(200, str(content), **{'Content-Type': 'text', 'Content-Disposition': attachment + ';'})


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())




def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()