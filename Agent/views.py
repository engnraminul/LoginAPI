
from rest_framework import permissions
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveDestroyAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from Agent.models import Agent
from Agent.serializers import AgentSerializer

class AgentListView(ListAPIView):
    permission_classes=(permissions.AllowAny,)
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    pagination_class = None
    


class TopSellerListView(ListAPIView):
    permission_classes=(permissions.AllowAny,)
    queryset = Agent.objects.filter(top_seller = True)
    serializer_class = AgentSerializer
    pagination_class = None
    

class AgentDetailsView(RetrieveAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    

