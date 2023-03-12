# LaptopPrice-Predictor-2023-BD
### Laptop Price Prediction Model
This project aims to predict the prices of laptops in Bangladesh in 2023. The machine learning model was built using XGBoost regressor and trained on the current prices of laptops collected from various Bangladeshi e-commerce sites. The data was collected through web scraping using Python's Beautiful Soup library, which took 5 days for scraping and cleaning. After performing exploratory data analysis, data preprocessing, and feature engineering, the XGBoost regressor was selected as the best model through cross-fold validation and GridSearchCV. The model was saved using Pickle, and a web application was created using Flask and hosted on Render.

## Data Sources
The following e-commerce sites were scraped for collecting the laptop price data:

* https://www.startech.com.bd/laptop-notebook
* https://www.ryanscomputers.com/category/laptop-all-laptop
* https://www.techlandbd.com/shop-laptop-computer/brand-laptops


## Libraries used
* Python (version x.x.x)
* Beautiful Soup (version x.x.x)
* Pandas (version x.x.x)
* NumPy (version x.x.x)
* Scikit-learn (version x.x.x)
* XGBoost (version x.x.x)
* Flask (version x.x.x)
* Pickle (version x.x.x)


## How to Use
## On Local Machine
* Clone the repository to your local machine
* Run the Flask application using the command python app.py
* Access the web application on your browser by visiting http://localhost:5000/

## Online
* Access the web application by visiting https://example.com/
