# 🛡️ SOC & DevSecOps Automation Tools

Este repositório contém ferramentas práticas desenvolvidas para automatizar tarefas diárias de um Analista de SOC (Security Operations Center) Tier 1, visando reduzir o tempo de triagem de incidentes e mitigar riscos operacionais.

---

## 🛠️ Ferramentas Disponíveis

### 1. Phishing URL Defanger & IoC Extractor
Ferramenta em Python utilizada durante a triagem inicial de e-mails suspeitos e alertas de phishing. 

* **O Problema:** Analistas precisam compartilhar links maliciosos em relatórios de incidentes (Jira, ServiceNow, TheHive) sem o risco de execução acidental (*misclick*) por outros membros da equipe.
* **A Solução:** O script extrai o domínio principal (IoC - Indicador de Comprometimento) da URL e aplica técnicas de *defanging* (substituição de caracteres perigosos, como `http` por `hxxp` e `.` por `[.]`).
* **Como usar:**
    ```bash
    python3 url_defanger.py [http://malicious-domain.com/payload.exe](http://malicious-domain.com/payload.exe)
    ```

---

## 🚀 Tecnologias e Habilidades Demonstradas
* **Linguagem:** Python 3
* **Segurança Operacional:** Tratamento seguro de Indicadores de Comprometimento (Defanging).
* **Tratamento de Strings:** Manipulação e extração de dados de URLs.
