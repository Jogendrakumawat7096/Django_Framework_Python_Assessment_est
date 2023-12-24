from django.urls import path
from . import views
urlpatterns = [
path('',views.index,name='index'),
path('about',views.about,name='about'),
path('admin-login/',views.admin_login,name='admin-login'),
path('admin-logout/',views.admin_logout,name='admin-logout'),
path('adminbase/',views.adminbase,name='adminbase'),
path('admin-category/',views.admin_category,name='admin-category'),
path('add-category/',views.add_category,name='add-category'),
path('admin-view-category/',views.admin_view_category,name='admin-view-category'),
path('admin-view-policy/',views.admin_view_policy,name='admin-view-policy'),
path('admin-add-policy/',views.admin_add_policy,name='admin-add-policy'),
path('admin-update-policy/',views.admin_update_policy,name='admin-update-policy'),
path('admin-update-category/',views.admin_update_category,name='admin-update-category'),
path('admin-delete-category/<int:pk>/',views.admin_delete_category,name='admin-delete-category'),
path('admin-edit-category/<int:pk>/',views.admin_edit_category,name='admin-edit-category'),
path('admin-policy/',views.admin_policy,name='admin-policy'),
path('admin-customer-quetion/',views.admin_customer_quetion,name='admin-customer-quetion'),
path('send-message/<int:pk>/',views.send_message,name="send-message"),
path('admin-customer/',views.admin_customer,name='admin-customer'),
path('admin-customer-edit/<str:email>/',views.admin_customer_edit,name='admin-customer-edit'),
path('admin-customer-delete/<str:email>/',views.admin_customer_delete,name='admin-customer-delete'),
path('admin-policy-delete/<int:pk>/',views.admin_policy_delete,name='admin-policy-delete'),
path('admin-policy-edit/<int:pk>/',views.admin_policy_edit,name='admin-policy-edit'),
path('admin-total-policy-holder/',views.admin_total_policy_holder,name='admin-total-policy-holder'),
path('admin-total-policy-approved-holder/',views.admin_total_policy_approved_holder,name='admin-total-policy-approved-holder'),
path('admin-total-policy-disaproved-holder/',views.admin_total_policy_disaproved_holder,name='admin-total-policy-disaproved-holder'),
path('admin-total-policy-pending-holder/',views.admin_total_policy_pending_holder,name='admin-total-policy-pending-holder'),
path('admin_approved-policy/<int:pk>/',views.admin_approved_policy,name='admin-approved-policy'),




# Customer
path('customer-login/',views.customer_login,name='customer-login'),
path('customer-signup/',views.customer_signup,name='customer-signup'),
path('customer-logout/',views.customer_logout,name='customer-logout'),
path('policies/',views.policies,name='policies'),

path('apply-policy/<int:pk>/',views.apply_policy,name='apply-policy'),
path('applied-policy/',views.applied_policy,name='applied-policy'),
path('quetion-to-admin/',views.quetion_to_admin,name='quetion-to-admin'),
path('submit_question/',views.submit_question,name='submit_question'),
path('forgot-password/',views.forgot_password,name='forgot-password'),
path('verify-otp/',views.verify_otp,name='verify-otp'),
path('new-password/',views.new_password,name='new-password'),














]