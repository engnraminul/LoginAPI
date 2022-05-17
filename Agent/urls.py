from django.urls import path
from Agent.views import AgentDetailsView, AgentListView, TopSellerListView

urlpatterns = [
    path('list/', AgentListView.as_view()),
    path('<pk>/', AgentDetailsView.as_view()),
    path('top-seller/', TopSellerListView.as_view()),

]
