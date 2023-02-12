from datetime import date

class Livro:
    def __init__(self, nome, autor, data_lancamento, preco):
        self._nome = nome
        self._autor = autor
        self._data_lancamento = data_lancamento
        self._preco = preco


    @property
    def nome(self):
        return self._nome


    @property
    def autor(self):
        return self._autor


    @property
    def preco(self):
        return self._preco


    def tamanho_nome(self):
        """
        Função usada para categorizar o tamanho do livro, em Pequeno (até 5 palavras) ou Grande (acima de 5)
        """
        nome_completo = self.nome.strip().split(' ')
        nome_tamanho = len(nome_completo)
        if nome_tamanho < 5:
            return 'Pequeno'
        elif nome_tamanho >= 5:
            return 'Grande'


    def anos_lancamento(self):
        """
        Função para calcular quantos anos o livro tem desde que foi lançado.
        """
        data_lancamento_quebrada = self._data_lancamento.split('/')
        ano_lancamento = data_lancamento_quebrada[-1]
        ano_atual = date.today().year
        return ano_atual - int(ano_lancamento)

    
    def sobrenome_autor(self):
        """
        Função para separar e retornar o sobrenome do autor do livro
        """
        nome_autor_completo = self.autor.strip()
        nome_autor_quebrado = nome_autor_completo.split(' ')
        return nome_autor_quebrado[-1]
    

    def _eh_best_seller(self):
        """
        Função que reune os sobrenomes dos autores best-sellers e retorna aqueles cujo valor do livro é menor 
        que R$50,00.
        """
        sobrenomes = ['Silva', 'Gomes', 'Pires', 'Peixoto', 'Costa', 'Melo', 'Moreira', 'Paes']
        return self._preco <= 50 and (self.sobrenome_autor() in sobrenomes)
            

    def desconto_preco(self):
        """
        Função usada pela livraria para aplicar um desconto nos livros com preço acima de R$100,00.
        """
        if self._preco >= 100:
            desconto = self._preco * 0.1
            self._preco = self._preco - desconto
        

    def aumentar_preco(self):
        """
        Função para aumentar o preço dos livros que se encaixam na função _eh_best_seller
        """
        if self._eh_best_seller():
            aumento = self._preco * 0.5
            self._preco = self._preco + aumento
        elif self._preco > 50:
            raise Exception('O preço ja é muito alto para aumentar.')
        return self._preco


    def __str__(self):
        return f'Livro({self._nome}, {self._autor}, {self._data_lancamento}, {self._preco})'
