# SISTEMA GERADOR DE TABELA DE CIDADES
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Ricardo Antonio Cardoso
# Created Date: Abr-2022
# version ='1.0'
# ---------------------------------------------------------------------------

import pandas as pd


class Cidades:
    def __init__(self):
        self.lista_cidades = pd.read_excel("cidades.xlsx")
        self.lista_dt = pd.DataFrame(self.lista_cidades)
        self.lista_populada = pd.DataFrame()

    def populacao_maior(self, total, arquivo):
        lista_populacao = self.lista_dt[["UF", "MUNICIPIO", "POPULACAO"]]
        lista_pop = pd.DataFrame(lista_populacao)
        for i, row in lista_pop.iterrows():
            try:
                row[2] = int(row[2])
                if row[2] >= total:
                    df_novo = pd.DataFrame({'MUNICIPIO': [row[1]], "UF": [row[0]],
                                            'POPULACAO': [row[2]]})  # CRIA O DATAFRAME SEMPRE COM COLCHETES
                    self.lista_populada = pd.concat([self.lista_populada, df_novo])  # CRIA O DATAFRAME CONCATENADO
            except:
                continue
        self.lista_populada.to_excel(arquivo, index=False)

    def populacao_menor(self, total, arquivo):
        lista_populacao = self.lista_dt[["UF", "MUNICIPIO", "POPULACAO"]]
        lista_pop = pd.DataFrame(lista_populacao)
        for i, row in lista_pop.iterrows():
            try:
                row[2] = int(row[2])
                if row[2] <= total:
                    df_novo = pd.DataFrame({'MUNICIPIO': [row[1]], "UF": [row[0]],
                                            'POPULACAO': [row[2]]})  # CRIA O DATAFRAME SEMPRE COM COLCHETES
                    self.lista_populada = pd.concat([self.lista_populada, df_novo])  # CRIA O DATAFRAME CONCATENADO
            except:
                continue
        self.lista_populada.to_excel(arquivo, index=False)

    def cidade(self, nome, arquivo):
        verifica = 0
        lista_cidade = self.lista_dt[["UF", "MUNICIPIO", "POPULACAO"]]
        lista_pop = pd.DataFrame(lista_cidade)
        for i, row in lista_pop.iterrows():
            if row[1] == nome:
                df_novo = pd.DataFrame({'MUNICIPIO': [row[1]], "UF": [row[0]],
                                        'POPULACAO': [row[2]]})  # CRIA O DATAFRAME SEMPRE COM COLCHETES
                self.lista_populada = pd.concat([self.lista_populada, df_novo])  # CRIA O DATAFRAME CONCATENADO
                verifica = 1
        if verifica == 1:
            return self.lista_populada.to_excel(arquivo, index=False)
        else:
            return 0

    def estado(self, estado, arquivo):
        lista_cidade = self.lista_dt[["UF", "MUNICIPIO", "POPULACAO"]]
        lista_pop = pd.DataFrame(lista_cidade)
        for i, row in lista_pop.iterrows():
            if row[0] == estado:
                df_novo = pd.DataFrame({'MUNICIPIO': [row[1]], "UF": [row[0]],
                                        'POPULACAO': [row[2]]})  # CRIA O DATAFRAME SEMPRE COM COLCHETES
                self.lista_populada = pd.concat([self.lista_populada, df_novo])  # CRIA O DATAFRAME CONCATENADO

        self.lista_populada.to_excel(arquivo, index=False)

