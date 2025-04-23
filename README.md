# 📊 EDA Visual Explorer

---

## 🚀 Goal

By the end of this project, you'll have a comprehensive comparison of various Python plotting tools, an understanding of which visuals suit which data types, and a reusable EDA toolkit for future data science projects.

## Project Description

EDA Visual Explorer is a project aimed at exploring and comparing various Python tools and libraries used for visualizing data, specifically in the context of Exploratory Data Analysis (EDA). The core objective is to understand which plotting techniques are most suitable for different types and structures of data.

The project follows a stepwise approach, beginning with simple, one-column DataFrames and gradually moving to more complex, multi-column datasets. At each stage, the focus is on using appropriate visual representations that are compatible with the data type and structure.

---

## 🔍 Workflow

### 1. Phase 1: One-Column DataFrames
Explore basic plots using popular visualization libraries such as `matplotlib`, `seaborn`, and `plotly` based on data types:

- **Numerical (int, float)**: Histogram, Box plot, KDE plot.
- **Categorical (object, category)**: Count plot / Bar plot, Pie chart.
- **Date/Time (datetime)**: Line plot (over time), Histogram with time bins.

### 2. Phase 2: Two-Column DataFrames
Explore relationships between two variables:

- **Numerical vs Numerical**: Scatter plot, Hexbin plot.
- **Categorical vs Numerical**: Box plot, Violin plot.
- **Categorical vs Categorical**: Grouped bar plot, Heatmap (frequency).

### 3. Phase 3: Multi-Column DataFrames
Explore high-dimensional data representations:

- Pair plots.
- Correlation heatmaps.
- Parallel coordinates.
- Interactive dashboards (e.g., using `Plotly Dash` or `Streamlit`).

---

## 📦 Libraries Explored

- `matplotlib`
- `seaborn`
- `plotly`
- `pandas` (for basic plotting)
- `altair`
- `bokeh`
- `missingno` (for missing data visualization)
- `sweetviz` / `pandas-profiling` (for automated EDA)

---

## 📁 Folder Structure

