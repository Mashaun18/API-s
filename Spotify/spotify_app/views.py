from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Song
from .serializers import SongSerializer
from rest_framework.decorators import api_view

# @api_view(["GET", "POST"])
# def all_songs(request):
#     if request.method == "GET": 
#         all_songs = Song.objects.all()
#         serializer_class = SongSerializer(all_songs, many=True)
#         permission_classes = [IsAuthenticated]
        

# class SongRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Song.objects.all()
#     serializer_class = SongSerializer
#     permission_classes = [IsAdminUser]



@api_view(["GET", "POST"])
def all_songs(request):
    if request.method == "GET": 
        all_songs = Song.objects.all()
        serializer_class = SongSerializer(all_songs, many=True)
        return Response(serializer_class.data)
    else:
        Song_data = SongSerializer(data=request.data)
        if Song_data.is_valid():
            Song_data.save()
            return Response("You have added a new song")
        return Response(Song_data.errors)
    


@api_view(["GET", "POST", "DELETE"])
def single_songs(request, pk):
    if request.method == "GET": 
        single_songs = Song.objects.get(id=pk)
        serializer_class = SongSerializer(single_songs)
        return Response(serializer_class.data)
    elif request.method == "PUT":
        single_songs = Song.objects.get(id=pk)
        serializer_class= SongSerializer(single_songs, data=request.data, partial=True)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response("You have updated this song")
        return Response(serializer_class.errors)
    else:
        single_songs = Song.objects.get(id=pk)
        single_songs.delete()
        return Response("You have deleted this song")
