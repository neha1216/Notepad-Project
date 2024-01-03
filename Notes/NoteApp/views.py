from django.http import HttpResponse
from django.shortcuts import render
from .models import NoteAPP

def index(request):
    return HttpResponse("Hello, world. You're at the notes app.")

def create_notes(request):
    notes_obj = NoteAPP()
    notes_obj.username = 'Nidhi'
    # import pdb
    # pdb.set_trace()
    if request.GET.get('new_note'):
        notes_obj.notes_content = request.GET.get('new_note')
        notes_obj.Note_title = request.GET.get('new_title')
    else:
        return HttpResponse("Note not saved,something went wrong")
    notes_obj.save()

    return HttpResponse("Notes saved")

def create_page(request):
    logged_in_user = 'Nidhi'
    print("came in create note")
    context_data = {"logged_in_user": logged_in_user}
    return render(request, "NoteApp/create_note.html", context=context_data)


def view_notes(request):
    logged_in_user = 'Nidhi'
    notes = NoteAPP.objects.filter(username=logged_in_user)
    notes = [note.__dict__ for note in notes]
    all_notes = {"notes": notes}
    
    return render(request, "NoteApp/index.html", context=all_notes)

    # return HttpResponse("Hello, world. You're at the view section.")

def edit_page(request):
    logged_in_user = 'Nidhi'
    note_id = request.GET.get('note_id')
    notes = NoteAPP.objects.filter(id=note_id)
    notes_obj = notes[0]
    content = notes_obj.notes_content
    title = notes_obj.Note_title
    print(content)

    context_data = {"logged_in_user": logged_in_user,
                    "present_content": content,
                    "present_title" : title,
                    "note_id": notes_obj.id}
    return render(request, "NoteApp/edit_note.html", context=context_data)


def edit_notes(request):
    user_name = 'Nidhi'
    note_title = request.GET.get('Note_title')
    notes_id = request.GET.get('note_id')
    edited_note = request.GET.get('edited_note')
    notes = NoteAPP.objects.filter(id=notes_id)

    notes_obj = notes[0]
    notes_obj.notes_content = edited_note
    notes_obj. Note_title =  note_title
    notes_obj.save()

    return HttpResponse("Hello, world. Your note is saved")

def delete_notes(request):
    notes_id = request.GET.get('note_id')

    notes = NoteAPP.objects.filter(id=int(notes_id))
    notes.delete()

    return HttpResponse("Note Deleted")


