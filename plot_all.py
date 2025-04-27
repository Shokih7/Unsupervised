from grouping import *
import seaborn as sns
import matplotlib.pyplot as plt

class PlotAll:

    def __init__(self, df):
        self.df = df
        self.pink_palette = sns.color_palette("RdPu", n_colors=len(self.df['spec_cluster_habits'].unique())) # Example, adjust n_colors as needed
        self.plot_clusters()
        self.plot_dim()

    def plot_clusters(self):
        for group_name, cluster_cols in class_groups.items():
            for feature in all_features:
                fig, axes = plt.subplots(1, len(cluster_cols), figsize=(25, 5), sharey=True)
                fig.suptitle(f'Feature: {feature}, Clustering by {group_name}')

                for i, col in enumerate(cluster_cols):
                    sns.swarmplot(ax=axes[i], x=col, y=feature, data=self.df, size=5, palette=self.pink_palette, )
                    axes[i].set_title(f'Cluster: {col}')
                    axes[i].set_xlabel(col)
                    axes[i].set_ylabel(feature)

                plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Adjust layout to prevent title overlap
                plt.show()

    def plot_dim(self):
        for group in groups:
            for method in reduction_methods:
                fig, axes = plt.subplots(1, len(class_groups[group]), figsize=(25, 5))
                fig.suptitle(f'{method} Dimensionality Reduction for {group} Clusters')

                for i, col in enumerate(class_groups[group]):
                    # Extract x and y coordinates from the tuple
                    self.df['x'] = self.df[f'{method}_{group}'].apply(lambda x: x[0])
                    self.df['y'] = self.df[f'{method}_{group}'].apply(lambda x: x[1])

                    sns.scatterplot(ax=axes[i], x='x', y='y', hue=col, data=self.df, palette=pink_palette,
                                    s=50)  # Increased point size
                    axes[i].set_title(f'Cluster: {col}')
                    axes[i].set_xlabel(f'{method}_x')
                    axes[i].set_ylabel(f'{method}_y')

                    # Clean up the x and y columns
                    self.df.drop(['x', 'y'], axis=1, inplace=True)

                plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Adjust layout
                plt.show()