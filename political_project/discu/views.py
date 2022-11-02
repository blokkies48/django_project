from email import message
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Discussion, Message
from .forms import Discussion_Form
from django.contrib.auth.decorators import login_required

# Create your views here.

# Gets all the discussions in the database and displays them
def discussions(request):
    discussions = Discussion.objects.all()
    context = {'discussions': discussions}
    return render(request, 'discussions/discussions.html', context)

# Displays the info about the discussion
# And the messages relating to the discussion 
def discussion(request, pk):
    discussion = Discussion.objects.get(id=pk)
    messages = Message.objects.all().order_by('created')

    # Manages the new comments
    if request.method == 'POST':
        messages = Message.objects.create(
            user = request.user,
            discussion = discussion,
            body = request.POST.get('body')
        )
        return redirect('discussion', pk=discussion.id)

    context = {'discussion': discussion, 'messages': messages}
    return render(request, 'discussions/discussion.html', context)

# When you create a new discussion
# User must be logged in to create
@login_required(login_url="/login")
def start_discussion(request):
    form = Discussion_Form() # Sets form
    if request.method == 'POST': # Checks if it is a post method in template
        form = Discussion_Form(request.POST)
        if form.is_valid(): # If valid form
            form.save() # Then saves to database
            return redirect("discussions") # Goes back to page with all discussions
    # Goes to the page where the new form is to be created
    context = {'form': form}
    return render(request, 'discussions/d_form.html', context)

# The logic in the following functions are basically the same as above
@login_required(login_url="/login")
def update_discussion(request, pk):
    discussion = Discussion.objects.get(id=pk)
    form = Discussion_Form(instance=discussion)
    # Only the user that created of the discussion can update it 
    # Even if the id is known
    if request.user != discussion.host:
        return HttpResponse("You are not the author of this discussion")
    if request.method == 'POST':
        form = Discussion_Form(request.POST, instance=discussion)
        if form.is_valid():
            form.save()
            return redirect("discussions")
    context = {'form': form}
    return render(request, 'discussions/d_form.html', context)


@login_required(login_url="/login")
def delete_discussion(request, pk):
    discussion = Discussion.objects.get(id=pk)

    if request.user != discussion.host:
        return HttpResponse("You are not the author of this discussion")
        
    if request.method == "POST":
        discussion.delete()
        return redirect("discussions")
    return render(request, 'discussions/delete.html', {'obj': discussion})
    
@login_required(login_url="/login")
def delete_comment(request, pk):
    message = Message.objects.get(id=pk)
    if request.user != message.user:
        return HttpResponse("You can not delete this comment")
        
    if request.method == "POST":
        message.delete()
        return redirect("discussions")
    return render(request, 'discussions/delete.html', {'obj': message})