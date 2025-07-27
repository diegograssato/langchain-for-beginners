# Curso LangChain - Iniciantes

Bem-vindo ao repositório do Curso LangChain fo Beginner! Aqui você encontrará todos os exemplos de código necessários para acompanhar o curso e aprender sobre LangChain do zero. Ao final do curso, você será capaz de criar seus próprios aplicativos com LLM integrado, construir chatbots RAG e automatizar tarefas com IA.


### Pré-requisitos

- Python  3.11 ou superior.
- Criar um ambiente virtual e clonar o repositório
- Instalar as dependências  presentes no arquivo requirements.txt


6) Execute os exemplos de código via interface ou via terminal, conforme sua preferência.

## Estrutura do Repositório

Veja o que você encontrará em cada pasta:

```
📁 curso-langchain/
├── 📁 00-course-setup/          # Configuração inicial do ambiente
│   ├── SETUP.md                 # Guia de configuração detalhado
│   └── setup-environment.sh     # Script de configuração automática
│
├── 📁 01-langchain/             # Fundamentos do LangChain
│   ├── 01-basic-prompt.ipynb    # Introdução a prompts básicos
│   ├── 01-langchain-chat-model.ipynb  # Modelos de chat
│   ├── 02-langchain-runnables.ipynb   # Conceitos de Runnables
│   ├── 03-langchain-template.ipynb    # Templates de prompts
│   ├── 04-langchain-output-parser.ipynb # Parsers de saída
│   ├── 05-langchain-document-loaders.ipynb # Carregadores de documentos
│   ├── 06-langchain-memory.ipynb      # Sistemas de memória
│   ├── 07-langchain-text-splitters.ipynb # Divisores de texto
│   ├── 08-langchain-routing.ipynb     # Roteamento de chains
│   ├── 09-langchain-embeddings.ipynb  # Embeddings e vetorização
│   ├── 10-langchain-vectores.ipynb    # Bancos de dados vetoriais
│   ├── 11-langchain-retrievers.ipynb  # Sistemas de recuperação
│   ├── 12-langchain-rag.ipynb         # RAG (Retrieval Augmented Generation)
│   ├── agent.py                 # Exemplo de agente básico
│   ├── app.py                   # Aplicação principal
│   ├── rag_main.py             # Implementação RAG principal
│   └── 📁 data/                # Dados de exemplo para exercícios
│
├── 📁 02-langgraph/             # Agentes inteligentes com LangGraph
│   ├── 02-langgraph-exemplo.ipynb     # Introdução ao LangGraph
│   ├── 03-langgraph-tools.ipynb       # Integração de ferramentas
│   ├── 04-langgraph-memory.ipynb      # Memória em grafos
│   ├── 05-langgraph-mcp.ipynb         # Model Context Protocol
│   ├── 06-langgraph-acp.ipynb         # Agent Communication Protocol
│   ├── MCP.md                  # Documentação sobre MCP
│   ├── agent-pre-built.py      # Agentes pré-construídos
│   ├── acp_agent.py            # Agente com ACP
│   └── exemplos de ferramentas: math_server.py, weather.py, pokemon.py, jira.py
│
├── 📁 03-crewia/               # Sistemas multi-agente com CrewAI
│   ├── 01-crew-exemplo.ipynb   # Exemplo de crew de agentes
│   ├── requirements.txt        # Dependências específicas do CrewAI
│   └── 📁 data/, 📁 db/        # Dados e banco para exercícios
│
├── 📁 helpers/                 # Utilitários e helpers
│   ├── 00-llm.ipynb           # Configuração base de LLM
│   └── llm.py                 # Classe helper para LLM
│
├── .env.exemplo                # Template de variáveis de ambiente
├── requirements.txt            # Dependências do projeto
└── README.md                   # Este arquivo
```

### 🎯 Ordem de Estudo Recomendada:

1. **00-course-setup/** - Configure seu ambiente primeiro
2. **01-langchain/** - Aprenda os fundamentos (notebooks 01-12 em sequência)
3. **02-langgraph/** - Construa agentes inteligentes
4. **03-crewia/** - Explore sistemas multi-agente

### 📚 Recursos por Módulo:

- **LangChain Básico**: Prompts, chains, memória, RAG
- **LangGraph**: Agentes, ferramentas, MCP, fluxos condicionais
- **CrewAI**: Coordenação de múltiplos agentes especializados

## FAQ

**Q: O que é LangChain?**\
A: LangChain é um framework que simplifica o processo de criação de aplicações que utilizam modelos de linguagem.

**Q: Como configuro meu ambiente?**\
A: Siga as instruções em **00-course-setup/SETUP.md**

**Q: Estou tendo problemas ao executar os exemplos, o que faço?**\
A: Verifique se todas as dependências foram instaladas corretamente e se as variáveis de ambiente estão configuradas.

