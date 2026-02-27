<div align="center">

![AutoRewardsPC Social Preview](assets/social_preview.png)

# 🎯 AutoRewardsPC

### Solução Avançada de Automação Desktop para Windows

_Robusta, Portátil e Baseada em Visão Computacional_

![Release](https://img.shields.io/badge/release-v1.0.0-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)](https://www.python.org/)
![Tests](https://img.shields.io/badge/tests-6/6_passed-brightgreen)
![Integrity](https://img.shields.io/badge/integrity-diamond_audit-blueviolet)

**O **AutoRewardsPC** é uma aplicação desktop desenvolvida em **Python** que automatiza processos
repetitivos com precisão de OCR, distribuída como um **executável (.exe)** para Windows.  
 O usuário final **não precisa instalar Python**, bibliotecas ou configurar nada — é só baixar
e executar.**

[📖 Documentação Oficial Completa](docs/INDEX.md) | [🌐 Site do Projeto](https://davidwallacem1982.github.io/AutoRewardsPC)

</div>

## 🏷️ Palavras-chave

`RPA`, `Automação`, `Bing Rewards Bot`, `Microsoft Rewards Automation`, `Python Automation`, `Desktop App`, `OCR`, `Vision AI`, `Open Source`

## 📋 Sobre o Projeto

O **AutoRewardsPC** é uma aplicação desktop de alta performance desenvolvida em **Python** e distribuída como executável nativo (`.exe`) para Windows. Projetado com uma arquitetura limpa e modular, o sistema elimina a necessidade de configuração de ambiente pelo usuário final, entregando uma ferramenta pronta para uso imediato.

Utilizando tecnologias de **Visão Computacional (OCR)**, o sistema é capaz de interpretar textos e elementos visuais na tela, permitindo automações complexas que dependem de leitura de conteúdo, não apenas de coordenadas fixas.

### ✨ Destaques Técnicos

- 🏗️ **Arquitetura Profissional:** Estrutura baseada em Domain-Driven Design (DDD), separando camadas de `domain`, `core` e `ui`.
- 🤖 **Motor de Automação:** Reconhecimento de texto via Tesseract OCR para interações inteligentes.
- 🔄 **CI/CD Integrado:** Build automático de releases via GitHub Actions.
- 🛡️ **Segurança:** Não requer instalação de dependências sensíveis no sistema do usuário (Python/PyPI).

---

## 🖥️ Requisitos

- Windows 10 ou superior (64 bits)
- Não é necessário Python instalado
- Não é necessário Git ou GitHub
- O sistema é autossuficiente, mas depende de um componente externo para
  o motor de reconhecimento de texto que é o Tesseract OCR

---

## 🚀 Download (Windows)

👉 **Baixe a versão mais recente do programa aqui:**

🔗 [🚀 Download da Última Versão](https://github.com/davidwallacem1982//AutoRewardsPC/releases/latest)

### 📦 Após o download

1. Extraia o arquivo `.zip` em uma pasta de sua preferência  
   (exemplo: `C:\AutoRewardsPC`)
2. Entre na pasta extraída
3. Crie **um atalho** do arquivo `AutoRewardsPC.exe` na área de trabalho
4. Clique no atalho para executar o sistema, **(esse passo só pode ser feito depois da instalação do Tesseract OCR, instruções da instalação dele logo abaixo)**.

---

## 🔍 Dependência externa – Tesseract OCR

Este programa utiliza o **Tesseract OCR** (Optical Character Recognition) para realizar a **leitura e reconhecimento de textos exibidos na tela**.

O Tesseract é responsável por converter imagens e capturas de tela em texto digital, permitindo que o sistema:

- identifique palavras, números e padrões visuais
- reconheça textos que não podem ser lidos diretamente pelo sistema
- automatize ações com base no conteúdo exibido na tela

Sem o Tesseract OCR, o programa **não consegue interpretar textos presentes em imagens ou capturas**, o que inviabiliza parte fundamental do funcionamento do sistema.

### 📌 Por que o Tesseract não vem embutido no executável?

O Tesseract OCR é uma ferramenta externa e independente do Python.  
Por boas práticas de distribuição e licenciamento, ele **não é incorporado diretamente** ao executável (`.exe`) do programa.

Isso traz vantagens como:

- executável mais leve
- menor chance de bloqueio por antivírus
- facilidade de atualização do OCR
- maior estabilidade e compatibilidade

### 📥 Instalação do Tesseract OCR (Obrigatório)

1. Acesse o instalador oficial:  
   [🚀 Download da Última Versão](https://github.com/UB-Mannheim/tesseract/wiki)
2. Baixe e instale normalmente no Windows
3. Durante a instalação, mantenha o caminho padrão: `C:\Program Files\Tesseract-OCR\tesseract.exe`
4. Caso utilize outro caminho, configure a variável de ambiente: `TESSERACT_PATH=C:\caminho\para\tesseract.exe`

---

## 🧪 Testes e Qualidade (Precisão Diamantina) 💎

O AutoRewardsPC não é apenas um script de automação; é um sistema blindado. Implementamos uma camada de **Testes de Integração de OCR** para garantir que a identificação de pontos seja 100% precisa em diversas resoluções de tela.

### 🛡️ Auditoria de Integridade

Todo o código passa pelo protocolo **Juggernaut Integrity Audit**, garantindo que as travas de segurança e a lógica de meta diária nunca falhem.

- 🔬 **Precisão:** Validação de padrões OCR (`PC Search`, `X / Y`).
- 🛑 **Segurança:** Encerramento automático garantido ao atingir a meta.
- 🏆 **QA:** Testes automatizados executados via `python -m unittest discover tests`.

[📄 Ver Relatório de Integridade Técnica](docs/Auditoria/Relatorio_Integridade.md)

---

## ✨ Funcionalidades

- Interface simples e intuitiva
- Captura automatizada de ações na tela
- Execução por mouse ou teclado
- Captura sem mover o mouse (Enter)
- Aplicação portátil
- Build automático via GitHub Actions

---

## 📚 Documentação Oficial

Toda a documentação do **AutoRewardsPC** está disponível para leitura online:

### 👤 Usuários Finais e Clientes

- 📘 [**Manual do Usuário**](docs/Manuais/Manual_Usuario_AutoRewardsPC.md)
- 📄 [**Documentação Comercial**](docs/Comercial/AutoRewardsPC_Documentacao_Comercial.md)

### 🛠️ Suporte e Operação

- 🧰 [**Guia de Suporte e Diagnóstico**](docs/Guias/Guia_Suporte_e_Diagnostico_AutoRewardsPC.md)
- 🔧 [**Manual Técnico de Sustentação**](docs/Manuais/Manual_Tecnico_AutoRewardsPC.md)

### 👨‍💻 Desenvolvedores

- 🏗️ [**Guia de Arquitetura**](docs/Guias/Guia_Arquitetura_AutoRewardsPC.md)
- 🔌 [**Guia de Extensão**](docs/Guias/Guia_Extensao_Desenvolvedor_AutoRewardsPC.md)
- 🏷️ [**Guia de Release**](docs/Guias/Guia_Release_e_Versionamento_AutoRewardsPC.md)

### 📊 Relatórios de Qualidade

- 🏆 [**Análise de SEO e Governança**](docs/SEO/Analise_SEO_Fevereiro_2026.md)
  > Relatório de conformidade técnica e comunitária (Fev/2026).

---

## 📜 Licença

Distribuído sob a licença **MIT**.

---

Desenvolvido com ❤️ em Python assinada por **David Wallace Marques Ferreira** - Engenheiro Sênior.
