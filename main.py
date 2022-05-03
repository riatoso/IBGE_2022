# SISTEMA GERADOR DE TABELA DE CIDADES
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Ricardo Antonio Cardoso
# Created Date: Abr-2022
# version ='1.0'
# ---------------------------------------------------------------------------
import PySimpleGUI as sg
import gerador

if __name__ == "__main__":

    def populacao():
        sg.theme("DarkTeal12")
        layout = [
            [sg.Text(f"{40 * '--'}", size=45)],
            [sg.Text(" * Busca por população. Digite um valor de busca.", size=40)],
            [sg.Radio('Menor', 1, default=True, enable_events=True, key='menor'),
             sg.Radio('Maior', 1, enable_events=True, key='maior')],
            [sg.Input(key="populacao", size=15)],
            [sg.Text(f"{40 * '--'}", size=45)],
            [sg.Text("Nome do arquivo a ser gerado.", size=40)],
            [sg.Input(key="arquivo", size=35)],
            [sg.Text(f"{40 * '--'}", size=45)],
            [sg.Button('Gerar', size=10), sg.Button("Estado", size=10),
             sg.Button('Cidade', size=10)],
        ]
        return sg.Window('Busca por população.', size=(350, 260), icon="login.ico", layout=layout,
                         finalize=True)


    def busca_nome():
        sg.theme("DarkTeal12")
        layout = [
            [sg.Text(f"{40 * '--'}", size=45)],
            [sg.Text(" * Busca por nome de cidade.", size=40)],
            [sg.Input(key="nome_cidade", size=35)],
            [sg.Text(f"{40 * '--'}", size=45)],
            [sg.Text("Nome do arquivo a ser gerado.", size=40)],
            [sg.Input(key="arquivo", size=35)],
            [sg.Text(f"{40 * '--'}", size=45)],
            [sg.Button('Gerar', size=10), sg.Button("Voltar", size=10)],
        ]
        return sg.Window('Busca por cidade.', size=(350, 240), icon="login.ico", layout=layout, finalize=True)


    def busca_estado():
        sg.theme("DarkTeal12")
        estados = ('AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE',
                   'PI',
                   'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO')
        layout = [
            [sg.Text(f"{40 * '--'}", size=45)],
            [sg.Text(" * Busca por estado do Brasil. Selecione o estado.", size=40)],
            [sg.Listbox(values=estados, key="estd", default_values=['AC'], size=(13, 3))],
            [sg.Text(f"{40 * '--'}", size=45)],
            [sg.Text("Nome do arquivo a ser gerado.", size=40)],
            [sg.Input(key="arquivo", size=35)],
            [sg.Text(f"{40 * '--'}", size=45)],
            [sg.Button('Gerar', disabled=False, size=10), sg.Button("Voltar", size=10)],
        ]
        return sg.Window('Busca por estados.', size=(350, 270), icon="login.ico", layout=layout, finalize=True)


    def executa():
        janela1, janela2, janela3 = populacao(), None, None
        while True:
            window, events, values = sg.read_all_windows()
            if events == janela1 and sg.WINDOW_CLOSED:
                break
            if window == janela1 and events == "Cidade":
                janela1.hide()
                janela2 = busca_nome()
                continue
            if window == janela1 and events == "Estado":
                janela1.hide()
                janela3 = busca_estado()
                continue
            if window == janela1 and events == "Gerar":
                if values["populacao"] and values["arquivo"]:
                    pop_cidade = values["populacao"]

                    def milhao(num):
                        if len(num) < 3:
                            return num
                        if 3 < len(num) < 6:
                            return f'{num[:-3]}.{num[-3:]}'
                        if len(num) == 6:
                            return f"{num[0:3]}.{num[3:6]}"
                        if len(num) == 8:
                            return f"{num[0:2]}.{num[2:5]}.{num[5:8]}"
                        if len(num) == 9:
                            return f"{num[0:3]}.{num[3:6]}.{num[6:9]}"

                    try:
                        pop_cidade = int(pop_cidade)
                        gerapop = gerador.Cidades()
                        if values["menor"]:
                            sg.popup_no_border(f"População menor que {milhao(values['populacao'])} habitantes.\n"
                                               f"Arquivo a ser gerado {values['arquivo']}.xlsx",
                                               title="População", background_color="silver",
                                               button_color="gray")
                            gerapop.populacao_menor(pop_cidade, f"{values['arquivo']}.xlsx")
                            sg.popup_no_border("Gerado com sucesso.")
                            janela1["populacao"].update("")
                            janela1["arquivo"].update("")
                            continue
                        if values["maior"]:
                            sg.popup_no_border(f"População maior que {milhao(values['populacao'])} habitantes.\n"
                                               f"Arquivo a ser gerado {values['arquivo']}.xlsx",
                                               title="População", background_color="silver",
                                               button_color="gray")
                            gerapop.populacao_maior(pop_cidade, f"{values['arquivo']}.xlsx")
                            sg.popup_no_border("Gerado com sucesso.")
                            janela1["populacao"].update("")
                            janela1["arquivo"].update("")
                            continue
                    except:
                        sg.popup_no_border("Digite apenas numeros.")
                        janela1["populacao"].update("")
                        janela1["populacao"].set_focus()
                        continue
                elif values["arquivo"] and not values["populacao"]:
                    sg.popup_no_border("Digite um valor para populacao.")
                    janela1["populacao"].set_focus()
                    continue
                elif not values["arquivo"] and not values["populacao"]:
                    sg.popup_no_border("Digite um valor para populacao e o nome do arquivo a ser gerado.")
                    continue
                else:
                    sg.popup_no_border("Digite o nome do arquivo a ser gerado.")
                    janela1["populacao"].set_focus()
                    continue
            if window == janela2 and events == "Gerar":
                if values["arquivo"] and values["nome_cidade"]:
                    cidade = values["nome_cidade"]
                    cidade = cidade.title()
                    sg.popup_no_border(f"Voce digitou a cidade de {cidade}\n"
                                       f"O arquivo a ser gerado é {values['arquivo']}.xlsx",
                                       button_color="gray", background_color="silver")
                    geracidade = gerador.Cidades()
                    verifica = geracidade.cidade(f"{cidade}", f"{values['arquivo']}.xlsx")
                    if verifica == 0:
                        sg.popup_no_border("Cidade não encontrada.\n"
                                           "Arquivo não gerado.")
                        janela2["nome_cidade"].update("")
                        janela2["arquivo"].update("")
                        continue
                    else:
                        sg.popup_no_border("Gerado com sucesso.")
                        janela2["nome_cidade"].update("")
                        janela2["arquivo"].update("")
                        continue
                elif not values["arquivo"] and values["nome_cidade"]:
                    sg.popup_no_border("Digite o nome do arquivo a ser gerado.")
                    janela2["arquivo"].set_focus()
                    continue
                elif not values["nome_cidade"] and values["arquivo"]:
                    sg.popup_no_border("Digite o nome da cidade a ser pesquisada.")
                    janela2["nome_cidade"].set_focus()
                    continue
                else:
                    sg.popup_no_border("Digite o nome da cidade a ser pesquisada.\n"
                                       "E o nome do arquivo a ser gerado.", background_color="silver",
                                       button_color="gray")
                    continue
            if window == janela3 and events == "Gerar":
                if values["arquivo"]:
                    arquivo = f"{values['arquivo']}.xlsx"
                    estado = f"{values['estd'][0]}"
                    sg.popup_no_border(f"Voce digitou a estado de {estado}\n"
                                       f"O arquivo a ser gerado é {arquivo}", background_color="silver",
                                       button_color="gray")
                    geraestado = gerador.Cidades()
                    geraestado.estado(estado, arquivo)
                    sg.popup_no_border("Gerado com sucesso.")
                    janela3["arquivo"].update("")
                    continue
                elif not values["arquivo"]:
                    sg.popup_no_border("Digite o nome do arquivo a ser gerado.")
                    janela3["arquivo"].set_focus()
                    continue
            if window == janela2 and events == "Voltar":
                janela2.hide()
                janela1 = populacao()
                continue
            if window == janela3 and events == "Voltar":
                janela3.hide()
                janela1 = populacao()
                continue
            if window == janela1 or window == janela2 or window == janela3:
                if events == sg.WINDOW_CLOSED:
                    break


    executa()
