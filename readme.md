# 🚗 Django Car Dealer

![Feito com Django](https://img.shields.io/badge/feito%20com-Django-092E20?style=for-the-badge&logo=django&logoColor=white)

Aplicação web desenvolvida com **Django** para o gerenciamento de carros, permitindo **cadastro**, **edição**, **exclusão** e **visualização** de veículos com **upload de imagens** e **filtro por modelo**, tudo isso integrado a uma landing page simples e funcional.

#### 🧩 Funcionalidades

<small>

- ✅ Cadastro de carros com imagem
- 📝 Edição de veículos existentes
- ❌ Exclusão com confirmação
- 🔎 Filtro por **modelo do carro**
- 🖼️ Upload e exibição de imagens
-  🤖 Geração automática de **descrição do carro via IA**

</small>

---

#### 🛠️ Tecnologias Utilizadas

<small>

- **Python 3.x**
- **Django 4.x**
- **SQLite3 e PostgreSQL**
- **HTML5 & CSS3**
- **Pillow** (para tratamento de imagens)

</small>

---

### ⚙️ Como Rodar Localmente

<small> 1. Clone o repositório: 

```bash
git clone https://github.com/kaoan-eduardo/DjangoCarDealer.git
cd DjangoCarDealer
```

2. Crie o ambiente virtual: 

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. Instale as dependências: 

```bash
pip install -r requirements.txt
```

4. Realize as migrações:  

```bash
python manage.py migrate
```
5. (Opcional) Crie um superusuário: 

```bash
python manage.py createsuperuser
```

6. Inicie o servidor:

```bash
python manage.py runserver
```
</small>

#### 🔍 Filtro por Modelo
<small>

Na página inicial, você pode filtrar a lista de carros pelo modelo. Isso facilita a busca por veículos específicos.

</small>

#### 🤝 Contribuindo

<small>
Contribuições são bem-vindas!

1. Fork este repositório clicando em Fork no canto superior direito da página do GitHub.

2. Clone o repositório forkado para sua máquina:

```bash
git clone https://github.com/seu-usuario/DjangoCarDealer.git
```

3. Crie uma nova branch para a sua funcionalidade ou correção:

```bash
git checkout -b minha-nova-feature
```

4. Faça suas alterações e dê commit:
```bash
git commit -m "Adiciona nova funcionalidade"
```

5. Envie para seu fork:
```bash
git push origin minha-nova-feature
```

6. Abra um Pull Request explicando suas mudanças e por que elas devem ser incluídas.

</small>

##### Obrigado por contribuir! 💙

<br>
<br>

##### Feito com 💙 por @kaoan-eduardo
