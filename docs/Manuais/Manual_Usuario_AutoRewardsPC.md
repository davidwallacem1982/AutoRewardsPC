# Manual do Usuário - AutoRewardsPC

## 1. Introdução

Bem-vindo ao **AutoRewardsPC**! Este software foi desenvolvido para automatizar suas tarefas diárias no Microsoft Rewards, garantindo que você maximize seus pontos sem esforço. MCom uma interface moderna, segura e fácil de usar, o AutoRewardsPC simula a navegação humana para realizar pesquisas no Bing e coletar pontos.

## 2. Requisitos do Sistema

- Sistema Operacional: Windows 10 ou 11.
- Navegador: Microsoft Edge (instalado e logado na conta Microsoft).
- Resolução de Tela: Recomendado 1366x768 ou superior.
- Permissões: O software requer permissão para controlar o mouse e o teclado.

## 3. Instalação do Tesseract OCR (Obrigatório)

O sistema utiliza uma tecnologia de leitura de tela chamada Tesseract OCR. Ela é essencial para o funcionamento do robô.

1. **Passo 1: Baixe o instalador**
   Acesse o link oficial: https://github.com/UB-Mannheim/tesseract/wiki

2. **Passo 2: Instale o programa**
   - Execute o instalador e clique em "Next" até finalizar. Mantenha o caminho padrão de instalação:
     > "C:\Program Files\Tesseract-OCR"

3. **Passo 3: (Opcional) Caminho Personalizado**
   Se você instalou em outro local, precisará criar uma Variável de Ambiente chamada `TESSERACT_PATH` apontando para o arquivo `tesseract.exe`.

## 4. Instalação e Configuração do AutoRewardsPC

Como o software é portátil, o processo é extremamente simples:

1. Baixe o arquivo `AutoRewardsPC.exe` fornecido.
2. Coloque-o em uma pasta de sua preferência (ex: `Documentos\AutoRewards` ou Área de Trabalho).
3. (Opcional) Crie um atalho na Área de Trabalho para facilitar o acesso.

_Nota: Não é necessário instalar nada. O executável contém tudo o que você precisa._

## 5. Interface Principal

Ao abrir o programa, você encontrará uma interface limpa e intuitiva.

### Componentes:

- **Painel Esquerdo (Controles):**
  - **INICIAR:** O botão principal. Clique aqui para começar a ganhar pontos.
  - **Calibrar:** Abre o assistente de configuração de cliques.
  - **Importar / Exportar:** Ferramentas para salvar e restaurar suas calibrações.
  - **Ver Logs:** Abre o arquivo de registro de atividades.

## 6. Passo a Passo: Sua Primeira Automação

1. **Preparação:** Abra o Microsoft Edge e certifique-se de estar conectado à sua conta Microsoft Rewards.
2. **Limpeza:** Feche todas as janelas do Edge para evitar conflitos.
3. **Execução:** Abra o AutoRewardsPC (como Administrador, se possível).
4. **Ação:** Clique no botão verde INICIAR.
5. **Aguarde:** O robô abrirá o navegador e fará as pesquisas automaticamente.

**⚠️ Importante: Enquanto o robô estiver trabalhando, não mexa no mouse ou teclado.**

## 7. Calibração: O Segredo da Precisão

Se o robô estiver clicando fora dos botões, use a Calibração:

1. Clique no botão Calibrar.
2. Siga as instruções na tela.
3. Posicione o mouse sobre o local indicado e pressione ENTER.
4. Ao final, clique em Salvar Calibração.

## 8. Backup e Importação

- **Exportar:** Salva suas configurações em um arquivo `.json` na pasta backups.
- **Importar:** Restaura configurações de um arquivo salvo anteriormente.

## 9. Solução de Problemas

### "A aplicação já está em execução"

Verifique a Bandeja do Sistema (perto do relógio). O ícone pode estar lá. Clique com botão direito -> Sair.

### O robô clica no "vazio"

Execute o processo de Calibração novamente.

### Erro de "OCR não encontrado"

O sistema não encontrou o Tesseract. Verifique se você instalou o Tesseract OCR conforme a seção 3 deste manual.

---

_Gerado por – Leprechaun´s Green Team_
