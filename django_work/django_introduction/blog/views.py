from django.shortcuts import render

from django.http import HttpResponse

from blog.models import Article
# Create your views here.

def hello_world(request):
    return HttpResponse("Hello World")


def article_content(request):
    article = Article.objects.all()[0]
    title = article.title
    brief_content = article.brief_content
    content = article.content
    article_id = article.article_id
    publish_date = article.publish_date
    return_str = 'title: %s, brief_content :%s, ' \
                 'content: %s, article_id: %s, publish_data: %s' % (title,
                                                                    brief_content,
                                                                    content,
                                                                    article_id,
                                                                    publish_date)

    return HttpResponse(return_str)


def get_index_page(request):
    all_article = Article.objects.all()
    return render(request, 'blog/index.html',
                  {
                      'article_list': all_article
                  }
                )

def get_detail_page(request):
    curr_article = Article.objects.all()[2]
    section_list = curr_article.content.split('\n')
    return render(request, 'blog/detail.html',
                  {
                      'curr_article': curr_article,
                      'section_list': section_list
                  }
                  )