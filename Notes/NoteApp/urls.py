from django.urls import path
from . import views




urlpatterns = [
    # path("", views.home, name=""),
    path("create", views.create_notes, name="create"),
    path("create_page", views.create_page, name="view"),

    path("edit", views.edit_notes, name="edit"),
    path("edit_page", views.edit_page, name="edit"),

    # path("view", views.view_notes, name="view"),
    path("delete_note", views.delete_notes, name="delete"),
    

    # ------------------------------------------------
    
    

]







"""
create new note
cross confirming  db, newly created note should be there,
cross confirming html page 

edit recently created note (manually change primary key)
cross confirming  db, newly created note should be there,
cross confirming html page

"""