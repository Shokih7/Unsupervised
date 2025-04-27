features_for_clustering = ['Age', 'Hours per day', 'BPM', 'Anxiety', 'Depression', 'Insomnia', 'OCD'] #continuis

all_features            = ['Age', 'Primary streaming service', 'Hours per day',
                           'While working', 'Instrumentalist', 'Composer', 'Fav genre',
                           'Exploratory', 'Foreign languages', 'BPM', 'Classical F Indicator',
                           'Country F Indicator', 'EDM F Indicator', 'Folk F Indicator',
                           'Gospel F Indicator', 'Hip hop F Indicator', 'Jazz F Indicator',
                           'K pop F Indicator', 'Latin F Indicator', 'Lofi F Indicator',
                           'Metal F Indicator', 'Pop F Indicator', 'R&B F Indicator',
                           'Rap F Indicator', 'Rock F Indicator', 'Video game music F Indicator'
                           'Anxiety', 'Depression', 'Insomnia', 'OCD', 'Music effects']

cat_features            = ['Primary streaming service', 'While working', 'Instrumentalist',
                           'Composer', 'Composer Indicator','Fav genre', 'Exploratory',
                           'Foreign languages','Frequency [Classical]','Frequency [Country]',
                           'Frequency [EDM]', 'Frequency [Folk]', 'Frequency [Gospel]',
                           'Frequency [Hip hop]', 'Frequency [Jazz]', 'Frequency [K pop]',
                           'Frequency [Latin]', 'Frequency [Lofi]','Frequency [Metal]',
                           'Frequency [Pop]',  'Frequency [R&B]', 'Frequency [Rap]',
                           'Frequency [Rock]', 'Frequency [Video game music]', 'Music effects']

genre                   = ['Fav genre', 'Foreign languages','Frequency [Classical]',
                           'Frequency [Country]', 'Frequency [EDM]', 'Frequency [Folk]',
                           'Frequency [Gospel]', 'Frequency [Hip hop]', 'Frequency [Jazz]',
                           'Frequency [K pop]', 'Frequency [Latin]', 'Frequency [Lofi]',
                           'Frequency [Metal]', 'Frequency [Pop]',  'Frequency [R&B]',
                           'Frequency [Rap]','Frequency [Rock]', 'Frequency [Video game music]']

genre_indicators        = ['Classical F Indicator', 'Country F Indicator', 'EDM F Indicator',
                           'Folk F Indicator', 'Gospel F Indicator', 'Hip hop F Indicator',
                           'Jazz F Indicator',  'K pop F Indicator', 'Latin F Indicator',
                           'Lofi F Indicator', 'Metal F Indicator', 'Pop F Indicator',
                           'R&B F Indicator',  'Rap F Indicator', 'Rock F Indicator',
                           'Video game music F Indicator']

mental_features         = ['Anxiety', 'Depression', 'Insomnia', 'OCD']

habits_features         = ['Age', 'Hours per day', 'While working Indicator', 'BPM']

cat_habits              = ['Primary streaming service', 'While working', 'Instrumentalist',
                           'Composer', 'Fav genre', 'Exploratory',
                           'Foreign languages','Music effects']

genre_indicators        = ['Classical F Indicator', 'Country F Indicator', 'EDM F Indicator',
                           'Folk F Indicator', 'Gospel F Indicator', 'Hip hop F Indicator',
                           'Jazz F Indicator', 'K pop F Indicator', 'Latin F Indicator',
                           'Lofi F Indicator', 'Metal F Indicator', 'Pop F Indicator',
                           'R&B F Indicator', 'Rap F Indicator', 'Rock F Indicator',
                           'Video game music F Indicator']

class_groups = {'habits': ['spec_cluster_habits', 'prim_habits_cluster', 'gmm_cluster_habits', 'fcm_habits', 'kmeans_habits', 'spec_kmodes_habits'],
                'mental': ['spec_cluster_mental', 'prim_mental_cluster', 'gmm_cluster_mental', 'fcm_mental','kmeans_mental', 'spec_kmodes_genre'],
                'all': ['spec_cluster_all', 'prim_all_cluster', 'gmm_cluster_all', 'fcm_all', 'kmeans_all', 'spec_kmodes_all']
                }

fet1 = ['Age', 'Hours per day', 'While working', 'BPM']
fet2 = ['Gospel F Indicator','K pop F Indicator', 'Latin F Indicator', 'Lofi F Indicator',]
fet3 = mental_features
intresting = [fet2, fet3]

reduction_methods = ['SVD', 'PCA', 'ICA', 'MDS']
groups = ['habits', 'mental', 'all']
