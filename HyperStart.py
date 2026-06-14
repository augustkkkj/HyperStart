"""
HyperStart.py
Script simples para abrir o navegador com abas específicas, iniciar programas
e organizar as janelas na tela. Comentários didáticos explicam cada etapa.
"""

import webbrowser
import os
import time
import pyautogui
import pygetwindow as gw


class OpenSystem:
   """Classe responsável por abrir aplicações e organizar janelas.

   Métodos:
   - organizar_janelas: posiciona o VS Code e o navegador lado a lado.
   - abrir_navegador_abas: abre uma lista de sites em abas do Brave.
   - abrir_programas: inicia o VS Code usando o caminho do executável.
   - iniciar: fluxo principal que chama os outros métodos na ordem correta.
   """

   def organizar_janelas(self):
      """Organiza as janelas na tela para facilitar o trabalho.

      Passos:
      1. Obtém o tamanho da tela e calcula metade da largura.
      2. Encontra a janela do Visual Studio Code e a posiciona à esquerda.
      3. Encontra a janela do Brave e a posiciona à direita.
      """

      # Pega a resolução atual da tela (largura, altura)
      largura_tela, altura_tela = pyautogui.size()

      # Calcula metade da largura para dividir a tela em duas colunas
      metade_largura = largura_tela // 2

      # Pequena pausa para garantir que janelas abertas tenham tempo de aparecer
      time.sleep(2)

      # Procura por janelas cujo título contenha 'Visual Studio Code'
      janelas_vscode = gw.getWindowsWithTitle('Visual Studio Code')
      if len(janelas_vscode) > 0:
         vscode = janelas_vscode[0]

         # Garante que a janela não esteja minimizada/maximizada antes de mover
         vscode.restore()

         # Redimensiona e move o VS Code para a metade esquerda da tela
         vscode.resizeTo(metade_largura, altura_tela)
         vscode.moveTo(0, 0)

         # Agora procura pela janela do navegador Brave
         janelas_brave = gw.getWindowsWithTitle('Brave')
         if len(janelas_brave) > 0:
            brave = janelas_brave[0]

            # Informação para o usuário sobre qual janela está sendo organizada
            print(f"Organizando a janela: {brave.title}")

            # Se o Brave estiver maximizado, restaura antes de redimensionar
            if brave.isMaximized:
               brave.restore()
               time.sleep(1)

            # Restaura novamente (caso esteja minimizado) e aguarda
            brave.restore()
            time.sleep(1)

            # Redimensiona e move o Brave para a metade direita da tela
            brave.resizeTo(metade_largura, altura_tela)
            brave.moveTo(metade_largura, 0)

            # Pausa final para dar tempo da GUI aplicar as mudanças
            time.sleep(1)


   def abrir_navegador_abas(self):
      """Abre o navegador Brave e carrega uma lista de sites em abas.

      Observações:
      - `webbrowser.register` associa um caminho específico ao nome 'brave'.
      - O loop abre cada site em sequência, com uma pequena pausa entre eles.
      """

      # Caminho para o executável do Brave no Windows (ajuste se necessário)
      navegador = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

      # Lista de sites que queremos abrir como abas iniciais
      sites = [
         'https://www.youtube.com/',
         'https://music.youtube.com/',
         'https://www.udemy.com/course/python-rpa-e-excel-aprenda-automatizar-processos-e-planilhas/learn/lecture/39218898?start=870#content'
      ]

      # Registra o navegador para que possamos abri-lo pelo nome 'brave'
      webbrowser.register('brave', None, webbrowser.BackgroundBrowser(navegador))

      # Abre cada site em uma nova aba do Brave, com pequena pausa entre aberturas
      for site in sites:
         webbrowser.get('brave').open(site)
         time.sleep(3)


   def abrir_programas(self):
      """Inicia programas locais. Aqui, abre o Visual Studio Code.

      Usa `os.startfile` que delega ao Windows iniciar o executável.
      """

      # Caminho para o executável do VS Code (ajuste se instalado em outro local)
      vs_code = r"C:\Users\leite\AppData\Local\Programs\Microsoft VS Code\Code.exe"

      # Abre o VS Code
      os.startfile(vs_code)


   def iniciar(self):
      """Fluxo principal: abre o navegador, inicia programas e organiza janelas."""

      # 1) Abre as abas do navegador
      self.abrir_navegador_abas()

      # 2) Abre o VS Code
      self.abrir_programas()

      # 3) Organiza as janelas já abertas na tela
      self.organizar_janelas()


# Instancia a classe e executa o fluxo principal
sistem = OpenSystem()

# Chamada final que inicia todo o processo
sistem.iniciar()


