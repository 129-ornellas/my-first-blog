from django.shortcuts import render
from .models import Post
from django.utils import timezone
# O ponto antes de models significa diretório atual ou aplicativo atual. 
# Tanto views.py como models.py estão no mesmo diretório. 
# Isto significa que podemos usar . e o nome do arquivo (sem py). 
# Em seguida, importamos o nome do modelo (Post).

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
    
    # o posts virou nosso queryset... como se a gente desse um nome pra ele, 
    # ou seja, podemos criar uma variável para um comando DB?
    # o queryset é o nome usado para a linha de comando que faz pesquisa no banco de dados? 