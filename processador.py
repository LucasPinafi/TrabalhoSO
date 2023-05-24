from typing import Dict, List
from processo import Processo
from settings import *

class Processador:
    def __init__(self, lista_processos: List[Processo]):
        self.filas: Dict[str, List[Processo]] = {'Q0': lista_processos, 'Q1': [], 'Q2': []}
        self.filaIO: List[Processo] = []
      
    def processar(self, tempo: int) -> None:
        if self.filas['Q0']:
            fila = 'Q0'
        elif self.filas['Q1']:
            fila = 'Q1'
        else:
            fila = 'Q2'
        
        processos = self.filas[fila]
        if not processos:
            return 
        processo = processos[0]
        processo.tempoProcessando += 1
        processo.burstFaltante -= 1
        
        if processo.burstFaltante == 0:
            # Mandar para a fila de IO
            if processo.numeroIO > 0:
                processo.fila = 'IO'
                processo.inicioIO = tempo
                self.filaIO.append(processo)
            # Processo terminou
            else:
                processo.fila = None
            processos.remove(processo)
        
        # Se Q0 ou Q1 devem ser passadas para a próxima fila
        if processo.tempoProcessando == FILAS[fila]:
            if fila == 'Q0':
                processo.fila = 'Q1'
                self.filas['Q0'].remove(processo)
                self.filas['Q1'].append(processo)
            elif fila == 'Q1':
                processo.fila = 'Q2'
                self.filas['Q1'].remove(processo)
                self.filas['Q2'].append(processo)
            processo.tempoProcessando = 0
            
        
    def IO(self, tempo: int) -> None:
        if self.filaIO:
            processo = self.filaIO[0]
            # Só pode começar a contar 1ms depois de entrar no IO
            if processo.inicioIO == tempo:
                return           
            processo.tempoIO += 1
            
            if processo.tempoIO == TEMPO_IO:
                processo.fila = 'Q0'
                processo.burstFaltante = processo.burstInicial
                processo.tempoIO = 0
                processo.tempoProcessando = 0
                processo.numeroIO -= 1
                self.filas['Q0'].append(processo)                      
                self.filaIO.remove(processo)
    
    def update(self, tempo: int) -> None:
        self.processar(tempo)
        self.IO(tempo)
        #print(self.filas)
    
    def get_processando(self) -> Processo | None:
        if fila := self.filas['Q0']:
            return fila[0]
        if fila := self.filas['Q1']:
            return fila[0]
        if fila := self.filas['Q2']:
            return fila[0]
        return None 
    
    def get_IO(self) -> Processo | None:
        if self.filaIO:
            return self.filaIO[0]
        return None
            