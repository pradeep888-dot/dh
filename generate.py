import json
import random

with open('products.json', 'r') as f:
    data = json.load(f)

current_id = max(p['id'] for p in data['products'])
new_products = []

protection_keywords = ['Case', 'Protector', 'Shield', 'Armor', 'Guard', 'Pad', 'Helmet']
protection_bases = ['Phone', 'Laptop', 'Knee', 'Screen', 'Backpack', 'Camera', 'Wallet']
pleasure_keywords = ['Massager', 'Toy', 'Gel', 'Cushion', 'Roller', 'Aroma', 'Candle']
pleasure_bases = ['Shoulder', 'Neck', 'Luxury', 'Relaxing', 'Therapy', 'Spa', 'Sensual']

for i in range(100):
    cat = 'Protection Tools' if i < 50 else 'Pleasure & Wellness'
    
    if cat == 'Protection Tools':
        name = f"{random.choice(protection_bases)} {random.choice(protection_keywords)} {random.randint(1,99)}X"
        icon = 'shield'
    else:
        name = f"{random.choice(pleasure_bases)} {random.choice(pleasure_keywords)} {random.choice(['Pro', 'Max', 'Lite', 'Ultra'])}"
        icon = 'heart'

    price = random.randint(199, 4999)
    discount = random.choice([0, 0, 5, 10, 15, 20])
    rating = round(random.uniform(3.5, 5.0), 1)
    reviews = random.randint(10, 5000)
    badge = random.choice(['', '', 'NEW', 'BESTSELLER', 'LIMITED'])

    new_products.append({
        'id': current_id + 1 + i,
        'name': name,
        'price': price,
        'icon': icon,
        'category': cat,
        'badge': badge,
        'rating': rating,
        'reviews': reviews,
        'discount': discount
    })

data['products'].extend(new_products)

with open('products.json', 'w') as f:
    json.dump(data, f, indent=4)
print('Added 100 new products!')
