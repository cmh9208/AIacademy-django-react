from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from blog.comments.repository import CommentRepository
from blog.comments.serializers import CommentSerializer


@api_view(['POST','PUT','PATCH','DELETE','GET'])
@parser_classes([JSONParser])
def comment(request):
    if request.method == "POST":
        return CommentSerializer().create(request.data)
    elif request.method == "GET":
        return CommentRepository().find_by_id(request.data)
    elif request.method == "PATCH":
        return None
    elif request.method == "PUT":
        return CommentSerializer().update(request.data)
    elif request.method == "DELETE":
        return CommentSerializer().delete(request.data)

@api_view(['GET'])
@parser_classes([JSONParser])
def comment_list(request): return CommentRepository().get_all(request.data)
