from django.db.models import Q
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly
)
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveDestroyAPIView,
    RetrieveUpdateAPIView
)
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)

# Create your views here.
from .models import (
    Proparty,
    PropartyImage
)
from .serializers import (
    PropartyListSerializer,
    PropartyDetailSerializer,
    PropartyImageSerializer,
)
from .permissions import IsOwnerOrReadOnly
from .pagination import (
    PostLimitOffsetPagination,
    PostPageNumberPagination
)


class PropartyListAPIView(ListAPIView):
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'content', 'user__first_name']
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = PostPageNumberPagination  # PageNumberPagination
    serializer_class = PropartyListSerializer

    def get_queryset(self, *args, **kwargs):
        queryset_list = Proparty.objects.all()
        query = self.request.GET.get("q")
        print(query)
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(address__address__icontains=query)
            ).distinct()
        return queryset_list


class PropartyDetailAPIView(RetrieveAPIView):
    queryset = Proparty.objects.all()
    serializer_class = PropartyDetailSerializer
    lookup_field = 'id'
    permission_classes = [IsOwnerOrReadOnly]


class PropertyCreateAPIView(CreateAPIView):
    queryset = Proparty.objects.all()
    serializer_class = PropartyDetailSerializer
    permission_classes = [IsAuthenticated]


class PropertyDeleteAPIView(RetrieveDestroyAPIView):
    queryset = Proparty.objects.all()
    serializer_class = PropartyDetailSerializer
    lookup_field = 'id'
    permission_classes = [IsOwnerOrReadOnly]


class PropertyUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Proparty.objects.all()
    serializer_class = PropartyDetailSerializer
    lookup_field = 'id'
    permission_classes = [IsOwnerOrReadOnly]


class PropartyImageListAPIView(ListAPIView):
    queryset = PropartyImage.objects.all()
    serializer_class = PropartyImageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
