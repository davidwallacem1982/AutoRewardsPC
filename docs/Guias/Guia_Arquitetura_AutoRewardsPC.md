# Guia de Arquitetura - AutoRewardsPC

_Documentação Técnica de Alto Nível - Versão 1.0_

## 1. Introdução Arquitetural

O AutoRewardsPC foi projetado seguindo princípios de design modular e separação de responsabilidades. Embora seja uma aplicação desktop pequena, ela adota conceitos de DDD (Domain-Driven Design) simplificado para garantir manutenibilidade e testabilidade.

## 2. Visão Geral do Sistema

O sistema opera como um Agente de Automação Desktop (RPA) assistido. Ele não roda em background silencioso (serviço), mas sim como uma aplicação interativa que assume o controle dos periféricos (mouse/teclado) para realizar tarefas no navegador.

## 3. Camadas da Aplicação

### 3.1. Camada de Apresentação (UI)

Responsável por toda interação com o usuário. Implementada usando CustomTkinter.

**Principais Componentes:**

- `App` (`src/ui/app.py`): Container principal, gerencia janelas e rotas.
- `Theme` (`src/ui/theme.py`): Centraliza definições de estilo (cores, fontes).
- `ViewModels`: Lógica de apresentação embutida na classe App (padrão simplificado para TKinter).

### 3.2. Camada de Aplicação/Core

Orquestra os fluxos de automação e regras de negócio.

**Principais Componentes:**

- `Automation` (`src/core/automation.py`): Classe central que executa os roteiros de navegação.
- `Tesseract Integration`: Módulo de interface com o motor OCR externo.

### 3.3. Camada de Domínio/Dados

Define as estruturas de dados e contratos.

**Principais Componentes:**

- `Items` (`src/domain/items.py`): DTOs e constantes.
- `Configuração` (`calibration_config.json`): Persistência local de parâmetros de calibração.

### 3.4. Camada de Testes (QA) [NEW]

Garante a precisão e estabilidade das operações críticas.

**Principais Componentes:**

- `OCR Validation` (`tests/test_ocr_integration.py`): Testes de integração que validam a precisão do motor de OCR e regex sob diversas condições.

## 4. Fluxos Críticos

### 4.1. Inicialização

1. `main.py` é invocado.
2. **Mutex Check**: Garante instância única via Win32 API.
3. **Setup de Logs**: Configura rotação de arquivos.
4. **Bootstrap UI**: Instancia App e loop Tkinter.

### 4.2. Ciclo de Automação

O ciclo de automação roda em uma Thread separada (`threading.Thread`) para não congelar a UI.

**Flow:**

> `UI Click` -> `start_automation_thread()` -> `Automation.run_safe()` -> (Loop de Ações) -> `Update UI Log`

## 5. Decisões de Design

| Decisão               | Justificativa                                                                |
| :-------------------- | :--------------------------------------------------------------------------- |
| **CustomTkinter**     | Aparência moderna (Dark Mode) nativa e fácil implementação em Python.        |
| **Tesseract Externo** | Evita inflar o executável e permite update do motor OCR independente da app. |
| **PyAutoGUI**         | Abstração cross-platform de input, embora o foco seja Windows.               |
| **JSON Config**       | Formato legível e simples para persistir dados locais (NoSQL light).         |

---

_assinada por **David Wallace Marques Ferreira** - Engenheiro Sênior_
