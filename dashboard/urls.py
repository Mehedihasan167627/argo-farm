from django.urls import path 

from .views import *

app_name="dashboard"

urlpatterns=[
    path("",DashBoardView.as_view(),name="dashboard"),
    path("add-banner-view/",AddBannerAreaView.as_view(),name="add-banner-view"),
    path("about-us/",AboutUsView.as_view(),name="about-us"),
    path("advertisment/",AdvertismentView.as_view(),name="advertisment"),
    path("bid-settings/",BidSettingView.as_view(),name="bid-settings"),
    path("home-page-section/",HomePageSectionView.as_view(),name="home-page-section"),
    path("language-setting/",LanguageSettingView.as_view(),name="language-setting"),
    path("manage-cupon/",ManageCuponView.as_view(),name="manage-cupon"),
    path("payment-gateway/",PaymentGatwayView.as_view(),name="payment-gateway"),
    path("privacy-policy/",PrivacyPolicyView.as_view(),name="privacy-policy"),
    path("product-review/",ProductReviewView.as_view(),name="product-review"),
    path("quality-setting/",QualitySettingView.as_view(),name="quality-setting"),
    path("seo-setting/",SEOSettingView.as_view(),name="seo-setting"),
    path("shipping-method/",ShippingMethodView.as_view(),name="shipping-method"),
    path("slider-setting/",SliderSettingView.as_view(),name="slider-setting"),
    path("sms-config/",SMSConfigView.as_view(),name="sms-config"),
    path("social-media/",SocialMediaView.as_view(),name="social-media"),
    path("subscriber/",SubscriberView.as_view(),name="subscriber") 
    
]
