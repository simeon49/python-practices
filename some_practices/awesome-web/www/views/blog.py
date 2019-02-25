# -*- coding: utf-8 -*


from aiohttp import web
from core_web import get, post, APIError

from models import Blog

print(dir(Blog.findAll))

@get('/')
async def get_blogs():
    blogs = await Blog.findAll(orderBy='create_time desc')
    return dict(blogs=blogs)

@get('/blog/{id}')
async def get_blog(id):
    blog = await Blog.find(pk=id)
    return blog

@post('/blogs')
async def create_blog(*, user_id, title, content):
    blog = Blog(user_id=user_id, title=title, content=content)
    try:
        await blog.save()
    except Exception as e:
        raise APIError(error=e, message='create blog fail.')
    return blog
