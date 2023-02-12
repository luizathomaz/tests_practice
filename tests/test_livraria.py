from codigo.livraria import Livro
import pytest
from pytest import mark

class TestClass:
    def test_quando_anos_lancamento_recebe_13_01_2000_deve_retornar_23(self):
        #Given-Contexto:
        entrada = '13/03/2000'
        esperado = 23

        livro_teste = Livro('Teste', 'Autor Teste', entrada, 60)
        #When-Ação:
        resultado = livro_teste.anos_lancamento()

        assert resultado == esperado #Then-Desfecho
        

    def test_quando_sobrenome_autor_recebe_Lucas_Silva_deve_retornar_Silva(self):
        entrada = '  Lucas Silva  ' #Given
        esperado = 'Silva'

        lucas = Livro('Nome Teste', entrada, '11/11/2000', 30)
        resultado = lucas.sobrenome_autor() #When

        assert resultado == esperado

    
    def test_quando_desconto_preco_recebe_100_deve_retornar_90(self):
        entrada_preco = 100 #Given
        entrada_nome = 'O Nosso Tempo'
        esperado = 90

        livro_teste = Livro(entrada_nome, 'Autor Teste', '11/11/2015', entrada_preco)
        livro_teste.desconto_preco() #When
        resultado = livro_teste.preco

        assert resultado == esperado #Then


    @mark.aumentar_preco
    def test_quando_aumentar_preco_recebe_40_deve_retornar_60(self):
        entrada = 40 #Given
        esperado = 60

        livro_teste = Livro('Nome Teste', 'Pedro Paes', '11/11/2016', entrada) 
        resultado = livro_teste.aumentar_preco()#When

        assert resultado == esperado #Then

    
    @mark.aumentar_preco
    def test_quando_aumentar_preco_recebe_150_deve_retornar_excpetion(self):
        with pytest.raises(Exception):
            entrada = 150 #Given

            livro_teste = Livro('Nome Teste', 'Julia Costa', '11/11/2015', entrada) 
            resultado = livro_teste.aumentar_preco()#When

            assert resultado #Then


    def test_quando_tamanho_nome_recebe_5_deve_retornar_grande(self):
        entrada = 'O Gato de Nove Vidas'
        esperado = 'Grande'
        livro_teste = Livro(entrada, 'Autor Teste', '12/06/2020', 50)
        resultado = livro_teste.tamanho_nome()

        assert resultado == esperado


    def test_quando_tamanho_nome_recebe_3_deve_retornar_pequeno(self):
        entrada = 'A Pequena Baleia'
        esperado = 'Pequeno'
        livro_teste = Livro(entrada, 'Autor Teste', '12/06/2020', 50)
        resultado = livro_teste.tamanho_nome()

        assert resultado == esperado 