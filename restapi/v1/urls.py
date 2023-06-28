from django.urls import path, include, re_path

from restapi.v1.api_compiler import views as compiler_views
from restapi.v1.auth import views as auth_views
from restapi.v1.chat_gpt import views as gpt_views
from restapi.v1.problems import views as problems_views
from restapi.v1.problems_examples import views as problem_examples_views
from restapi.v1.rank import views as rank_views
from restapi.v1.topics import views as topics_views
from restapi.v1.user_solution_submissions import views as user_submissions_views
from restapi.v1.users import views as users_views

auth_urlpatterns = [
    path(r'login/', auth_views.AuthViewSet.Login.as_view(), name="login"),
    path(r'logout/', auth_views.AuthViewSet.Logout.as_view(), name="logout"),
    path(r'register-user/', auth_views.AuthViewSet.Register.as_view(), name="register"),
    path(
        r'reset-password/', auth_views.AuthViewSet.ResetPassword.as_view(),
        name="reset-password"
    ),
    path(r'set-csrf/', auth_views.AuthViewSet.set_csrf_token, name='Set-CSRF'),
]

users_urlpatterns = [
    # users
    path(
        r'',
        users_views.UserViewSet.UserListView.as_view(),
        name="list-users"
    ),
    re_path(
        r'^(?P<pk>[0-9]+)/$',
        users_views.UserViewSet.UserUpdateView.as_view(),
        name="get-user-by-id"
    ),
    path(
        r'profile/',
        users_views.UserViewSet.UserDetailsView.as_view(),
        name="get-users-profile"
    ),
    path(
        r'rank/',
        rank_views.RankViewSet.RankListView.as_view(),
        name="list-users-rank"
    ),
    re_path(
        r'rank/(?P<search_value>[\w\-]+)/$',
        rank_views.RankViewSet.RankRetrieveView.as_view(),
        name="get-user-rank-by-username"
    ),
    path(
        r'change-password/',
        users_views.UserViewSet.ChangePassword.as_view(),
        name="change-password"
    ),
]

topics_urlpatterns = [
    # topics
    path(
        r'',
        topics_views.TopicViewSet.TopicsListView.as_view(),
        name="list-topics"
    ),
    re_path(
        r'^(?P<pk>[0-9]+)/$', topics_views.TopicViewSet.TopicUpdateView.as_view(),
        name="get-topic-by-id"
    ),
]

problems_urlpatterns = [
    # problems
    path(
        r'',
        problems_views.ProblemViewSet.ProblemView.as_view(),
        name="list-problems"
    ),

    path(
        r'admin-list-problems/',
        problems_views.ProblemViewSet.ProblemAdminView.as_view(),
        name="list-problems-admin"
    ),

    re_path(
        r'^(?P<pk>[0-9]+)/$',
        problems_views.ProblemViewSet.ProblemUpdateView.as_view(),
        name="update"
    ),
]

problem_examples_urlpatterns = [
    # problem examples
    path(
        r'',
        problem_examples_views.ProblemExampleViewSet.ProblemExampleView.as_view(),
        name="list-problems"
    ),
]

compiler_urlpatterns = [
    # compiler
    path(
        r'compile-and-run/',
        compiler_views.CompilerViewSet.CompilerRunCodeView.as_view(),
        name="compile_and_run"
    ),
    path(
        r'submit-solution/',
        compiler_views.CompilerViewSet.CompilerSubmitSolutionView.as_view(),
        name="submit-solution"
    ),
]

user_submissions_patterns = [
    re_path(
        r'^(?P<pk>[0-9]+)/$',
        user_submissions_views.UserSolutionViewSet.UserSolutionView.as_view(),
        name="get-user-submissions"
    ),
    path(
        r'all-max-submissions/',
        user_submissions_views.UserSolutionViewSet.UserAllMaxSolutionsView.as_view(),
        name="all-max-submissions"
    ),
    path(
        r'all/',
        user_submissions_views.UserSolutionViewSet.UserAllSolutionsView.as_view(),
        name="all-submissions"
    ),
]

chat_gpt_patterns = [
    path(
        r'code-improvements/',
        gpt_views.GPTViewSet.ChatGPTView.as_view(),
        name="get-code-improvements"
    ),
]

urlpatterns = [
    path(r'auth/', include((auth_urlpatterns, 'auth'), namespace='auth')),
    path(r'users/', include((users_urlpatterns, 'users'), namespace='users')),
    path(r'topics/', include((topics_urlpatterns, 'topics'), namespace='topics')),
    path(r'problems/', include((problems_urlpatterns, 'problems'), namespace='problems')),
    path(r'compiler/', include((compiler_urlpatterns, 'compiler'), namespace='compiler')),
    path(r'user-submissions/',
         include(
             (user_submissions_patterns, 'user-submissions'), namespace='user-submissions')
         ),
    path(r'ai/', include((chat_gpt_patterns, 'chat_gpt'), namespace='chat_gpt')),
]
