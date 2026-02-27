# Guia de Release e Versionamento - AutoRewardsPC

_Processos de Entrega Contínua e Ciclo de Vida - Versão 1.0_

## 1. Estratégia de Versionamento

O projeto adota o **Semantic Versioning (SemVer)** seguindo o formato `MAJOR.MINOR.PATCH`:

- **MAJOR:** Mudanças incompatíveis (breaking changes).
- **MINOR:** Novas funcionalidades compatíveis.
- **PATCH:** Correções de bugs e segurança.

## 2. Processo de Release

O processo de release é totalmente automatizado via GitHub Actions.

### 2.1. Como criar uma Release

Para disparar uma nova build e publicar uma release, basta criar uma TAG no git e fazer o push.

**Passo a passo:**

```bash
git pull origin main
git tag v1.0.X
git push origin v1.0.X
```

## 3. Pipeline CI/CD (GitHub Actions)

O arquivo de workflow `.github/workflows/build-exe.yml` é responsável por:

1. **Trigger:** Detectar push de tags `v*`.
2. **Setup:** Instalar Python e dependências.
3. **Build:** Executar `python build.py`.
4. **Publish:** Criar uma Release no GitHub e fazer upload do `AutoRewardsPC.exe`.

## 4. Manutenção do Changelog

Recomendamos manter um arquivo `CHANGELOG.md` atualizado:

- **Added:** Novas features.
- **Fixed:** Correções de bugs.
- **Changed:** Alterações em funcionalidades existentes.

---

_assinada por **David Wallace Marques Ferreira** - Engenheiro Sênior_
