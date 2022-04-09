# Paws-online-pet-store
<img width="1368" alt="Screen Shot 2022-04-03 at 11 31 39 AM" src="https://user-images.githubusercontent.com/97713325/161435929-178ff9c4-8a8d-4ee3-9d56-944ecdb03537.png">



# overview
This project creates a mini amazon for our best friends paws -- cats and dogs.The online shopping site will tailor products for pets.As pets have become more and more important members of human lives, we have seen an increase in demand for pet products and thus create a business opportunity for e-commerce that specializes in selling pet products. We hope our final product will be a convenient stop for pet owners to shop and explore for their loved ones.


# main features
## Account / Purchases
Users can register, login, logout and edit their account information.
Users can browse their purchase history.

## Products / Cart
Users can browse, search, add products to cart and purchase products.

## Inventory
Users can act as a seller and edit the inventory information.

## Feedback
Users can add rating/reviews to products/sellers.

# Usage
Edit the `Database` setting in paws_ltd/setting.py
Add your postfreSQL username and password in `USER` and `PASSWORD`
```
'NAME': 'pawsApp',
'USER': '###',
'PASSWORD': '###',
```
Run following commands to migrate
```
python manage.py makemigrations
python manage.py migrate
```

Run `python manage.py runserver` to browse the webpage