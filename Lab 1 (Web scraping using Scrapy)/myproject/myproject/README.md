# Books to Scrape - Data Analysis Project

## Project Overview

This project involves web scraping book data from [Books to Scrape](https://books.toscrape.com/), performing data cleaning and transformation, and creating visualizations to gain insights into book pricing, ratings, and categories.

## Project Files

### 1. Spider (spider.py)

The Scrapy spider that crawls the website and extracts book details.

**Key Features:**
- Scrapes up to 5 pages of books
- Extracts book details including title, price, rating, availability, description, UPC, and category
- Follows product links for detailed information

### 2. Data Processing (data_processing.py)

Python script that cleans and transforms the scraped data.

**Key Features:**
- Removes duplicate records based on UPC
- Standardizes text fields (title, category, rating, availability)
- Extracts stock count from availability text
- Converts text ratings to numeric values
- Calculates additional metrics:
  - Affordability score
  - Value score (combination of rating and price)
  - Recommendation status
- Creates price bands and word counts for descriptions

### 3. Visualization (visualizations.py)

Python script that generates visualizations from the cleaned data.

**Key Visualizations:**
1. Distribution of Book Prices (Histogram)
2. Distribution of Book Ratings (Count Plot)
3. Average Price by Category (Bar Chart)
4. Price Distribution by Rating (Box Plot)
5. Word Cloud from Book Descriptions

## Dataset Overview

The scraped dataset contains information about 100 books across multiple categories.

### Sample Data

| Title | Category | Price | Rating | Availability |
|-------|----------|-------|--------|--------------|
| It's Only the Himalayas | Travel | 45.17 | 2 | In stock |
| Libertarianism for Beginners | Politics | 51.33 | 2 | In stock |
| Mesaerion: The Best Science Fiction Stories 1800-1849 | Science Fiction | 37.59 | 1 | In stock |
| Olio | Poetry | 23.88 | 1 | In stock |
| Our Band Could Be Your Life | Music | 57.25 | 3 | In stock |

## Analysis Results

### Price Distribution

![Price Distribution](image.png)

The distribution of book prices shows:
- Most books are priced between £20-£40
- There are several books in the higher price range (£50-£60)
- Average book price is approximately £35
- Price range spans from £10 to £58

### Rating Distribution

![Rating Distribution](image.png)

Key insights:
- Most books have 3 or 5-star ratings
- 1-star and 2-star ratings are less common
- The dataset has a good spread of ratings, though 3-star books are most frequent

### Average Price by Category

![Average Price by Category]

Top 5 most expensive categories:

| Category | Average Price |
|----------|---------------|
| Historical Fiction | ~£48 |
| Politics | ~£47 |
| Childrens | ~£46 |
| Health | ~£45 |
| Self Help | ~£44 |

### Price by Rating

![Price by Rating](image.png)

Observations:
- Higher-rated books (4-5 stars) show a wider price range
- 1-star books have a relatively high median price
- Books with 5-star ratings appear at all price points
- No clear correlation between price and rating

### Description Word Cloud

![Word Cloud](image.png)

The most common words in book descriptions include:
- Life
- Story
- World
- Love
- New
- Time
- Book
- Years
- People
- Work

## Key Insights

### 1. Price Distribution
- **Most books** fall in the £20-£40 range
- **Premium books** (>£50) are less common but present
- **Budget books** (<£15) are rare in this dataset

### 2. Category Insights
- **Historical Fiction** and **Politics** tend to be the most expensive categories
- **Spirituality** and **Young Adult** tend to be more affordable
- Categories like **Science Fiction**, **Poetry**, and **Music** show moderate pricing

### 3. Rating Analysis
- 3-star and 5-star books are most common
- 1-star books tend to have higher prices, suggesting price doesn't guarantee quality
- The "sweet spot" for good value appears to be in the £20-£40 range with 4-5 star ratings

### 4. Recommendations
Based on the analysis, the best value books (high rating, low price) include:
- Books in the Young Adult and Spirituality categories
- Books priced under £20 with 4+ star ratings
- Budget-friendly categories like Poetry and Thriller

## Data Quality Notes

1. **Missing Descriptions**: Some books had missing descriptions, which were filled with "No description available"
2. **Duplicate Removal**: Duplicates were removed based on UPC
3. **Rating Standardization**: Text ratings (One, Two, etc.) were converted to numeric values (1-5)
4. **Price Cleaning**: Currency symbols and commas were removed for numerical analysis

## Technical Specifications

- **Scraping Tool**: Scrapy Framework
- **Data Processing**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn, WordCloud
- **Data Format**: CSV
- **Total Records**: 100 books
- **Categories**: 24 unique categories

## Conclusion

This analysis reveals a diverse book market with:
- Prices ranging from £10 to £58
- A variety of categories with different price points
- No strong correlation between price and rating
- Several categories offering good value (affordable prices with high ratings)

The cleaned and enhanced dataset can be used for further analysis, including:
- Building recommendation systems
- Price prediction models
- Category-based trend analysis
- Customer preference studies