# meu_projeto_review

Projeto CRUD para lembrar todo o processo de codificação no python usando o
django e postgres como banco de dados, e fazendo deploy pelo render.
com filtro básico que busca a partir de um valor.

https://meu-projeto-review.onrender.com/stok/cadastrar_produto/

## Configuração para Produção

### Armazenamento de Mídia (Fotos)

As fotos dos produtos são armazenadas no AWS S3 em produção. Para configurar:

1. Crie um bucket no AWS S3
2. Configure as seguintes variáveis de ambiente no Render:
   - `AWS_ACCESS_KEY_ID`: Sua chave de acesso AWS
   - `AWS_SECRET_ACCESS_KEY`: Sua chave secreta AWS
   - `AWS_STORAGE_BUCKET_NAME`: Nome do seu bucket S3
   - `AWS_S3_REGION_NAME`: Região do bucket (padrão: us-east-1)

### Como executar localmente

1. Clone o repositório
2. Instale as dependências: `pip install -r requirements.txt`
3. Configure o arquivo `.env` com suas variáveis
4. Execute: `python manage.py runserver`

