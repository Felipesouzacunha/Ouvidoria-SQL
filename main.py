from operacoesbd import *
from metodos import *

conexao = abrirBancoDados('localhost', 'root', '12345', 'ouvidoria')
manifestacao = []
tipo = ''
opcao = 0
while opcao != 8:
    print()
    print(f'1) Listagem das Manifestações  {"2) Listagem de Manifestações por Tipo":^62}')
    print(f'3) Criar uma nova Manifestação  {"4) Exibir quantidade de manifestações": ^60}')
    print(f'5) Pesquisar uma manifestação por código {"6) Alterar o Título e Descrição de uma Manifestação": ^55} ')
    print(f'7) Excluir uma Manifestação pelo Código {" 8) Sair do Sistema.": ^25}')
    opcao = int(input('Qual a sua opção? '))

    if opcao == 1:
        manifestacoes = listarTudo(conexao)
        if len(manifestacoes) == 0:
            print('Não há manifestações!')
        else:
            for manifestacao in manifestacoes:
                print(f'Codigo: {manifestacao[0]} - Nome: {manifestacao[1]} - Titulo: {manifestacao[2]} - '
                      f'Descrição da manifestação: {manifestacao[3]} - Tipo da manifestação: {manifestacao[4]}')

    elif opcao == 2:
        print('Listagem de manifestação por tipo: ')
        opcaodelistagem = int(input('1)Elogios\n2)Sugestão\n3)Reclamações\nEscolha a opção desejada: '))
        manifestacoes = listarPortipo(conexao, opcaodelistagem)
        if opcaodelistagem == 1:
            if len(manifestacoes) > 0:
                print('Listagem de Elogios: ')
                for manifestacao in manifestacoes:
                    print(f'Codigo: {manifestacao[0]} - Nome: {manifestacao[1]} - Titulo: {manifestacao[2]} - '
                          f'Descrição da manifestação: {manifestacao[3]}')
            else:
                print('Não há Elogios!')

        elif opcaodelistagem == 2:
            manifestacoes = listarPortipo(conexao, opcaodelistagem)
            if len(manifestacoes) > 0:
                print('Listagem de Sugestões: ')
                for manifestacao in manifestacoes:
                    print(f'Codigo: {manifestacao[0]} - Nome: {manifestacao[1]} - Titulo: {manifestacao[2]} - '
                          f'Descrição da manifestação: {manifestacao[3]}')
            else:
                print('Não há Sugestões!')

        elif opcaodelistagem == 3:
            manifestacoes = listarPortipo(conexao, opcaodelistagem)
            if len(manifestacoes) > 0:
                print('Listagem de Reclamações: ')
                for manifestacao in manifestacoes:
                    print(f'Codigo: {manifestacao[0]} - Nome: {manifestacao[1]} - Titulo: {manifestacao[2]} - '
                          f'Descrição da manifestação: {manifestacao[3]}')
            else:
                print('Não há Reclamações! ')

    elif opcao == 3:
        print('1) Elogio')
        print('2) Sugestão')
        print('3) Reclamão')
        opcaotipo = 0
        while opcaotipo != 1 and opcaotipo != 2 and opcaotipo != 3:
            opcaotipo = int(input('Que tipo de manifestção quer fazer?'))
            if opcaotipo == 1:
                tipo = 'Elogio'
            elif opcaotipo == 2:
                tipo = 'Sugestão'
            elif opcaotipo == 3:
                tipo = 'Reclamação'
            else:
                print('Opção inválida!')
        autor = input('Digite seu nome:')
        titulo = input('Titulo para a sua manifetação: ')
        descricao = input('Descreve aqui a sua manifetação: ')
        criarManifestacao(conexao, autor, titulo, descricao, tipo)
        print('Comentario cadastrado com sucesso!')

    elif opcao == 4:
        sqlcontagem = 'select count(*) from manifestacao'
        resultado = contagemdeManifestacoes(conexao)
        print('Quantidade de manifestações cadastradas: ')
        if resultado > 0:
            print(f'Há {resultado} manifestações cadastradas')
        else:
            print('Não há manifestações!')

    elif opcao == 5:
        codigo = input('Digite o codigo de manifestação que deseja pesquisar: ')
        manifestacao = pesquisaPorcondiog(conexao, codigo)
        if len(manifestacao) == 0:
            print('Codigo inválido!')
        else:
            for elementos in manifestacao:
                print(f'Nome: {elementos[1]} - Titulo: {elementos[2]} - Descrição da manifestação: '
                      f'{elementos[3]} - Tipo da manifestação: {elementos[4]}')
    elif opcao == 6:
        codigo = input('Digite o codigo de manifestação que deseja alterar: ')
        print()
        resultado = checagemdeManifestacao(conexao, codigo)
        if resultado == 0:
            print('Manifetação não existente!')
        else:
            novotitulo = input('Novo titulo: ')
            novadescricao = input('Nova descrição: ')
            alterarManifestacao(conexao, codigo, novotitulo, novadescricao)
            print('Manifestação atualizada com sucesso! ')

    elif opcao == 7:
        codigo = input('Digite o codigo da manifestação que deseja excluir: ')
        resultado = checagemdeManifestacao(conexao, codigo)
        if resultado[0][0] == 0:
            print('Manifestação não existente!')
        else:
            sqlexcluir = 'delete from manifestacao where codigo = %s'
            valores = [codigo]
            excluirBancoDados(conexao, sqlexcluir, valores)
            print('Manifestação excluida com sucesso!')

    elif opcao > 8:
        print('Opção inválida!')

print('Obrigrado por usar a nossa ouvidoria!')
print('Saindo do sistema...')
encerrarBancoDados(conexao)
