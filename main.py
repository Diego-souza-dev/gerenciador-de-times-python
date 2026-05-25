# gerenciador-de-times-python
Gerenciamento back end de times de games online


import os

times = [
            {'nome': 'Legends Online', 'categoria': 'RPG', 'atividade':True},
            {'nome': 'Transformice em Rato', 'categoria': 'RPG', 'atividade':True},
            {'nome': 'Cs 1.6', 'categoria': 'FPS', 'atividade':True},
            {'nome': 'Minimundos', 'categoria': 'RP', 'atividade':False}
        ]

def exibir_nome_da_liga(): 
    '''Essa função serve para exibir o nome da liga'''
    print("""

░█─── ─▀─ █▀▀▀ █▀▀█ 　 █▀▀▄ █▀▀█ █▀▀ 　 ░█▀▄▀█ █▀▀█ █▀▀▀ █▀▀█ █▀▀ 
░█─── ▀█▀ █─▀█ █▄▄█ 　 █──█ █──█ ▀▀█ 　 ░█░█░█ █▄▄█ █─▀█ █──█ ▀▀█ 
░█▄▄█ ▀▀▀ ▀▀▀▀ ▀──▀ 　 ▀▀▀─ ▀▀▀▀ ▀▀▀ 　 ░█──░█ ▀──▀ ▀▀▀▀ ▀▀▀▀ ▀▀▀
      
""")

def exibir_opcoes():
    '''Essa função serve para exibir as opções do menu principal'''
    print('1. Cadastrar time')
    print('2. Listar times')
    print('3. Ativar ou desativar um time')
    print('4. Sair\n')

def encerrando_operacao():
    '''Essa função serve para encerrar a operação do aplicativo'''
    exibir_subtitulos('Encerrando operação...')

def voltar_ao_menu_principal():
    '''Essa função serve para voltar a operação para o menu principal'''
    input('\nPressione uma tecla para voltar ao menu principal ')
    main()

def opcao_invalida():
    '''Essa função serve para quando o usuario inserir uma opção inválida'''
    print('Opção Inválida chef\n')
    voltar_ao_menu_principal()

def exibir_subtitulos(texto):
    '''Essa função serve para exibir um texto conhecido como subtitulo'''
    os.system('cls')
    linha = '-' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_time():
    '''Essa função serve para cadastrar um nome time no sistema'''
    exibir_subtitulos('Cadastre seu novo time')
    nome_do_time = input('Coloque aqui o nome do time que deseja cadastrar: ')
    categoria_do_time = input(f'Coloque aqui a categoria do time {nome_do_time} (exemplo: RPG, RP, FPS...) ')
    dados_do_time = {'nome': nome_do_time, 'categoria': categoria_do_time, 'atividade': False }
    times.append(dados_do_time)
    print(f'O time {nome_do_time} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()
 
def ver_lista_de_times():
    '''Essa função serve para exibir a lista dos times que estão cadastrados no sistema'''
    exibir_subtitulos('Veja aqui a lista dos times cadastrados')

    print(f'{"Nome do Time".ljust(22)} | {"Categoria do Time".ljust(20)} | Status do Time\n ')
    for time in times:
        nome_do_time = time['nome']
        categoria_do_time = time['categoria']
        atividade_do_time = 'Ativo' if time ['atividade'] else 'Desativado'
        print(f'- {nome_do_time.ljust(20)} | {categoria_do_time.ljust(20)} | {atividade_do_time}')
    voltar_ao_menu_principal()

def ativar_ou_desativar_time():
    '''Essa funcão serve para alterar o status de atividade de times no sistema'''
    exibir_subtitulos('Ative ou desative seu time')
    nome_time = input('Coloque aqui o nome do time que deseja ativar ou desativar: ')
    time_encontrado = False
    for time in times:
        if time['nome'] == nome_time:
            time_encontrado = True
            time['atividade'] = not time['atividade']
            mensagem = f'O time {nome_time} foi ativado com sucesso!' if time['atividade'] else f'O time {nome_time} foi desativado com sucesso!'
            print(mensagem)
    if not time_encontrado:
        print('Time não encontrado nos nossos times cadastrados')

    voltar_ao_menu_principal()
    

def escolher_opcoes():
    '''Essa função serve para que o usuario escolha uma das opções do menu'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_time()
        elif opcao_escolhida == 2:
            ver_lista_de_times()
        elif opcao_escolhida == 3:
            ativar_ou_desativar_time()
        elif opcao_escolhida == 4:
            encerrando_operacao()
        else: 
            opcao_invalida()
    except: 
        opcao_invalida()

def main():
    '''Essa função serve para que o arquivo seja o principal arquivo do sistema'''
    os.system('cls')
    exibir_nome_da_liga()
    exibir_opcoes()
    escolher_opcoes()

if __name__=='__main__':
        main()
