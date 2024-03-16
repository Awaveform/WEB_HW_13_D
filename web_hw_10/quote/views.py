from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import TagForm, QuoteForm, AuthorForm
from .models import Tag, Quote, Author


# Create your views here.


# def main(request):
#     return render(request, 'quote/index.html')
# def main(request):
#     quotes = Quote.objects.all()
#     return render(request, 'quote/index.html', {"quotes": quotes})

# quote/views.py - add output to the main page
def main(request):
    quotes = Quote.objects.filter(
        # user=request.user
    ).all() #if request.user.is_authenticated else []
    return render(
        request,
        'quote/index.html',
        {"quotes": quotes}
    )


# def tag(request):
#     if request.method == 'POST':
#         form = TagForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(to='quote:main')
#         else:
#             return render(request, 'quote/tag.html', {'form': form})
#
#     return render(request, 'quote/tag.html', {'form': TagForm()})
@login_required
def tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            _tag = form.save(commit=False)
            _tag.user = request.user
            _tag.save()
            return redirect(to='quote:main')
        else:
            return render(request, 'quote/tag.html', {'form': form})

    return render(request, 'quote/tag.html', {'form': TagForm()})


# def quote(request):
#     tags = Tag.objects.all()
#
#     if request.method == 'POST':
#         form = QuoteForm(request.POST)
#         if form.is_valid():
#             new_quote = form.save()
#
#             choice_tags = Tag.objects.filter(
#                 name__in=request.POST.getlist('tags')
#             )
#             for _tag in choice_tags.iterator():
#                 new_quote.tags.add(_tag)
#
#             return redirect(to='quote:main')
#         else:
#             return render(
#                 request,
#                 'quote/quote.html',
#                 {"tags": tags, 'form': form}
#             )
#
#     return render(
#         request,
#         'quote/quote.html',
#         {"tags": tags, 'form': QuoteForm()}
#     )
@login_required
def quote(request):
    tags = Tag.objects.filter().all()
    authors = Author.objects.filter().all()
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save(commit=False)
            new_quote.user = request.user
            new_quote.author = Author.objects.filter(
                fullname=request.POST.get("authors")
            ).first()
            new_quote.save()
            choice_tags = Tag.objects.filter(
                name__in=request.POST.getlist('tags'),
                user=request.user
            )
            for _tag in choice_tags.iterator():
                new_quote.tags.add(_tag)
            return redirect(to='quote:main')
        else:
            return render(
                request,
                'quote/quote.html',
                {"tags": tags, "authors": authors, 'form': form}
            )

    return render(
        request,
        'quote/quote.html',
        {"tags": tags, "authors": authors, 'form': QuoteForm()}
    )


# def detail(request, quote_id):
#     quote = get_object_or_404(Quote, pk=quote_id)
#     return render(
#         request,
#         'quote/detail.html',
#         {"quote": quote}
#     )
@login_required
def detail(request, quote_id):
    _quote = get_object_or_404(Quote, pk=quote_id, user=request.user)
    return render(
        request,
        'quote/detail.html',
        {"quote": _quote, "is_user_owner": True}
    )


# def set_done(request, quote_id):
#     Quote.objects.filter(pk=quote_id).update(done=True)
#     return redirect(to='quote:main')
@login_required
def set_done(request, quote_id):
    Quote.objects.filter(pk=quote_id, user=request.user).update(done=True)
    return redirect(to='quote:main')


# def delete_quote(request, quote_id):
#     Quote.objects.get(pk=quote_id).delete()
#     return redirect(to='quote:main')
@login_required
def delete_quote(request, quote_id):
    Quote.objects.get(pk=quote_id, user=request.user).delete()
    return redirect(to='quote:main')


@login_required
def author(request):
    # tags = Tag.objects.filter(user=request.user).all()

    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            new_author = form.save(commit=False)
            new_author.user = request.user
            new_author.save()
            # choice_tags = Tag.objects.filter(
            #     name__in=request.POST.getlist('tags'),
            #     user=request.user
            # )
            # for _tag in choice_tags.iterator():
            #     new_quote.tags.add(_tag)

            return redirect(to='quote:main')
        else:
            return render(
                request,
                'quote/author.html',
                {'form': form}
            )

    return render(
        request,
        'quote/author.html',
        {'form': AuthorForm()}
    )


@login_required
def author_detail(request, author_id):
    _author = get_object_or_404(Author, pk=author_id, user=request.user)
    return render(
        request,
        'quote/author_detail.html',
        {"quote": _author, "is_user_owner": True}
    )


@login_required
def set_done_author(request, author_id):
    Author.objects.filter(pk=author_id, user=request.user).update(done=True)
    return redirect(to='quote:main')


@login_required
def delete_author(request, author_id):
    Author.objects.get(pk=author_id, user=request.user).delete()
    return redirect(to='quote:main')
