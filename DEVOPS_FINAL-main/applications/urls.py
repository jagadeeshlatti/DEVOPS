from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home_page'),
    path('login/',views.loginHandler,name='login'),
    path('register/',views.registerHandler,name='register'),
    path('about/',views.about),
    path('auth/',views.authPage,name='auth_page'),
    path('personaldetailsform/',views.personalFormsPage,name='personal_form_page'),
    path('edu&financedetailsform/',views.educationalDetailsForm,name='educational_form_page'),
    # path('uploadDocuments/',views.uploadDocumentsForm,name='upload_documents_page'),
    path('submit_the_Application/',views.submitApplication,name='submit_page'),
    path('logout/',views.logoutUser,name='logout_page'),
    path('download/',views.downloadPdf,name='download_pdf')
]