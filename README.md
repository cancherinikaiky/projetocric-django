# ROTA CRIC - ReadMe

## Visão Geral
O projeto ROTA CRIC é um site de cicloturismo que tem como objetivo promover e facilitar a exploração da região carbonífera do Rio Grande do Sul, Brasil. Foi desenvolvido utilizando o framework Django, com funcionalidades interativas adicionadas por meio de JavaScript puro.

## Funcionalidades Principais

### Roteiros de Cicloturismo
- Apresenta uma lista de roteiros de cicloturismo disponíveis na região carbonífera do Rio Grande do Sul, incluindo informações detalhadas, mapas e dicas.

### Sistema de Reservas
- Permite aos visitantes do site reservar passeios e serviços relacionados ao cicloturismo, como aluguel de bicicletas e guias turísticos.

### Compartilhamento de Experiências
- Os ciclistas podem compartilhar suas experiências e fotos das rotas de cicloturismo, ajudando a comunidade a descobrir novos lugares e obter dicas valiosas.

### Calendário de Eventos
- Mantém um calendário de eventos relacionados ao cicloturismo na região, permitindo que os usuários se programem para participar de passeios em grupo, competições e outros eventos.

### Informações da Região
- Oferece informações sobre a região carbonífera do Rio Grande do Sul, incluindo história, cultura, gastronomia e acomodações disponíveis.

## Requisitos do Sistema

- Python 3.x
- Django 3.x
- Banco de dados (por padrão, o Django usa o SQLite, mas você pode configurar para outros, como MySQL ou PostgreSQL)
- Navegador da Web compatível com JavaScript

## Configuração

1. Clone o repositório em seu ambiente de desenvolvimento:

   ```
   git clone https://github.com/cancherinikaiky/projetocric-django
   ```

2. Crie um ambiente virtual para o projeto e ative-o:

   ```
   python -m venv venv
   source venv/bin/activate  # No Windows, use "venv\Scripts\activate"
   ```

3. Instale as dependências do projeto:

   ```
   pip install -r requirements.txt
   ```

4. Configure o arquivo de configuração `settings.py` com informações do banco de dados e outras configurações necessárias.

5. Execute as migrações do banco de dados:

   ```
   python manage.py migrate
   ```

6. Inicie o servidor de desenvolvimento:

   ```
   python manage.py runserver
   ```

7. Acesse o site em seu navegador, normalmente em http://localhost:8000.

## Contribuição

Aceitamos contribuições para melhorar o projeto ROTA CRIC. Se você deseja contribuir, siga estas etapas:

1. Faça um fork deste repositório.

2. Crie uma branch para sua funcionalidade ou correção de bug: `git checkout -b feature-nova` ou `git checkout -b correcao-bug`.

3. Faça as alterações necessárias e adicione comentários ao código, se necessário.

4. Teste suas alterações para garantir que não haja problemas.

5. Envie um pull request para este repositório.

## Autores

- Kaiky Cancherini, Jeremias Piontkoski, Mateus Peres, Pedro Rodrigues, Regis Brasil, Marcelo Oliveira e Vanius Zapalowski

## Contato

- E-mail: kaikyfillipo@gmail.com

Agradecemos por escolher o ROTA CRIC para explorar a região carbonífera do Rio Grande do Sul em duas rodas. Se você tiver alguma dúvida ou feedback, não hesite em entrar em contato. Esperamos que esta plataforma ajude a comunidade de ciclistas a desfrutar de experiências incríveis na região.
