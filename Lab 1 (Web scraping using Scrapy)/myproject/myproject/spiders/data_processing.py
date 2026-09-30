import pandas as pd
import re

df=pd.read_csv('titles.csv')

print(f"Initial records: {len(df)}")

df_clean=df.drop_duplicates(subset=['upc'], keep='first')

print(f"\nRemoved duplicates: {len(df)-len(df_clean)} records")
print(f"Unique records: {len(df_clean)}\n")

def clean_text(text):
    if pd.isna(text):
        return ''
    text=re.sub(r'\s+',' ',str(text))
    return text.strip()

df_clean['title']=df_clean['title'].apply(clean_text)
df_clean['category']=df_clean['category'].apply(clean_text)
df_clean['rating']=df_clean['rating'].apply(clean_text)
df_clean['availability']=df_clean['availability'].apply(clean_text)

df_clean['description']=df_clean['description'].apply(clean_text)
df_clean['description']=df_clean['description'].fillna('No description available')
df_clean['description']=df_clean['description'].replace('','No description available')

def extract_stock(avail):
    if pd.isna(avail):
        return 0
    match=re.search(r'\((\d+)\s+available\)', str(avail))
    if match:
        return int(match.group(1))
    numbers=re.findall(r'\d+', str(avail))
    if numbers:
        return int(numbers[0])
    if 'in stock' in str(avail).lower():
        return 20
    return 0

df_clean['stock_count']=df_clean['availability'].apply(extract_stock)

def clean_price(price):
    if pd.isna(price):
        return 0.0
    cleaned = str(price).replace('£', '').replace(',', '').strip()
    try:
        return float(cleaned)
    except ValueError:
        return 0.0

df_clean['price_numeric']=df_clean['price'].apply(clean_price)

rating_map = {
    'One':1,'Two':2,'Three':3,'Four':4,'Five':5,
    'one':1,'two':2,'three':3,'four':4,'five':5
}

def clean_rating(rating):
    if pd.isna(rating):
        return 0
    rating_str=str(rating).strip().split()[0]
    return rating_map.get(rating_str,0)

df_clean['rating_numeric']=df_clean['rating'].apply(clean_rating)

def word_count(text):
    if pd.isna(text):
        return 0
    return len(str(text).split())

df_clean['description_word_count']=df_clean['description'].apply(word_count)

def price_band(price):
    if price<=15:
        return 'Budget (<15)'
    elif price<=25:
        return 'Moderate (15-25)'
    elif price<=40:
        return 'Premium (25-40)'
    elif price<=55:
        return 'Luxury (40-55)'
    else:
        return 'Elite (>55)'

df_clean['price_band']=df_clean['price_numeric'].apply(price_band)

def affordability_score(price):
    if price<=0:
        return 0
    score=max(1,min(10,10-(price-10)/5))
    return round(score,1)

df_clean['affordability_score']=df_clean['price_numeric'].apply(affordability_score)

def value_score(row):
    if row['price_numeric']==0:
        return 0
    rating_weight=row['rating_numeric'] / 5
    price_weight=max(1, 60 - row['price_numeric']) / 60
    score = (rating_weight * 0.6 + price_weight * 0.4) * 10
    return round(score, 1)

df_clean['value_score'] = df_clean.apply(value_score, axis=1)

def is_recommended(row):
    if row['rating_numeric'] >= 4 and row['affordability_score'] >= 5:
        return 'Yes'
    return 'No'

df_clean['recommended'] = df_clean.apply(is_recommended, axis=1)

print()
print("DATA CLEANING SUMMARY-")
print()

print(f"\nFinal records: {len(df_clean)}")
print(f"Price range: {df_clean['price_numeric'].min():.2f} - {df_clean['price_numeric'].max():.2f}")
print(f"Average rating: {df_clean['rating_numeric'].mean():.1f}/5")
print(f"Average description length: {df_clean['description_word_count'].mean():.0f} words")

print(f"\nPrice Bands:")
print(df_clean['price_band'].value_counts())

print(f"\nRating Distribution:")
print(df_clean['rating_numeric'].value_counts().sort_index())

print(f"\nAverage price by price_band:")
print(df_clean.groupby('price_band')['price_numeric'].mean().round(2))

print(f"\nAverage rating by price_band:")
print(df_clean.groupby('price_band')['rating_numeric'].mean().round(2))

print()
print("TOP 10 BEST VALUE BOOKS (High Rating, Low Price)-")
print()

best_deals = df_clean.nlargest(10, 'value_score')[['title', 'category', 'price_numeric', 'rating_numeric', 'value_score', 'recommended']]
for idx, row in best_deals.iterrows():
    print(f"{row['title'][:40]:<40} | {row['price_numeric']:>6.2f} | {row['rating_numeric']} | Value: {row['value_score']:.1f}")

print()
print("CATEGORY STATISTICS-")
print()

cat_stats = df_clean.groupby('category').agg({
    'title': 'count',
    'price_numeric': 'mean',
    'rating_numeric': 'mean',
    'value_score': 'mean'
}).round(2).sort_values('title', ascending=False)

cat_stats.columns = ['Count', 'Avg Price', 'Avg Rating', 'Avg Value Score']
print(cat_stats.head(10))

output_columns = [
    'page', 'product_url', 'title', 'category', 
    'price_numeric', 'rating_numeric', 'stock_count',
    'price_band', 'affordability_score', 'value_score', 'recommended',
    'description_word_count', 'description'
]

df_final = df_clean[output_columns]

df_final.columns = [
    'Page', 'URL', 'Title', 'Category',
    'Price', 'Rating', 'Stock Count',
    'Price Band', 'Affordability Score', 'Value Score', 'Recommended',
    'Description (Words)', 'Description'
]

df_final.to_csv('scraped_cleaned.csv', index=False, encoding='utf-8')
print(f"\nSaved cleaned data to: books_cleaned.csv")

print()
print("PREVIEW OF CLEANED DATA-")
print()

preview_cols = ['Title', 'Category', 'Price', 'Rating', 'Price Band', 'Value Score', 'Recommended']
print(df_final[preview_cols].head(10).to_string(index=False))