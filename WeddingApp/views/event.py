from django.http import JsonResponse
from rest_framework.response import Response
from WeddingApp.renderers import UserProfileRenderer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework_simplejwt.authentication import JWTAuthentication
from WeddingApp.models import Event
from WeddingApp.permissions import IsSuperuserOrReadOnly,EventPermission
from WeddingApp.serializers import EventSerializer
from WeddingApp.pagination import MyPageNumberPagination
from WeddingApp.models import Category
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

class EventViewSet(viewsets.ModelViewSet):
    renderer_classes = [UserProfileRenderer]
    pagination_class = MyPageNumberPagination
    permission_classes = [EventPermission]
    authentication_classes = [JWTAuthentication]
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.filter(Q(user=self.request.user) | Q(invited=self.request.user) | Q(is_private=False)).distinct()

    # def get_queryset(self):
    #     user = self.request.user
    #     if user.is_authenticated:
    #         queryset = Event.objects.filter(
    #             Q(is_private=False) | 
    #             Q(is_private=True, user=user) |
    #             Q(is_private=True, invited=user)
    #         ).distinct()
    #     else:
    #         queryset = Event.objects.filter(is_private=False).distinct()
    #     return queryset

    def list(self, request):
        queryset = self.get_queryset().order_by('-updated_at')
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
       
    def create(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error":  serializer.errors}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    def partial_update(self, request, pk=None):
        try:
            instance = self.get_queryset().get(id=pk)
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Event partially updated successfully", "event_detail":serializer.data})
            return Response({"errors": serializer.errors}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except Event.DoesNotExist:
            return Response({"Event": "Event not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def destroy(self,request,pk=None):
        try:
            instance = self.get_queryset().get(id=pk)
            instance.delete()
            return Response({"message": "Event deleted successfully"}, status=status.HTTP_200_OK)
        except Event.DoesNotExist:
            return Response({"Event": "Event not found"}, status=status.HTTP_404_NOT_FOUND)
    
    @action(detail=False, methods=['get'], url_path='get-events-for-category')
    def get_events_for_category(self, request, category_id):
        try:
            category = Category.objects.get(pk=category_id)
        except Category.DoesNotExist:
            return JsonResponse({"error": "Category not found"}, status=404)
        events = Event.objects.filter(event_category_id=category_id)
        serializer = EventSerializer(events, many=True)
        if events.exists():
            return JsonResponse({"message": "Events retrieved successfully", "event_detail": serializer.data}, status=200)
        else:
            return JsonResponse({"message": "No events found for the provided category"}, status=404)
