from django.http import Http404
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from . models import Answers, Questions
from .forms import Question , Answer
# Create your views here.

login_redirect = "authenticate:login"

@login_required(login_url=login_redirect)
def ask_question(request):
    if "logout" in request.POST:
        logout(request)
        return redirect(reverse(login_redirect))
    if request.POST:
        question = request.POST['question']
        user = request.user 
        Questions.objects.create(question=question, user=user)
    
    form = Question

    return render(request, "ask.html", context={"title":"Ask", "form":form})


def feed(request):
    all_question = Questions.objects.all()[:10]
    if "logout" in request.POST:
        logout(request)
        return redirect(reverse(login_redirect))
    
    return render(request, "feed.html", context={"questions": all_question, "title":"feed"})


@login_required(login_url=login_redirect)
def view_comments(request, num):
    if "logout" in request.POST:
        logout(request)
        return redirect(reverse(login_redirect))
        
    try:
        post = Questions.objects.get(id=num)
    except Exception:
        raise Http404("The quesiton may be deleted")

    if request.POST:
        answer = request.POST["answer"]
        Answers.objects.create(posted_by=request.user, post=post, answer
        =answer)
    answers = Answers.objects.filter(post=post).all()

    form = Answer()
    
    return render(request, "view_comment.html", context={"title":"comments", "asked":post.user ,  "answers":answers, "form":form})

@login_required(login_url=login_redirect)
def user_posts(request):
    if "logout" in request.POST:
        logout(request)
        return redirect(reverse(login_redirect))
        
    posts = Questions.objects.filter(user=request.user).all()

    return render(request, "user_posts.html", context={"title":"Your post" , "questions":posts})

@login_required(login_url=login_redirect)
def delete_post(request, id):
    try:
        post = Questions.objects.get(pk=id)
    except Exception:
        raise Http404("The page you are searching for does not exist")
    see = True
    if post.user != request.user:
        see = False

    if "logout" in request.POST:
        logout(request)
        return redirect(reverse(login_redirect))
    
    elif request.POST:
        Questions.objects.get(pk=id).delete()
        return redirect(reverse("stack:posts"))

    return render(request, "delete.html", context={"post":post, "title":f"delete {post}", "see":see})
