# Exercício: resolução de conflitos

Este repositório contém um conflito intencional para o treinamento **GitHub For Developers**.

## Objetivo

Resolver o conflito entre as branches abaixo, preservando uma mensagem de boas-vindas que faça sentido para o time.

- `treinamento/conflito-pessoa-a`
- `treinamento/conflito-pessoa-b`

## Roteiro

```bash
git fetch origin
git switch treinamento/conflito-pessoa-a
git merge origin/treinamento/conflito-pessoa-b
```

Abra `exercicios/conflito-mensagem.txt`, escolha ou combine as mensagens, remova os marcadores de conflito e finalize:

```bash
git add exercicios/conflito-mensagem.txt
git commit
```

Depois, confirme o resultado com `git status` e `git log --oneline --graph --all`.
