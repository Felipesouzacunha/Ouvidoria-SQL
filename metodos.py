from operacoesbd import *

def listarTudo(conexao):
    sqlListar = 'select * from manifestacao'
    manifestacoes = listarBancoDados(conexao, sqlListar)
    print()
    return manifestacoes

def listarPortipo(conexao, opcaodelistagem):
    if opcaodelistagem == 1:
        sqlListar = "select * from manifestacao where tipo = 'Elogio'"
        manifestacoes = listarBancoDados(conexao, sqlListar)
        return manifestacoes

    if opcaodelistagem == 2:
        sqllistar = "select * from manifestacao where tipo = 'Sugestão'"
        manifestacoes = listarBancoDados(conexao, sqllistar)
        return manifestacoes

    if opcaodelistagem == 3:
        sqllistar = "select * from manifestacao where tipo = 'Reclamação'"
        manifestacoes = listarBancoDados(conexao, sqllistar)
        return manifestacoes
def criarManifestacao(conexao, autor, titulo, descricao, tipo):
    sqlinserir = 'insert into manifestacao (autor, titulo, descricao, tipo) values (%s, %s, %s, %s)'
    valores = [autor, titulo, descricao, tipo]
    insertNoBancoDados(conexao, sqlinserir, valores)

def contagemdeManifestacoes(conexao):
    sqlcontagem = 'select count(*) from manifestacao'
    resultado = listarBancoDados(conexao, sqlcontagem)
    return resultado[0][0]

def checagemdeManifestacao(conxao, codigo):
    sqlchecar = 'select count(*) from manifestacao where codigo = ' + codigo
    resultado = listarBancoDados(conxao, sqlchecar)
    return resultado[0][0]
def pesquisaPorcondiog(conexao, condigo):
    sqllistar = 'select * from manifestacao where codigo = ' + condigo
    manifestacao = listarBancoDados(conexao,sqllistar)
    return manifestacao

def alterarManifestacao(conexao, codigo, novotitulo, novadescricao):
    sqlalterar = 'update manifestacao set titulo = %s, descricao = %s where codigo = %s'
    valores = [novotitulo, novadescricao, codigo]
    atualizarBancoDados(conexao,sqlalterar, valores)

