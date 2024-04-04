import requests
import csv

class ProductManager:
    def __init__(self):
        self.base_url = 'https://dummyjson.com/products'
        self.category_url = 'https://dummyjson.com/products/categories'

    def get_all_products(self):
        url = f'{self.base_url}?limit=100'
        response = requests.get(url)
        data = response.json().get('products', list())
        self._save_to_csv(data)

    def get_products_by_category(self, category):
        url = f'{self.base_url}/category/{category}'
        response = requests.get(url)
        data = response.json().get('products', list())
        self._save_to_csv(data)

    def _save_to_csv(self, data):
        with open('data_products.csv', 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['ID', 'Name', 'Description', 'Price', 'Discount Percentage', 'Rating', 'Stock', 'Brand', 'Category', 'Images']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if csvfile.tell() == 0:
                writer.writeheader()
            for occurrence in data:
                images = ';'.join(occurrence.get('images', list()))
                writer.writerow({
                    'ID': str(occurrence.get('id', str())),
                    'Name': occurrence.get('title', str()),
                    'Description': occurrence.get('description', str()),
                    'Price': str(occurrence.get('price', str())),
                    'Discount Percentage': str(occurrence.get('discountPercentage', str())),
                    'Rating': str(occurrence.get('rating', str())),
                    'Stock': str(occurrence.get('stock', str())),
                    'Brand': occurrence.get('brand', str()),
                    'Category': occurrence.get('category', str()),
                    'Images': images,
                })
        print('Arquivo salvo como data_products.csv')

def main():
    manager = ProductManager()
    print(5 * ' - ', 'Opções', 5 * ' - ')
    choice = input("  1. Para pegar todos os produtos \n  2. Para escolher uma categoria \nEscolha: ")
    
    if choice == '1':
        manager.get_all_products()
    if choice == '2':
        url_category = manager.category_url
        response = requests.get(url_category)
        list_categories = response.json()
        category = input(f'Categorias: {list_categories} \nEscolha uma categoria para ver a lista de produtos da categoria: ')
        manager.get_products_by_category(category)


if __name__ == "__main__":
    main()
