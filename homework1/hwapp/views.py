from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.info('New user')
    html = '''
    <h1>Супер, мега сайт Django</h1>
    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. 
    Repudiandae vero tempore qui, recusandae quisquam totam 
    illum enim cupiditate earum molestias.</p>
    '''
    return HttpResponse(html)


def about(request):
    logger.info('New user')
    html = '''
    <h1>Кто я?</h1>
    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. 
    Repudiandae vero tempore qui, recusandae quisquam totam 
    illum enim cupiditate earum molestias.</p>
    <h2>Где я?</h2>
    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. 
    Repudiandae vero tempore qui, recusandae quisquam totam 
    illum enim cupiditate earum molestias.</p>
    '''
    return HttpResponse(html)
