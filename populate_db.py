import sqlite3

def populate_table(table_name, data):
    conn = sqlite3.connect('quiz_bowl.db')
    cursor = conn.cursor()
    cursor.executemany(f'INSERT INTO {table_name} (question, answer) VALUES (?, ?)', data)
    conn.commit()
    conn.close()

# Create questions and answers
business_strategy = [
    ('What business strategy framework was introduced by Michael Porter in 1979?','Porter'),
    ('What is the term for the strategy involving the development and introduction of new products or services into existing markets?', 'Diversification'),
    ('In business strategy, what does the \"S\" in SWOT stand for?', 'Strength'),
    ('What strategy involves a company lowering its prices to gain market share rapidly?', 'Penetration'),
    ('Which strategic planning tool visualizes the competitive positions of companies in an industry?', 'Boston Matrix'),
    ('What is the strategy where a company focuses on serving a specific segment of the market?', 'Niche'),
    ('Which strategy focuses on reducing costs through efficient production and distribution processes?', 'Cost Leadership'),
    ('What is the term for a strategic alliance between two or more companies to achieve a common objective?', 'Partnership'),
    ('What is the strategic approach that aims to create a unique and valuable position in the market?', 'Differentiation'),
    ('What strategy involves a company expanding its operations into new markets or industries?', 'Expansion')
]

entrepreneurship = [
    ('Who is often regarded as the \"father of modern entrepreneurship\"?', 'Schumpeter'),
    ('What term describes a business model that seeks to address a social or environmental issue while generating profit?', 'Social'),
    ('Which Silicon Valley entrepreneur co-founded PayPal and later became the CEO of Tesla and SpaceX?', 'Elon Musk'),
    ('What is the term for a small amount of money invested in a startup in exchange for ownership equity?', 'Seed'),
    ('What is the name of the phenomenon where entrepreneurs take failed ideas or businesses and turn them into successful ventures?', 'Pivot'),
    ('What term describes the practice of bringing together resources to start a business venture?', 'Bootstrapping'),
    ('Which entrepreneur famously dropped out of college to co-found Microsoft?', 'Gates'),
    ('What is the term for the process of strategically choosing which markets to enter with a new product or service?', 'Market'),
    ('What is the name of the entrepreneur who co-founded Airbnb?', 'Chesky'),
    ('What term describes the strategy of rapidly scaling a business by reinvesting profits rather than seeking external funding?', 'Organic')
]

business_ethics = [
    ('What term refers to the ethical principle of being honest and truthful in business dealings?', 'Integrity'),
    ('What is the term for a situation where a person or entity has a conflict of interest between personal and professional duties?', 'Dilemma'),
    ('Which ethical principle emphasizes treating others fairly and justly in business transactions?', 'Equity'),
    ('What term describes the ethical responsibility of businesses to contribute positively to society and the environment?', 'Social'),
    ('What is the term for the practice of disclosing information that could influence a business transaction?', 'Transparency'),
    ('Which ethical theory emphasizes the importance of maximizing overall happiness or well-being?', 'Utilitarianism'),
    ('What is the term for the unethical practice of using one\'s position or power for personal gain', 'Corruption'),
    ('Which ethical principle emphasizes the importance of keeping promises and fulfilling obligations?', 'Fidelity'),
    ('What is the term for the systematic evaluation of a company\'s activities and their impact on society and the environment?', 'Sustainability'),
    ('What ethical theory suggests that ethical decisions should be based on fundamental principles of right and wrong?', 'Deontology')
]

business_analytics = [
    ('What is the term for the process of analyzing historical data to predict future outcomes?', 'Forecasting'),
    ('What statistical measure is used to describe the dispersion or spread of data points in a dataset?', 'Variance'),
    ('What term describes the technique of using algorithms to extract patterns and insights from large datasets?', 'Data Mining'),
    ('What is the name of the statistical method used to identify relationships between variables in a dataset?', 'Regression'),
    ('What term refers to the process of cleaning and organizing data before analysis?', 'Data Preprocessing'),
    ('Which type of analysis involves categorizing data into groups or clusters based on similarity?', 'Clustering'),
    ('What is the name of the technique used to visualize data and identify patterns through graphical representations?', 'Data Visualization'),
    ('What statistical measure represents the central tendency of a dataset?', 'Mean'),
    ('What is the term for the process of identifying and correcting errors in data?', 'Data Cleansing'),
    ('What type of analysis focuses on identifying the factors that contribute most to a particular outcome?', 'Factorial')
]

econometrics = [
    ('What statistical technique is commonly used to estimate the relationship between variables in econometrics?', 'Regression'),
    ('What is the term for the phenomenon where a change in one variable causes a change in another variable?', 'Causality'),
    ('Which econometric model is used when the dependent variable is binary or categorical?', 'Logit'),
    ('What is the name of the method used in econometrics to correct for autocorrelation in time series data?', 'ARIMA'),
    ('What term describes the situation where the error term in a regression model has a mean of zero?', 'Homoscedasticity'),
    ('What type of analysis involves estimating the effect of one variable on another while holding other variables constant?', 'Partial'),
    ('What is the name of the econometric technique used to estimate the joint effect of multiple independent variables on a dependent variable?', 'Multiple Regression'),
    ('What term refers to the problem of using past data to predict future outcomes in econometrics?', 'Forecasting'),
    ('Which statistical test is used to determine whether there is a significant relationship between the independent and dependent variables in a regression model?', 'T-test'),
    ('What is the term for the method used to estimate parameters in a regression model by minimizing the sum of squared differences between observed and predicted values?', 'Least Squares')
]

# Populate tables with questions and answers
populate_table('BusinessStrategy', business_strategy)
populate_table('Entrepreneurship', entrepreneurship)
populate_table('BusinessEthics', business_ethics)
populate_table('BusinessAnalytics', business_analytics)
populate_table('Econometrics', econometrics)
