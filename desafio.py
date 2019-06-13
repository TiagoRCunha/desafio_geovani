from menus import menu_inicial, menu_pesquisa;
from ordenacao import bubbleSort, selectionSort, mergeSort;
from utils import myClear, myStop, carregarArquivo, fecharArquivo, contadorFuncionarios, IniciarTempo, tempodeExecucao;

# printa um menu de opções
def printMenu(menu):
    menu_lista = [];
    for i in menu.values():
        menu_lista.append(i);
    menuSort = bubbleSort(menu_lista);
    for opcao in menuSort:
        print(opcao);
# função auxiliar para evidar a repetição de codigo
def auxExecAcao(dados,funcao, var_busca, categoria):
    resultado, lista_posicoes = pesquisarLista(dados['dicionarios'], var_busca, categoria);
    myClear();
    if (resultado):
        funcao(dados['dicionarios'], var_busca, lista_posicoes, categoria);
    else:
        print('Nenhum nome, cargo ou órgão "{}" foi encontrado'.format(var_busca)+'\n');
    myStop(), myClear();

# Roda uma acao relacionada a cada opcao do menu
def executarAcao(acao, dados):
    if (acao == 1):
        print('Existem {:,} funcionários.'.format(dados['num_funcionarios'])+ '\n');
        myStop(), myClear();
    elif (acao == 2 or acao == 5 or acao == 6 or acao == 7):
        var_busca, categoria = prepararPesquisa();
        if (var_busca == 'stop'):
            myClear();
            return;
        if (acao == 2):
            # Chamando a função auxiliar para reduzir o codigo
            auxExecAcao(dados, printResultadoPesquisa, var_busca, categoria);
        elif (acao == 5):
            auxExecAcao(dados, ordenarBubble, var_busca, categoria);
        elif (acao == 6):
            auxExecAcao(dados, ordenarSelected, var_busca, categoria);
        elif (acao == 7):
            auxExecAcao(dados, ordenarMerge, var_busca, categoria);
    elif (acao == 3):
        print('A média salarial dos funcionários é de R$ {:,}'.format(dados['media_salarios'])+'\n');
        myStop(), myClear();
    elif (acao == 4):
        print('O maior salário encontrado é de R$ {:,}'.format(dados['maior_salario'])+'\n');
        myStop(), myClear();

# roda o menu infinitamente ate o usuario escolher a opcao para sair do programa
def rodarMenu(dados_arquivo):
    while (True):
        myClear();
        printMenu(menu_inicial);
        opcao = int(input('\nOpção: '));
        if (opcao >= 1 and opcao <= 7):
            myClear();
            executarAcao(opcao, dados_arquivo);
        elif (opcao == 8):
            myClear();
            print('Saindo do programa.');
            break;

def prepararPesquisa():
    while (True):
        myClear();
        printMenu(menu_pesquisa);
        opcao = int(input('\nOpção: '));

        if (opcao >= 1 and opcao <= 4):
            myClear();
            while (opcao != 4):
                print("\nColocar no mínimo nome e sobrenome!\n");
                if (opcao == 1):
                    var_busca = input('Qual o nome que deseja proucurar:\n').upper();
                    chave_dicionario = 'nome';
                    return var_busca, chave_dicionario;
                elif (opcao == 2):
                    var_busca = input('Qual o cargo que deseja proucurar:\n').upper();
                    chave_dicionario = 'cargo';
                    return var_busca, chave_dicionario;
                elif (opcao == 3):
                    var_busca = input('Qual o órgao que deseja proucurar:\n').upper();
                    chave_dicionario = 'órgão';
                    return var_busca, chave_dicionario;
            myClear();
            return 'stop', 'stop';

def pesquisarLista(lista_dicionarios, valor_busca, chave):
    index = 0;
    lista_posicoes = [];

    for dicionario in lista_dicionarios:
        if (valor_busca in dicionario[chave]):
            lista_posicoes.append(index);
        index += 1;
    if (len(lista_posicoes) > 0):
        return True, lista_posicoes;
    return False;

# Printa o resultado da pesquisa de nome, órgaos ou cargo
def printResultadoPesquisa(lista_funcionarios, valor_proucurado, resultado, categoria):
    num_resultados = len(resultado);
    if (categoria == 'nome'): # Pesquisar por nome e mostrar informações do funcionário
        print('{:,} funcionários com o nome "{}":\n'.format(num_resultados, valor_proucurado));
        for index in range(num_resultados):
            for chave, valor in lista_funcionarios[resultado[index]].items():
                chave = chave.replace('_', ' ').title();
                print(chave + ':', valor);
    elif (categoria == 'cargo'): # Pesquisar um cargo e mostrar todos os funcionários dele
        print('{:,} funcionários trabalham como "{}":\n'.format(num_resultados, valor_proucurado));
        for index in range(num_resultados):
            print(lista_funcionarios[resultado[index]]['nome']);
    else:
        print('{:,} funcionários trabalham no órgão "{}":\n'.format(num_resultados, valor_proucurado));

