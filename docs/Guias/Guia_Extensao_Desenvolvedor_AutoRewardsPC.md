# Guia de Extensão para Desenvolvedores - AutoRewardsPC

_Como modificar, expandir e personalizar o sistema - Versão 1.0_

## 1. Introdução

Este guia é destinado a desenvolvedores que desejam adicionar novas funcionalidades, alterar o comportamento existente ou modificar a interface do AutoRewardsPC.

## 2. Setup do Ambiente de Desenvolvimento

Antes de começar, certifique-se de ter o ambiente configurado:

1. Python 3.10+
2. Dependências instaladas (`pip install -r requirements.txt`)
3. VS Code (Recomendado)

## 3. Adicionando Nova Etapa de Automação

Para ensinar o robô a clicar em um novo botão ou realizar uma nova ação:

### Passo 1: Mapear na UI (Calibration)

Edite o arquivo `src/ui/app.py`. Encontre a lista `self.calibration_steps` dentro do método `open_calibration_window`.

```python
self.calibration_steps = [
    ...
    {"key": "novo_botao", "desc": "Descrição para o Usuário"},
]
```

### Passo 2: Implementar Lógica no Core

Edite `src/core/automation.py`. No método `run` ou `run_safe`, adicione a lógica para usar a coordenada capturada.

```python
coords = self.load_calibration()
if "novo_botao" in coords:
    x, y = coords["novo_botao"]["x"], coords["novo_botao"]["y"]
    pyautogui.click(x, y)
```

## 4. Modificando a Interface (UI)

### Alterar Cores e Tema

Todas as constantes de cor estão centralizadas em `src/ui/theme.py`. Altere este arquivo para mudar a identidade visual da aplicação.

### Adicionar Componentes

A interface é construída com CustomTkinter em `src/ui/app.py`. Utilize o método `grid()` para posicionar novos widgets no layout.

## 5. Gerando Nova Versão

Após realizar suas alterações, é crucial gerar um novo executável para distribuição.

Execute o script de build na raiz do projeto:

> `python build.py`

Isso limpará as pastas antigas e gerará um novo `AutoRewardsPC.exe` na pasta `dist/`.

---

_Gerado por – Leprechaun´s Green Team_
