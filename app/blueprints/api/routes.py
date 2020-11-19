from .import bp as api
from flask import jsonify, request
from app import db
from app.blueprints.blog.models import BlogPost

@api.route('/blog', methods=['GET'])
def blog_posts():
    return jsonify([p.to_dict() for p in BlogPost.query.all()])

@api.route('/blog/<int:id>', methods=['GET'])
def single_post(id):
    """
    [GET] /api/blog/<id>
    """
    p = BlogPost.query.get(id)
    return jsonify(p.to_dict())

@api.route('/blog/create', methods=['POST'])
def create_post():
    data = request.json
    post = BlogPost()
    post.from_dict(data)
    post.save()
    return jsonify(post.to_dict()), 201

@api.route('blog/edit/<int:id>', methods=['PUT'])
def edit_post(id):
    """
    [PUT/PATCH] /api/blog/edit/<id>
    """
    data = request.json
    p = BlogPost.query.get(id)
    p.from_dict(data)
    db.session.commit()
    return jsonify(p.to_dict())
    
@api.route('/blog/delete/<int:id>', methods=['DELETE'])
def delete_post(id):
    """
    [DELETE] /api/blog/delete/<id>
    """
    p = BlogPost.query.get(id)
    p.remove()
    return jsonify([p.to_dict() for p in BlogPost.query.all()])
