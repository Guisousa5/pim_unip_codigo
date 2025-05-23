
# PIM - Projeto Integrado Multidisciplinar: Plataforma de Educação Digital Segura

## Descrição do Projeto

Este projeto, desenvolvido como parte da disciplina de **Projeto Integrado Multidisciplinar (PIM)** do curso de CST em Análise e Desenvolvimento de Sistemas da UNIP, visa a criação de uma **Plataforma de Educação Digital Segura** para inclusão digital e proteção de dados.

O objetivo geral é realizar o levantamento e análise de requisitos para o desenvolvimento de uma plataforma digital segura, considerando conceitos de pensamento lógico computacional, infraestrutura computacional e cibersegurança. O sistema foi projetado para permitir que usuários com diferentes níveis de conhecimento acessem conteúdos interativos sobre tecnologia da informação, programação básica e boas práticas de segurança digital, respeitando a LGPD (Lei Geral de Proteção de Dados) e princípios éticos.

A plataforma foi desenvolvida em **Python**, com dados armazenados em arquivos **JSON**, incorporando funcionalidades essenciais para o aprendizado e a segurança digital, além de oferecer estatísticas de uso para análise de desempenho.

---

## Objetivos

### Objetivo Geral

- Realizar o levantamento e análise de requisitos para o desenvolvimento de uma plataforma digital segura voltada para a educação digital e inclusão tecnológica, considerando pensamento lógico computacional, infraestrutura computacional e cibersegurança.

### Objetivos Específicos

- Aplicar conceitos matemáticos e estatísticos para análise de desempenho dos usuários na plataforma.
- Desenvolver um sistema em Python para ensino de lógica computacional e programação básica.
- Definir requisitos de infraestrutura computacional, contemplando desempenho, escalabilidade e segurança.
- Garantir a privacidade e proteção de dados dos usuários conforme a LGPD.
- Implementar diretrizes de cibersegurança para evitar ataques e vazamento de dados.
- Incluir princípios de ética e sustentabilidade digital, incentivando o uso responsável da tecnologia.

---

## Disciplinas Contempladas

**Base:**

- Matemática e Estatística  
- Pensamento Lógico Computacional com Python  
- Infraestrutura Computacional  
- Tecnologia da Informação e da Comunicação  
- Cibersegurança  
- LGPD  

**Complementar:**

- Ética, Cidadania e Sustentabilidade  
- Direitos Humanos  

---

## Contextualização do Caso

Este projeto atende à necessidade de uma ONG voltada para inclusão digital que busca oferecer um ambiente de aprendizado para comunidades carentes e estudantes de escolas públicas. A plataforma disponibiliza cursos básicos sobre pensamento lógico computacional, segurança digital e programação em Python, de forma interativa e acessível, garantindo a proteção dos dados dos usuários e promovendo cidadania digital, alinhada aos princípios de direitos humanos e ética no uso da tecnologia.

---

## Tecnologias e Diretrizes Utilizadas

- **Programa no modo Console:** Desenvolvido integralmente em Python.
- **Dados:** Armazenados em arquivos JSON para consulta, alteração e análise estatística.
- **Infraestrutura Computacional:** Definição da arquitetura, incluindo armazenamento e requisitos de segurança.
- **Segurança e LGPD:** Controle de acesso via login com senha criptografada (SHA-256), criptografia dos dados.
- **Estatísticas e Relatórios:** Análise do desempenho dos usuários utilizando média, moda e mediana.

---

## Funcionalidades Implementadas

- **Cadastro de Usuários:** Registro com armazenamento seguro de senhas via criptografia SHA-256.
- **Login Seguro:** Autenticação com verificação de senha criptografada.
- **Gestão de Cursos:**  
  - Cursos pré-definidos em lógica, Python e segurança digital.  
  - Listagem detalhada de cursos com descrição, duração e tópicos.  
  - Simulação de início e conclusão com registro do tempo e progresso do usuário.
- **Acompanhamento de Progresso:** Visualização do número de cursos concluídos, percentual de conclusão e tempo total de estudo.
- **Estatísticas da Plataforma:** Relatórios com total de usuários, acessos, média/moda/mediana das idades e tempo de estudo, curso mais popular.
- **Dicas de Segurança Digital:** Seção dedicada a boas práticas online.
- **Persistência de Dados:** Manutenção dos dados de usuários, cursos e acessos em arquivos JSON.

---

## Como Executar o Projeto

1. Clone o repositório ou baixe o arquivo `main.py`.
2. Certifique-se de ter o **Python 3.x** instalado em sua máquina.
3. Abra o terminal ou prompt de comando no diretório onde o arquivo `plataforma.py` está salvo.
4. Execute o script com o comando:

```bash
python plataforma.py
