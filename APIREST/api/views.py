from rest_framework import generics, mixins
from APIREST.models import *
from .serializers import VentesSerializer, DepensesSerializer, PretsSerializer,UsersSerializer
from django.db.models import Q
from .permissions import IsOwnerOrReadOnly


# creation de ventes
class BlogVentesAPIView(generics.CreateAPIView):
    pass
    lookup_field = 'pk'
    serializer_class = VentesSerializer # represent la convertion en JSON
    permission_clases = [IsOwnerOrReadOnly]
    def get_queryset(self):
        return Ventes.objects.all()

    def perform_create(self, serializer):
        serializer.save(userid=self.request.user)    


# afficher tout les utilisateurs
class BlogVentesListAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    pass
    lookup_field = 'pk'
    serializer_class = VentesSerializer # represent la convertion en JSON
    # faire des rechercher d l'articl en fonctio du titre et du contenu
    def get_queryset(self):
        qs= Ventes.objects.all()
        query=self.request.GET.get("q")
        if query is not None:
            qs= qs.filter(Q(designation__icontains=query)|Q(prix__icontains=query)).distinct()
            return qs
        return Ventes.objects.all()
    def perform_create(self, serializer):
        serializer.save(userid=self.request.user)   
    # ajouter post
    def post(self,request, *args, **kwargs):
        return self.create(request, *args, **kwargs)  
        

#recuperation, mise à jour et suppression
class BlogVentesRudView(generics.RetrieveUpdateDestroyAPIView):
    pass
    lookup_field = 'pk'
    serializer_class = VentesSerializer # represent la convertion en JSON

    def get_queryset(self):
        return Ventes.objects.all()




 # creation depenses
class BlogDepensesAPIView(generics.CreateAPIView):
    pass
    lookup_field = 'pk'
    serializer_class = DepensesSerializer # represent la convertion en JSON
    permission_clases = [IsOwnerOrReadOnly]
    def get_queryset(self):
        return Depenses.objects.all()

    def perform_create(self, serializer):
        serializer.save(userid=self.request.user)    


# afficher tout les utilisateurs
class BlogDepensesListAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    pass
    lookup_field = 'pk'
    serializer_class = DepensesSerializer # represent la convertion en JSON
    # faire des rechercher d l'articl en fonctio du titre et du contenu
    def get_queryset(self):
        qs= Depenses.objects.all()
        query=self.request.GET.get("q")
        if query is not None:
            qs= qs.filter(Q(designation__icontains=query)|Q(prix__icontains=query)).distinct()
            return qs
        return Depenses.objects.all()
    def perform_create(self, serializer):
        serializer.save(userid=self.request.user)   
    # ajouter post
    def post(self,request, *args, **kwargs):
        return self.create(request, *args, **kwargs)  
        

#recuperation, mise à jour et suppression
class BlogDepensesRudView(generics.RetrieveUpdateDestroyAPIView):
    pass
    lookup_field = 'pk'
    serializer_class = DepensesSerializer # represent la convertion en JSON

    def get_queryset(self):
        return Depenses.objects.all()       


# Creation de la class prets
class BlogPretsAPIView(generics.CreateAPIView):
    pass
    lookup_field = 'pk'
    serializer_class = PretsSerializer # represent la convertion en JSON
    permission_clases = [IsOwnerOrReadOnly]
    def get_queryset(self):
        return Prets.objects.all()

    def perform_create(self, serializer):
        serializer.save(userid=self.request.user)    


# afficher tout les utilisateurs
class BlogPretsListAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    pass
    lookup_field = 'pk'
    serializer_class = PretsSerializer # represent la convertion en JSON
    # faire des rechercher d l'articl en fonctio du titre et du contenu
    def get_queryset(self):
        qs= Prets.objects.all()
        query=self.request.GET.get("q")
        if query is not None:
            qs= qs.filter(Q(nomclient__icontains=query)|Q(montant__icontains=query)).distinct()
            return qs
        return Prets.objects.all()
    def perform_create(self, serializer):
        serializer.save(userid=self.request.user)   
    # ajouter post
    def post(self,request, *args, **kwargs):
        return self.create(request, *args, **kwargs)  
        

#recuperation, mise à jour et suppression
class BlogPretsRudView(generics.RetrieveUpdateDestroyAPIView):
    pass
    lookup_field = 'pk'
    serializer_class = PretsSerializer # represent la convertion en JSON

    def get_queryset(self):
        return Prets.objects.all()         

# creation de Users
class BlogUsersAPIView(generics.CreateAPIView):
    pass
    lookup_field = 'pk'
    serializer_class = UsersSerializer # represent la convertion en JSON
    permission_clases = [IsOwnerOrReadOnly]
    def get_queryset(self):
        return Users.objects.all()

    def perform_create(self, serializer):
        serializer.save(userid=self.request.user)    


# afficher tout les utilisateurs
class BlogUsersListAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    pass
    lookup_field = 'pk'
    serializer_class = UsersSerializer # represent la convertion en JSON
    # faire des rechercher d l'articl en fonctio du titre et du contenu
    def get_queryset(self):
        qs= Users.objects.all()
        query=self.request.GET.get("q")
        if query is not None:
            qs= qs.filter(Q(nom__icontains=query)|Q(numero__icontains=query)).distinct()
            return qs
        return Users.objects.all()
    def perform_create(self, serializer):
        serializer.save(userid=self.request.user)   
    # ajouter post
    def post(self,request, *args, **kwargs):
        return self.create(request, *args, **kwargs)  
        

#recuperation, mise à jour et suppression
class BlogUsersRudView(generics.RetrieveUpdateDestroyAPIView):
    pass
    lookup_field = 'pk'
    serializer_class = UsersSerializer # represent la convertion en JSON

    def get_queryset(self):
        return Ventes.objects.all()
