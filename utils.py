import time;
import os;

# Conta quantos funcionários existem
def contadorFuncionarios(lista_dicionarios): 
    count = 0;
    for nome in lista_dicionarios:
        count += 1;
    return count;
    
def myClear():
    if (os.name == 'nt'):
        os.system('cls');
    else:
        os.system('clear');

def myStop():
    if (os.name == 'nt'):
        os.system('pause');
    else:
        input('Aperte Enter para continuar');

def carregarArquivo():
    arquivo = open('./remuneracao.txt', 'r');
    return arquivo;

def fecharArquivo(arquivo):
    arquivo.close();

def IniciarTempo():
    int(time.perf_counter());
def tempodeExecucao():
    # Cronometragem de tempo
    print('Seu tempo de execulção foi de : ', int(time.perf_counter()));