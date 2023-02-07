from django.urls import path, include, re_path

from restapi.v1.problems import views as problems_views
from restapi.v1.problems_examples import views as problem_examples_views
from restapi.v1.topics import views as topics_views
from restapi.v1.users import views as users_views

users_urlpatterns = [
    # users
    path(r'', users_views.UserViewSet.UserListView.as_view(), name="list"),
]

topics_urlpatterns = [
    # topics
    path(r'', topics_views.TopicViewSet.TopicsListView.as_view(), name="list"),
]

problems_urlpatterns = [
    # problems
    path(r'', problems_views.ProblemViewSet.ProblemView.as_view(), name="list"),
    re_path(r'^(?P<pk>[0-9]+)/$', problems_views.ProblemViewSet.ProblemUpdateView.as_view(), name="update"),
]

problemExamples_urlpatterns = [
    # problem examples
    path(r'', problem_examples_views.ProblemExampleViewSet.ProblemExampleView
         .as_view(), name="list"),
]

urlpatterns = [
    path(r'users/', include((users_urlpatterns, 'users'), namespace='users')),
    path(r'topics/', include((topics_urlpatterns, 'topics'), namespace='topics')),
    path(r'problems/', include((problems_urlpatterns, 'problems'), namespace='problems'))
]
