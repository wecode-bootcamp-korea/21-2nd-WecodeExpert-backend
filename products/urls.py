from django.urls    import path

from products.views import ExpertView, ProductDetailView, ProductView

urlpatterns = [
    path('', ProductView.as_view()),
    path('/<int:product_id>', ProductDetailView.as_view()),
    path('/expert', ExpertView.as_view())
]