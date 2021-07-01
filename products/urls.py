from django.urls    import path

from products.views import ExpertView, ProductDetailView, ProductReviewView, ProductView

urlpatterns = [
    path('', ProductView.as_view()),
    path('/<int:product_id>', ProductDetailView.as_view()),
    path('/expert', ExpertView.as_view()),
    path('/<int:product_id>/review', ProductReviewView.as_view())
]