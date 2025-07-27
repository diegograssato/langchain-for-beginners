
## Ambiente de desenvolvimento

- [Visual Studio Code](https://code.visualstudio.com/)
- [PyCharm Community Edition](https://www.jetbrains.com/pycharm/download/?section=windows)
- [Python for windows](https://www.python.org/downloads/)


## Começando

- Crie uma pasta onde você deseja baixar o clone do repositório do nosso curso.
- Via terminal, acesse a pasta que você criou.

```
git clone https://github.com/diegograssato/langchain-for-beginners.git
```

- Abrindo o Pycharm, escolha o diretório que clonamos. Nesse momento o Pycharm pode criar um arquivo padrão main.py, mas ignore ele por enquanto. (Opcional: Se o Pycharm tiver criado o arquivo main.py você pode excluir ele).
- Uma vez clonado o repositório, você pode criar o ambiente virtual (`venv`) via interface seguindo os passos apresentados no vídeo do youtube ou acessando via terminal o diretório `langchain-for-beginners` e executando o comando:

```
python -m venv .venv

```

- Uma vez que você criou o ambiente virtual você deve ativa-lo, o ambiente virtual serve basicamente para não termos que dependencia soltas de projetos, ou utilizar varias versões de bibliotecas em projetos distintos sem alterar nada no sistema operacional.

```
#Linux
source .venv/bin/activate

# Windows
 .\.venv\Scripts\activate

(.venv) PS C:\Users\langchain-for-beginners>
```


- Para destivar o abiente virtual em ambos os sistemas operacionais use o comando abaixo:

```
deactivate
```

- Uma vez que você criou o ambiente virtual, acesse o terminal dentro da interface do Pycharm, pois ele ativará o ambiente virtual e instale as dependências.

```
pip install --upgrade pip
pip install ipykernel

# Setup do kernel para noteboks
python -m ipykernel install --user --name grassato --display-name "Python (langchain)"
pip --disable-pip-version-check --no-cache-dir install -r  requirements.txt

```


- Após a instalação você estará com o ambiente pronto com as dependências do LangChain instaladas.

- Por fim, faça uma cópia do arquivo `.env.example` para `.env` e atualize as variáveis com seus valores (suas chaves APIs).


## Configurando Provedores

As tarefas **podem** também ser configuradas para funcionar contra uma ou mais implantações de Modelos de Linguagem de Grande Porte (LLM) através de um provedor de serviços suportado, como OpenAI, Azure ou Hugging Face. Estes fornecem um _endpoint hospedado_ (API) que podemos acessar programaticamente com as credenciais corretas (chave ou token de API). Neste curso, discutimos esses provedores:

 - [OpenAI](https://platform.openai.com/docs/models) com modelos diversos, incluindo a série principal GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/) para modelos OpenAI com foco em prontidão empresarial
 - [Hugging Face](https://huggingface.co/docs/hub/index) para modelos de código aberto e servidor de inferência

**Você precisará usar suas próprias contas para estes exercícios**. As tarefas são opcionais, então você pode escolher configurar um, todos - ou nenhum - dos provedores com base em seus interesses. Algumas orientações para inscrição:

| Inscrição | Custo | Chave de API | Playground | Comentários |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup)| [Preços](https://openai.com/pricing#language-models)| [Baseado em Projetos](https://platform.openai.com/api-keys) | [Sem Código, Web](https://platform.openai.com/playground) | Vários Modelos Disponíveis |
| [Azure](https://aka.ms/azure/free)| [Preços](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/)| [Início Rápido SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart)| [Início Rápido Studio](https://learn.microsoft.com/azure/ai-services/openai/quickstart) |  [Deve Aplicar Antecipadamente para Acesso](https://learn.microsoft.com/azure/ai-services/openai/)|
| [Hugging Face](https://huggingface.co/join) | [Preços](https://huggingface.co/pricing) | [Tokens de Acesso](https://huggingface.co/docs/hub/security-tokens) | [Hugging Chat](https://huggingface.co/chat/)| [Hugging Chat tem modelos limitados](https://huggingface.co/chat/models) |
| | | | | |

Preencher arquivo `.env`

Vamos dar uma olhada rápida nos nomes das variáveis para entender o que elas representam:

| Variável  | Descrição  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Este é o token de acesso do usuário que você configurou no seu perfil |
| OPENAI_API_KEY | Esta é a chave de autorização para usar o serviço para endpoints OpenAI não-Azure |
| AZURE_OPENAI_API_KEY | Esta é a chave de autorização para usar esse serviço |
| AZURE_OPENAI_ENDPOINT | Este é o endpoint implantado para um recurso Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Este é o endpoint de implantação do modelo de _geração de texto_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Este é o endpoint de implantação do modelo de _incorporações de texto_ |
| | |

Nota: As duas últimas variáveis do Azure OpenAI refletem um modelo padrão para conclusão de chat (geração de texto) e busca vetorial (incorporações) respectivamente. As instruções para configurá-las serão definidas nas tarefas relevantes.

Configurar Azure: Do Portal

Os valores do endpoint e chave do Azure OpenAI serão encontrados no [Portal Azure](https://portal.azure.com), então vamos começar por lá.

1. Vá para o [Portal Azure](https://portal.azure.com)
1. Clique na opção **Chaves e Endpoint** na barra lateral (menu à esquerda).
1. Clique em **Mostrar Chaves** - você deverá ver o seguinte: CHAVE 1, CHAVE 2 e Endpoint.
1. Use o valor da CHAVE 1 para AZURE_OPENAI_API_KEY
1. Use o valor do Endpoint para AZURE_OPENAI_ENDPOINT

Em seguida, precisamos dos endpoints para os modelos específicos que implantamos.

1. Clique na opção **Implantações de Modelos** na barra lateral (menu à esquerda) para o recurso Azure OpenAI.
1. Na página de destino, clique em **Gerenciar Implantações**

Isso o levará ao site do Azure OpenAI Studio, onde encontraremos os outros valores conforme descrito abaixo

Configurar Azure: Do Studio

1. Navegue até o [Azure OpenAI Studio](https://oai.azure.com) **do seu recurso** conforme descrito acima.
1. Clique na aba **Implantações** (barra lateral, à esquerda) para ver os modelos atualmente implantados.
1. Se o modelo desejado não estiver implantado, use **Criar nova implantação** para implantá-lo.
1. Você precisará de um modelo de _geração de texto_ - recomendamos: **gpt-35-turbo**
1. Você precisará de um modelo de _incorporação de texto_ - recomendamos **text-embedding-ada-002**

Agora atualize as variáveis de ambiente para refletir o _Nome da Implantação_ usado. Este será tipicamente o mesmo que o nome do modelo, a menos que você o tenha alterado explicitamente. Assim, como exemplo, você pode ter:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Não se esqueça de salvar o arquivo .env quando terminar**. Agora você pode sair do arquivo e voltar para as instruções para executar o notebook.

### Configurar OpenAI: Do Perfil

Sua chave de API do OpenAI pode ser encontrada na sua [conta OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Se você não tiver uma, pode se inscrever para uma conta e criar uma chave de API. Assim que tiver a chave, você pode usá-la para preencher a variável `OPENAI_API_KEY` no arquivo `.env`.

### Configurar Hugging Face: Do Perfil

Seu token do Hugging Face pode ser encontrado no seu perfil em [Tokens de Acesso](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Não poste ou compartilhe estes publicamente. Em vez disso, crie um novo token para uso neste projeto e copie-o para o arquivo `.env` sob a variável `HUGGING_FACE_API_KEY`. _Nota:_ Este tecnicamente não é uma chave de API, mas é usado para autenticação, então estamos mantendo essa convenção de nomenclatura para consistência.


### Criar um github Personal Access Token (PAT) manualmente
Se você está rodando scripts fora do GitHub Actions, por exemplo localmente ou em um app Python, use um PAT (Personal Access Token):

Passos:
Acesse: https://github.com/settings/tokens

Clique em "Generate new token (classic)"

Defina:

Nome

Validade

Scopes (permissões), como:

repo (para repositórios privados)

workflow (para disparar GitHub Actions)

admin:org (para acesso a organizações, se necessário)

Clique em "Generate token"

Copie o token gerado e use como variável de ambiente:


```bash
# Github API Key for the OpenAI provider
GITHUB_TOKEN="ghp_XXxxxxxxxxyyyyyyyyyaaaa"
```
