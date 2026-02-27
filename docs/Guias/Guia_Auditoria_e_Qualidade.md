# Guia de Auditoria e Qualidade 🛡️⚖️🧪

Este documento descreve os padrões de excelência técnica e os processos de garantia de qualidade aplicados ao projeto **AutoRewardsPC**.

## 1. Protocolo Juggernaut Integrity Audit

Toda alteração significativa no código deve seguir o protocolo de auditoria para garantir a "Blindagem Diamante" do sistema.

### Passos Mandatórios

1. **🔍 Análise de Impacto:** Avaliar como a mudança afeta o fluxo de automação e leitura de OCR.
2. **🧪 Testes de Integração:** Criar ou atualizar testes em `tests/` para validar a nova lógica.
3. **🛡️ Verificação de Travas:** Confirmar que os mecanismos de segurança (como o fechamento automático do navegador) continuam operantes.
4. **📊 Relatório de Integridade:** Documentar o veredito da auditoria.

## 2. Testes de Integração de OCR

O motor de OCR é o "Coração do Sistema". Utilizamos mocks e simulações de ruído para garantir que a leitura de pontuação seja resiliente a:

- Diferentes resoluções de tela.
- Artefatos de renderização do navegador.
- Variações no texto detectado (ex: `Searcn` vs `Search`).

### Como Executar os Testes

```bash
python -m unittest discover tests
```

## 3. Estética e Comunicação

- **Logs:** Devem ser claros e educativos para o usuário.
- **Financeiro:** Valores devem sempre usar formatação adequada para clareza absoluta.

---

🦾 _Qualidade é o alicerce da nossa automação._
