# Contributing to AutoRewardsPC

First off, thanks for taking the time to contribute!

The following is a set of guidelines for contributing to AutoRewardsPC, which is hosted in the [DavidWallaceM1982/AutoRewardsPC](https://github.com/DavidWallaceM1982/AutoRewardsPC) repository on GitHub.

## 🐞 Reporting Bugs

This section guides you through submitting a bug report.

1. **Check existing issues**: Verify if the bug has already been reported.
2. **Use the Template**: Open a new Issue and select the **Bug Report** template. Fill in all the fields, including your screen resolution and OS version.
3. **Screenshots**: If the automation fails on a specific screen, a screenshot is invaluable.

## 💡 Suggesting Enhancements

This section guides you through submitting an enhancement suggestion, including completely new features and minor improvements to existing functionality.

1. **Use the Template**: Open a new Issue and select the **Feature Request** template.
2. **Be Specific**: Describe exactly how the feature should work and why it is useful.

## 💻 Development Setup

1. **Fork and Clone** the repository.
2. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Tesseract OCR**: Ensure Tesseract is installed and reachable. See `README.md` for details.

## Pull Request Process

1. Ensure any install or build dependencies are removed before the end of the layer when doing a build.
2. Update the `README.md` with details of changes to the interface, this includes new environment variables, exposed ports, useful file locations and container parameters.
3. You may merge the Pull Request in once you have the sign-off of two other developers, or if you do not have permission to do that, you may request the second reviewer to merge it for you.

## 🧪 Testes e Auditoria Mandatória

Toda contribuição deve passar por:

1. **Testes Unitários/Integração:** Execute `python -m unittest discover tests` e garanta 100% de sucesso.
2. **Auditoria de Integridade:** Siga o `docs/Guias/Guia_Auditoria_e_Qualidade.md`.

## 🎨 Coding Style

- We use **Python** with type hints.
- Use `black` for formatting.
- Check `docs/Guias/Guia_Arquitetura_AutoRewardsPC.md` to understand where your code belongs (Core vs UI vs Domain).
