# Skillset
## 📊 EDA Visual Explorer
### 🚀 Goal
By the end of this project, we'll have a comprehensive comparison of various Python plotting tools, an understanding of which visuals suit which data types, and a reusable EDA toolkit for future data science projects.

### Project Description:
EDA Visual Explorer is a project aimed at exploring and comparing various Python tools and libraries used for visualizing data, specifically in the context of Exploratory Data Analysis (EDA). The core objective is to understand which plotting techniques are most suitable for different types and structures of data.

The project follows a stepwise approach, beginning with simple, one-column DataFrames and gradually moving to more complex, multi-column datasets. At each stage, the focus is on using appropriate visual representations that are compatible with the data type and structure.

### 🔍 Workflow
### Phase 1: One-Column DataFrames
Explore basic plots using popular visualization libraries such as matplotlib, seaborn, and plotly based on data types:

  #### a) Numerical (int, float):
        1. Histogram
        2. Box plot
        3. KDE plot
  #### b) Categorical (object, category):
        1. Count plot/Bar plot
        2. Pie chart
 #### c) Date/Time (datetime):
       `1. Line plot (over time)
        2. Histogram with time bins
        
### Pgase 2: Two-Column DataFrames
Explore relationships between two variables

  #### a) Numerical vs Numerical:
        1. Scatter plot
        2. Hexbin plot
  #### b) Categorical vs Numerical:
        1. Box plot
        2. Violin plot
 #### c) Categorical vs Categorical:
       `1. Grouped bar plot
        2. Heatmap (frequency)

### Phase 3: Multi-Column DataFrames
        Pair plots
        Correlation heatmaps
        Parallel coordinates
        Interactive dashboards (e.g., using Plotly Dash or Streamlit)
        
### 📦 Libraries Explored
        matplotlib
        seaborn
        plotly
        pandas (for basic plotting)
        altair
        bokeh
        missingno (for missing data visualization)
        sweetviz / pandas-profiling (for automated EDA)

