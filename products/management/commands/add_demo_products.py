from django.core.management.base import BaseCommand
from products.models import Product

class Command(BaseCommand):
    help = 'Adds demo products to the database'

    def handle(self, *args, **options):
        demo_products = [
            {
                'name': 'Classic White T-Shirt',
                'description': 'Premium cotton crew neck t-shirt perfect for everyday wear. Comfortable fit with a modern silhouette.',
                'price': 29.99,
                'size': 'M',
                'image_url': 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=400&h=400&fit=crop'
            },
            {
                'name': 'Slim Fit Jeans',
                'description': 'Modern slim fit jeans in dark wash denim. Stretch fabric for comfort and mobility.',
                'price': 79.99,
                'size': 'L',
                'image_url': 'https://images.unsplash.com/photo-1542272604-787c3835535d?w=400&h=400&fit=crop'
            },
            {
                'name': 'Casual Blazer',
                'description': 'Versatile casual blazer perfect for smart casual occasions. Made from breathable cotton blend.',
                'price': 129.99,
                'size': 'L',
                'image_url': 'https://images.unsplash.com/photo-1593030761757-71fae45fa0e7?w=400&h=400&fit=crop'
            },
            {
                'name': 'Polo Shirt',
                'description': 'Classic polo shirt in navy blue. Made from pique cotton for breathability and comfort.',
                'price': 45.99,
                'size': 'M',
                'image_url': 'https://images.unsplash.com/photo-1586790170083-2f9ceadc732d?w=400&h=400&fit=crop'
            },
            {
                'name': 'Chino Pants',
                'description': 'Versatile chino pants in khaki. Perfect for both casual and business casual settings.',
                'price': 59.99,
                'size': 'L',
                'image_url': 'https://images.unsplash.com/photo-1473966968600-fa801b869a1a?w=400&h=400&fit=crop'
            },
            {
                'name': 'Hooded Sweatshirt',
                'description': 'Comfortable hooded sweatshirt in charcoal grey. Perfect for layering in cooler weather.',
                'price': 49.99,
                'size': 'XL',
                'image_url': 'https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=400&h=400&fit=crop'
            },
            {
                'name': 'Dress Shirt',
                'description': 'Crisp white dress shirt with a modern fit. Made from wrinkle-resistant cotton.',
                'price': 69.99,
                'size': 'M',
                'image_url': 'https://images.unsplash.com/photo-1602810318383-e386cc2a3ccf?w=400&h=400&fit=crop'
            },
            {
                'name': 'Leather Jacket',
                'description': 'Classic leather jacket with a modern twist. Premium faux leather with quilted detailing.',
                'price': 199.99,
                'size': 'L',
                'image_url': 'https://images.unsplash.com/photo-1551028719-00167b16eac5?w=400&h=400&fit=crop'
            }
        ]

        for product_data in demo_products:
            product, created = Product.objects.get_or_create(
                name=product_data['name'],
                defaults=product_data
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully created product "{product.name}"')
                )
            else:
                # Update existing products with size information
                product.size = product_data['size']
                product.save()
                self.stdout.write(
                    self.style.WARNING(f'Updated product "{product.name}" with size information')
                )

        self.stdout.write(
            self.style.SUCCESS(f'Demo products have been updated with size information!')
        ) 