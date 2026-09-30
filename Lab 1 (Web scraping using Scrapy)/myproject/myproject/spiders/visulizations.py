import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

df = pd.read_csv('scraped_raw.csv')

print(df.columns.tolist())

df['price'] = df['price'].astype(str).str.replace(r'[^\d.]', '', regex=True).astype(float)

rating_map = {
    'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5,
    'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5
}
df['rating'] = df['rating'].astype(str).map(rating_map)

df['availability'] = df['availability'].astype(str).str.extract(r'(\d+)').astype(float)

sns.set_style("whitegrid")

plt.figure(figsize=(10, 6))
sns.histplot(df['price'], bins=20, kde=True)
plt.title('Distribution of Book Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(8, 5))
sns.countplot(x='rating', data=df, palette='viridis')
plt.title('Distribution of Book Ratings')
plt.xlabel('Star Rating')
plt.ylabel('Number of Books')
plt.show()

plt.figure(figsize=(12, 6))
category_avg = df.groupby('category')['price'].mean().sort_values(ascending=False)
sns.barplot(x=category_avg.values, y=category_avg.index, palette='magma')
plt.title('Average Price by Category')
plt.xlabel('Average Price')
plt.ylabel('Category')
plt.show()

plt.figure(figsize=(8, 6))
sns.boxplot(x='rating', y='price', data=df, palette='Set2')
plt.title('Price Distribution by Rating')
plt.xlabel('Star Rating')
plt.ylabel('Price')
plt.show()

text = " ".join(description for description in df['Description'].dropna().astype(str))
wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='viridis').generate(text)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud from Book Descriptions')
plt.show()

print(df[['price', 'rating', 'availability']].describe())

print(df.isnull().sum())

print(df['Category'].value_counts().head(5))

print(df[df['rating'] == 5][['Title', 'price', 'Category']].head())

print(df.sort_values(by='availability', ascending=False)[['Title', 'availability']].head(5))