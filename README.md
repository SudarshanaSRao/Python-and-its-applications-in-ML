# [Project details](https://sudarshanasrao.github.io/portfolio/portfolio-9/)

# Single cell RNA sequencing
This project aimed to identify and rank important cells in a dataset taken from the neocortex region of a rat's brain, applying various machine learning techniques to reduce dimensionality and perform clustering and classification.

## Dataset
The dataset consists of 2,169 cells from the neocortex region of a rat's brain, each with features distributed across 20,000 columns. The dataset is available through the following [Google Drive link](https://drive.google.com/drive/folders/118RKqnAZyfG6aNkm9I-kByQvGSIX4Ak0?usp=sharing).

## Key Techniques
1. **Principal Component Analysis (PCA)**:
   - PCA was applied to reduce the 20,000 features to just 3-5 components, allowing us to retain most of the data's variability while simplifying the dataset for further processing.

2. **K-Means Clustering**:
   - K-means clustering was used to group the cells into different clusters based on their feature similarities. This helped in identifying patterns and grouping cells with similar properties.

3. **Logistic Regression**:
   - Logistic Regression was used to classify the cells and rank them in terms of their importance.

4. **3D Visualization**:
   - A dynamic 3D graph was used to visualize the output of the clustering and classification processes, allowing for easy interpretation of the results.

## Results and Accuracy
- **Accuracy**: The model achieved an accuracy of **89.8%** in identifying and ranking important cells within the dataset.
- **Visualization**: The dynamic 3D graph provided a clear view of how the cells were clustered and ranked, making the analysis more interpretable.

![clusters](https://github.com/SudarshanaSRao/Python-and-its-applications-in-ML/assets/87690830/d05f5769-7fee-4388-9d3f-620bff12942e)
