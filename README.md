# Checklist de Veículos

## Descrição

O projeto **Checklist** é uma aplicação web que permite realizar e registrar a avaliação de diferentes itens de um veículo, categorizando-os em três estados: Bom, Regular e Ruim. O sistema também inclui opção para adicionar observações e salvar os dados coletados para análise futura.

## Funcionalidades

- Registrar a placa do veículo avaliado.
- Avaliar itens predefinidos em três categorias: **Bom**, **Regular**, **Ruim**.
- Adicionar observações gerais sobre o veículo.
- Exibir informações da última sessão registrada.
- Salvar os dados do checklist no sistema.
- Botão para retornar à página inicial.

## Tecnologias Utilizadas

- **HTML5** e **CSS3** para a interface do usuário.
- **Django** como framework backend.
- **Python** para a lógica do servidor.
- **PostgreSQL** para persistência de dados.

## Estrutura do Projeto

### Arquivos Principais:

- **templates/checklist.html**: Contém o código HTML para o formulário de checklist.
- **views.py**: Lida com as requisições e renderizações de páginas.
- **models.py**: Define os modelos para armazenar informações do checklist.
- **urls.py**: Configura as rotas para acesso às páginas da aplicação.

### Estrutura de Dados:

- **Checklist**:
  - Placa do Veículo.
  - Data e hora do registro.
  - Avaliação de itens.
  - Observações.

