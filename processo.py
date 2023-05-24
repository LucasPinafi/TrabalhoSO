from __future__ import annotations

class Processo:
    def __init__(self,nomeProcesso: str, burstInicial: int, numeroIO: int):
        self.nomeProcesso = nomeProcesso
        self.burstInicial = burstInicial
        self.burstFaltante = burstInicial
        self.numeroIO = numeroIO
        self.fila: str | None = 'Q0'
        self.tempoProcessando: int = 0
        self.tempoIO: int = 0
        self.inicioIO: int = 0
        
    def __repr__(self) -> str:
        return f'{self.nomeProcesso}: \n\tBurst Faltante:{self.burstFaltante}\n\tTempo Processando: {self.tempoProcessando}' \
            f'\n\tFila: {self.fila}\n' 
    
    def __eq__(self, __value: Processo) -> bool:
        return self.nomeProcesso == __value.nomeProcesso
    