# Consumo de APIs - JSON Fictício de Produtos

#### Sobre DummyJSON
DummyJSON é uma API REST online gratuita que permite gerar instantaneamente dados de espaço reservado sem a necessidade de configurar um servidor. É ideal para desenvolvimento front-end, fins educacionais, testes e prototipagem!

O recurso que usei foi a de 100 produtos, uma API fictícia que tem 100 produtos e suas informações. Exemplo:

```
{'id': 19,
  'title': 'Skin Beauty Serum.',
  'description': 'Product name: rorec collagen hyaluronic acid white face serum riceNet weight: 15 m',
  'price': 46,
  'discountPercentage': 10.68,
  'rating': 4.42,
  'stock': 54,
  'brand': 'ROREC White Rice',
  'category': 'skincare',
  'thumbnail': 'https://cdn.dummyjson.com/product-images/19/thumbnail.jpg',
  'images': ['https://cdn.dummyjson.com/product-images/19/1.jpg',
   'https://cdn.dummyjson.com/product-images/19/2.jpg',
   'https://cdn.dummyjson.com/product-images/19/3.png',
   'https://cdn.dummyjson.com/product-images/19/thumbnail.jpg']}
```
###### Link
https://dummyjson.com/

https://dummyjson.com/products

### Instalação

Para executar o projeto, siga os seguintes comandos:

  * Clone o repositório na sua máquina
  ```sh
    https://github.com/pie172/avaliacao1_consumoAPI.git
  ```
  * Entre no diretorório e Instale o virtualenv
  ```sh
  pip install virtualenv
  ```

  * Crie um ambiente virtual
  ```sh
  virtualenv venv 
  ```

  * Ative o ambiente virtual
  ```sh
  venv/Scripts/activate
  ```
  
  * Instale as dependências 
  ```sh
    pip install -r requirements.txt
  ```
### Rodar Script

  ```sh
  python products_class.py
  ```

### Opções
```
    1 -  Gera um relatório em um csv dos 100 produtos.
```
```
    2 - Mostra uma lista de categorias que os produtos pertence,
    você  escreve a categoria que deseja e o script gera um relatório 
    dos produtos da categoria.
```
###### Linguagem: 
* Python
###### Biblioteca:
* requests
* csv