def ordenarBubble(lista_funcionarios, valor_proucurado, resultado, categoria):
    num_resultados = len(resultado);
    if (categoria == 'nome'): # Pesquisar por nome e mostrar informações do funcionário
        print('{:,} funcionários com o nome "{}":\n'.format(num_resultados, valor_proucurado));
        lista = [];
        IniciarTempo();
        for index in range(num_resultados):
            lista.append(lista_funcionarios[resultado[index]]['nome'])
            # Inserção do bubble
        for nome in bubbleSort(lista):
            print(nome);
        tempodeExecucao();
    elif (categoria == 'cargo'): # Pesquisar um cargo e mostrar todos os funcionários dele
        print('{:,} funcionários trabalham como "{}":\n'.format(num_resultados, valor_proucurado));
        lista = [];
        IniciarTempo();
        for index in range(num_resultados):
            lista.append(lista_funcionarios[resultado[index]]['nome'])
            # Inserão do bubble
        for nome in bubbleSort(lista):
            print(nome);
        tempodeExecucao();
    else:
        print('{:,} funcionários trabalham no órgão "{}":\n'.format(num_resultados, valor_proucurado));

def ordenarSelected(lista_funcionarios, valor_proucurado, resultado, categoria):
    num_resultados = len(resultado);
    if (categoria == 'nome'): # Pesquisar por nome e mostrar informações do funcionário
        print('{:,} funcionários com o nome "{}":\n'.format(num_resultados, valor_proucurado));
        lista = [];
        IniciarTempo();
        for index in range(num_resultados):
            lista.append(lista_funcionarios[resultado[index]]['nome'])
        for nome in selectionSort(lista):
            print(nome);
        tempodeExecucao();
    elif (categoria == 'cargo'): # Pesquisar um cargo e mostrar todos os funcionários dele
        print('{:,} funcionários trabalham como "{}":\n'.format(num_resultados, valor_proucurado));
        lista = [];
        IniciarTempo();
        for index in range(num_resultados):
            lista.append(lista_funcionarios[resultado[index]]['nome'])
        for nome in selectionSort(lista):
            print(nome);
        tempodeExecucao();
    else:
        print('{:,} funcionários trabalham no órgão "{}":\n'.format(num_resultados, valor_proucurado));

def ordenarMerge(lista_funcionarios, valor_proucurado, resultado, categoria):
    num_resultados = len(resultado);
    if (categoria == 'nome'): # Pesquisar por nome e mostrar informações do funcionário
        print('{:,} funcionários com o nome "{}":\n'.format(num_resultados, valor_proucurado));
        lista = [];
        IniciarTempo();
        for index in range(num_resultados):
            lista.append(lista_funcionarios[resultado[index]]['nome'])
        for nome in mergeSort(lista):
            print(nome);
        tempodeExecucao();
    elif (categoria == 'cargo'): # Pesquisar um cargo e mostrar todos os funcionários dele
        print('{:,} funcionários trabalham como "{}":\n'.format(num_resultados, valor_proucurado));
        lista = [];
        IniciarTempo();
        for index in range(num_resultados):
            lista.append(lista_funcionarios[resultado[index]]['nome'])
        for nome in mergeSort(lista):
            print(nome);
        tempodeExecucao();
    else:
        print('{:,} funcionários trabalham no órgão "{}":\n'.format(num_resultados, valor_proucurado));

def criarDicionario():
    arquivo = carregarArquivo();
    lista_dic_funcionarios = [];

    for linha in arquivo:
        linha = linha.replace('\n', '');  # remove quebra de linha do documento
        lista_linha = linha.split(';');   # separa a cada ocorrencia de ';'
        lista_dic_funcionarios.append({   # dicionario dentro da lista
            'nome': lista_linha[0],
            'cargo': lista_linha[1],
            'órgão': lista_linha[2],
            'remuneracao_do_mês': lista_linha[3],
            'ferias_e_13_salário': lista_linha[4],
            'pagamentos_eventuais': lista_linha[5],
            'licença_prêmio_indenizada': lista_linha[6],
            'abono_permanêncica_e_outras_indenizações': lista_linha[7],
            'redutor_salarial': lista_linha[8],
            'total_líquido': lista_linha[9]
        });
    fecharArquivo(arquivo);     # chama a função fecharArquivo()
    lista_dic_funcionarios.pop(0);  #remove a primeira linha do documento
    return lista_dic_funcionarios;

def pesquisaSalarios(lista_dicionarios, num_funcionarios):
    soma_salarios = 0;
    maior_salario = 0;

    for pessoa in lista_dicionarios:
        # Troca ',' por '.', assim pode ser transformado para float
        salario_atual = float(pessoa['total_líquido'].replace(',', '.'));
        if (salario_atual > maior_salario): # Pega o maior salario
            maior_salario = salario_atual;
        soma_salarios += salario_atual;
    # Media arredondada
    media_salarios = round(soma_salarios / num_funcionarios, 2);
    return media_salarios, maior_salario;

################################################### Main:

dicionarios = criarDicionario();
contagemFuncionarios = contadorFuncionarios(dicionarios);
mediaSalarios, maiorSalario = pesquisaSalarios(dicionarios, contagemFuncionarios);

informacoes = {
    'num_funcionarios': contagemFuncionarios,
    'media_salarios': mediaSalarios,
    'maior_salario': maiorSalario,
    'dicionarios': dicionarios
}

rodarMenu(informacoes); #primeira ação a ser execultada 