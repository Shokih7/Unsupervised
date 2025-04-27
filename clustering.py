import gower
from sklearn.cluster import SpectralClustering, AgglomerativeClustering, KMeans
from grouping import *
from sklearn.preprocessing import StandardScaler
from sklearn.mixture import GaussianMixture
from fcmeans import FCM
from kmodes.kmodes import KModes
from sklearn.decomposition import TruncatedSVD
from sklearn.decomposition import PCA
from sklearn.decomposition import FastICA
from sklearn.manifold import MDS

scaler = StandardScaler()


class Clustering:

    def __init__(self,df):
        self.df = df
        self.X_con_habits = df[habits_features]
        self.X_con_mental = df[mental_features]
        self.X_con_all = df[features_for_clustering]
        self.X_con_habits_scaled = scaler.fit_transform(self.X_con_habits)
        self.X_con_all_scaled = scaler.fit_transform(self.X_con_all)
        self.X_con_mental_scaled = scaler.fit_transform(self.X_con_mental)
        #habits
        self.gower_dist_matrix = gower.gower_matrix(self.X_con_habits)
        # Similarity = 1 - distance
        self.gower_sim_matrix = 1 - self.gower_dist_matrix
        self.clus()
        self.dim()

        # Step 3: Apply Spectral Clustering
    def clus(self):
        sc = SpectralClustering(n_clusters=4, affinity='precomputed', random_state=42)
        self.df['spec_cluster_habits'] = sc.fit_predict(self.gower_sim_matrix)

        # Clustering
        spectral = SpectralClustering(n_clusters=4, affinity='nearest_neighbors', assign_labels='kmeans', random_state=42)
        self.df['spec_cluster_mental'] = spectral.fit_predict(self.X_con_mental_scaled)
        self.df['spec_cluster_all'] = spectral.fit_predict(self.X_con_all_scaled)

        """###Prim"""

        prim_cluster = AgglomerativeClustering(n_clusters=4, metric='euclidean', linkage='ward')
        self.df['prim_habits_cluster'] = prim_cluster.fit_predict(self.X_con_habits_scaled)
        self.df['prim_mental_cluster'] = prim_cluster.fit_predict(self.X_con_mental_scaled)
        self.df['prim_all_cluster'] = prim_cluster.fit_predict(self.X_con_all_scaled)

        """###GMM"""

        gmm = GaussianMixture(n_components=4, random_state=42)
        self.df['gmm_cluster_habits'] = gmm.fit_predict(self.X_con_habits_scaled)
        self.df['gmm_cluster_mental'] = gmm.fit_predict(self.X_con_mental_scaled)
        self.df['gmm_cluster_all'] = gmm.fit_predict(self.X_con_all_scaled)

        """###FCM"""

        fcm = FCM(n_clusters=4, random_state=42)
        fcm.fit(self.X_con_habits_scaled)
        self.df['fcm_habits'] = fcm.predict(self.X_con_habits_scaled)

        fcm = FCM(n_clusters=4, random_state=42)
        fcm.fit(self.X_con_mental_scaled)
        self.df['fcm_mental'] = fcm.predict(self.X_con_mental_scaled)

        fcm = FCM(n_clusters=4, random_state=42)
        fcm.fit(self.X_con_all_scaled)
        self.df['fcm_all'] = fcm.predict(self.X_con_all_scaled)

        """###Kmeans"""

        kmeans = KMeans(n_clusters=4, random_state=42)
        kmeans.fit(self.X_con_habits_scaled)
        self.df['kmeans_habits'] = kmeans.predict(self.X_con_habits_scaled)
        kmeans = KMeans(n_clusters=4, random_state=42)
        kmeans.fit(self.X_con_mental_scaled)
        self.df['kmeans_mental'] = kmeans.predict(self.X_con_mental_scaled)
        kmeans = KMeans(n_clusters=4, random_state=42)
        kmeans.fit(self.X_con_all_scaled)
        self.df['kmeans_all'] = kmeans.predict(self.X_con_all_scaled)

        """###Categorial"""

        # Select categorical features
        X_categorical = self.df[cat_habits]
        # Apply K-Modes clustering
        kmodes_model = KModes(n_clusters=4, init='Huang', n_init=10, verbose=1) # You can adjust n_clusters
        self.df['spec_kmodes_habits'] = kmodes_model.fit_predict(X_categorical)

        # Select categorical features
        X_categorical = self.df[genre]
        # Apply K-Modes clustering
        kmodes_model = KModes(n_clusters=4, init='Huang', n_init=10, verbose=1) # You can adjust n_clusters
        self.df['spec_kmodes_genre'] = kmodes_model.fit_predict(X_categorical)

        # Select categorical features
        X_categorical = self.df[cat_features]
        # Apply K-Modes clustering
        kmodes_model = KModes(n_clusters=4, init='Huang', n_init=10, verbose=1) # You can adjust n_clusters
        self.df['spec_kmodes_all'] = kmodes_model.fit_predict(X_categorical)

    def dim(self):
        #Visualization- Dimentions
        ###SVD
        # habits
        svd = TruncatedSVD(n_components=2)  # Reduce to 2 dimensions for visualization
        X_svd = svd.fit_transform(self.X_con_habits_scaled)
        X_svd_list = [tuple(row) for row in X_svd]
        self.df['SVD_habits'] = X_svd_list

        # mental
        svd = TruncatedSVD(n_components=2)  # Reduce to 2 dimensions for visualization
        X_svd = svd.fit_transform(self.X_con_mental_scaled)
        X_svd_list = [tuple(row) for row in X_svd]
        self.df['SVD_mental'] = X_svd_list

        # All
        svd = PCA(n_components=2)  # Reduce to 2 dimensions for visualization
        X_svd = svd.fit_transform(self.X_con_all_scaled)
        X_svd_list = [tuple(row) for row in X_svd]
        self.df['SVD_all'] = X_svd_list

        """###PCA"""

        # ##PCA
        pca = PCA(n_components=2)  # Reduce to 2 dimensions for visualization
        X_pca = pca.fit_transform(self.X_con_habits_scaled)
        X_pca_list = [tuple(row) for row in X_pca]
        self.df['PCA_habits'] = X_pca_list

        pca = PCA(n_components=2)  # Reduce to 2 dimensions for visualization
        X_pca = pca.fit_transform(self.X_con_mental_scaled)
        X_pca_list = [tuple(row) for row in X_pca]
        self.df['PCA_mental'] = X_pca_list

        pca = PCA(n_components=2)  # Reduce to 2 dimensions for visualization
        X_pca = pca.fit_transform(self.X_con_all_scaled)
        X_pca_list = [tuple(row) for row in X_pca]
        self.df['PCA_all'] = X_pca_list

        """###ICA"""

        ica = FastICA(n_components=2, random_state=42)  # Reduce to 2 dimensions for visualization
        X_ica = ica.fit_transform(self.X_con_habits_scaled)
        X_ica_list = [tuple(row) for row in X_ica]
        self.df['ICA_habits'] = X_ica_list

        ica = FastICA(n_components=2, random_state=42)  # Reduce to 2 dimensions for visualization
        X_ica = ica.fit_transform(self.X_con_mental_scaled)
        X_ica_list = [tuple(row) for row in X_ica]
        self.df['ICA_mental'] = X_ica_list

        ica = FastICA(n_components=2, random_state=42)  # Reduce to 2 dimensions for visualization
        X_ica = ica.fit_transform(self.X_con_all_scaled)
        X_ica_list = [tuple(row) for row in X_ica]
        self.df['ICA_all'] = X_ica_list

        """###MDS"""

        mds = MDS(n_components=2, random_state=42)
        X_mds = mds.fit_transform(self.X_con_habits_scaled)
        X_mds_list = [tuple(row) for row in X_mds]
        self.df['MDS_habits'] = X_mds_list

        mds = MDS(n_components=2, random_state=42)
        X_mds = mds.fit_transform(self.X_con_mental_scaled)
        X_mds_list = [tuple(row) for row in X_mds]
        self.df['MDS_mental'] = X_mds_list

        mds = MDS(n_components=2, random_state=42)
        X_mds = mds.fit_transform(self.X_con_all_scaled)
        X_mds_list = [tuple(row) for row in X_mds]
        self.df['MDS_all'] = X_mds_list