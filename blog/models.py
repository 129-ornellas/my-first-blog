from django.conf import settings
from django.db import models
from django.utils import timezone

# Todas as linhas começando com from ou import são linhas que adicionam pedaços de outros arquivos. Então ao invés de copiar e colar as 
# mesmas coisas em cada arquivo, podemos incluir algumas partes com from... import ....

# class Post(models.Model): - esta linha define o nosso modelo (é um objeto).

# class é uma palavra-chave especial que indica que estamos definindo um objeto.
# Post é o nome do nosso modelo. Nós podemos dar um nome diferente (mas precisamos evitar caracteres especiais e espaços em branco). 
# Sempre inicie o nome de uma classe com uma letra em maiúsculo.
# models.Model significa que o Post é um modelo de Django, então o Django sabe que ele deve ser salvo no banco de dados.
# Agora definiremos as propriedades comentadas acima: title, text, created_date, published_date e author. Para fazer isso, é necessário definir um tipo para cada campo 
# (É um texto? Um número? Uma data? Uma relação com outro objeto, por exemplo, um usuário?)

# models.CharField - é assim que definimos um texto com um número limitado de caracteres.
# models.TextField - este campo é para textos sem um limite fixo. Parece ideal para o conteúdo de um blog, né?
# models.DateTimeField - este é uma data e hora.
# models.ForeignKey - este é um link para outro modelo.


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

#  E def publish(self):? Esse é justamente o método publish de que falamos anteriormente.
#  def significa que se trata de uma função/método e que publish é seu nome. 
#  Você pode mudar o nome do método, se quiser. A regra para nomes é sempre usar letras minúsculas e no lugar dos espaços em branco, usar o caractere sublinhado (_). 
#  Por exemplo, um método que calcula o preço médio poderia se chamar calculate_average_price (do inglês, calcular_preco_medio).
#  Métodos muitas vezes retornam (return) algo. Um exemplo disto é o método __str__. Neste caso, quando chamarmos __str__(), obteremos um texto (string) com o título do Post.

#  Lembre-se também de que tanto def publish(self): quanto def __str__(self): são endentados para dentro da classe. 
#  E porque Python é sensível a espaços em branco, precisamos endentar todos os nossos métodos para dentro da classe. 
#  Caso contrário, os métodos não pertencerão à classe e você poderá obter um comportamento inesperado.
