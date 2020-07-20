from django.urls import path,include
from blog.views import index,post_details,contact_us_form_view,register_form_view,post_form_view,post_update_form_view
from blog.views import HomeView,PostView,PostForm,PostListView,PostDetailView,AboutUs
from blog import views
urlpatterns = [
    path('',PostListView.as_view(),name = "home"),
    #path('blogs/<slug:slug>',RedirectPost.as_view()), 
    path('blogs/<slug:slug>',PostDetailView.as_view(),name ="post-detail"),
    path('category/<int:id>',views.CategoryView.as_view(), name='category'), 
    path('search/', views.search, name='search'),
    path('contact',contact_us_form_view,name = 'contact'),
    path('post',post_form_view),
    path('post/<int:id>',post_update_form_view),
    path('about-us',AboutUs.as_view(),name= 'about'),
    path('service',AboutUs.as_view(),name = 'services'),

]