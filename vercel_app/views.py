from rest_framework.decorators import api_view
from rest_framework.response import Response
from vercel_app.core.retreive import Leetcode_retreive_fn,Github_retreive_fn,LinkedIn_retreive_fn,Hackerrank_retreive_fn,Codechef_retreive_fn,Codeforces_retreive_fn

@api_view(['GET'])
def LeetcodeView(request, pk):
    ret = Leetcode_retreive_fn(pk)
    return Response(ret)

@api_view(['GET'])
def GithubView(request, pk):
    ret = Github_retreive_fn(pk)
    return Response(ret)

@api_view(['GET'])
def LinkedinView(request, pk):
    ret = LinkedIn_retreive_fn(pk)
    return Response(ret)

@api_view(['GET'])
def HackerrankView(request, pk):
    ret = Hackerrank_retreive_fn(pk)
    return Response(ret)

@api_view(['GET'])
def CodechefView(request, pk):
    ret = Codechef_retreive_fn(pk)
    return Response(ret)

@api_view(['GET'])
def CodeforcesView(request, pk):
    ret = Codeforces_retreive_fn(pk)
    return Response(ret)
