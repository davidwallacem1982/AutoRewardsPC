# Guia de Suporte e Diagnóstico - AutoRewardsPC

_Procedimentos de Resolução de Problemas (Troubleshooting) - Versão 1.0_

## 1. Escopo deste Guia

Este documento orienta analistas de Nível 1 e Nível 2 na identificação e correção de falhas comuns na operação do AutoRewardsPC.

## 2. Matriz de Diagnóstico Rápido

| Sintoma                      | Causa Provável                      | Ação Imediata                                                                     |
| :--------------------------- | :---------------------------------- | :-------------------------------------------------------------------------------- |
| Aplicação não abre           | Processo travado ou bloqueio de AV  | Verificar Gerenciador de Tarefas e matar processo duplicado.                      |
| Botão "Iniciar" não funciona | Microsoft Edge não encontrado       | Verificar se o Edge está instalado e acessível.                                   |
| Erro de OCR/Tesseract        | Tesseract não instalado/configurado | Instalar Tesseract ou corrigir variável de ambiente.                              |
| Mouse clicando errado        | Resolução de tela ou Zoom           | Ajustar escala do Windows para 100% e resolução 1366x768+.                        |
| Loop infinito na busca       | Bing bloqueou pesquisas rápidas     | Aumentar intervalo entre pesquisas nas configurações (se disponível) ou aguardar. |

## 3. Análise de Logs

A ferramenta gera logs detalhados em:

> `C:\...\AutoRewardsPC\logs\automation.log`

### Padrões de Erro no Log

- `[INFO] Starting...` -> Fluxo normal.
- `[ERROR] Element not found` -> Interface do Bing mudou ou página não carregou.
- `[CRITICAL] TesseractNotFound` -> Falha na dependência de OCR.

## 4. Procedimentos Avançados

### 4.1. Reset de Configurações

Se a aplicação estiver com comportamento errático, delete o arquivo `calibration_config.json` para forçar uma nova calibração limpa.

### 4.2. Modo de Debug

Execute a aplicação via terminal (CMD/PowerShell) para ver a saída padrão (stdout) em tempo real caso a GUI não abra:

> `.\AutoRewardsPC.exe`

---

_assinada por **David Wallace Marques Ferreira** - Engenheiro Sênior_
