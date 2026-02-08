import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier, IsolationForest
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.feature_selection import SelectKBest, f_classif
import warnings

warnings.filterwarnings('ignore')

# ============== ЗАГРУЗКА РЕАЛЬНЫХ ДАННЫХ ==============
print("Инструкция по загрузке данных:")
print(
    "1. Скачайте датасет: https://archive.ics.uci.edu/ml/datasets/Activity+recognition+using+wearable+physiological+measurements")
print("2. Распакуйте архив")
print("3. Найдите файлы subject10X.dat в папке")
print("4. Поместите их в рабочую директорию\n")

import os
import urllib.request
import zipfile

# Попытка автоматической загрузки
try:
    print("Попытка загрузки данных...")
    # Альтернативный способ - загрузка из UCI репозитория
    url = "https://archive.ics.uci.edu/static/public/318/activity+recognition+using+wearable+physiological+measurements.zip"

    if not os.path.exists('dataset.zip'):
        print("Загрузка архива...")
        urllib.request.urlretrieve(url, 'dataset.zip')

    print("Распаковка...")
    with zipfile.ZipFile('dataset.zip', 'r') as zip_ref:
        zip_ref.extractall('dataset')

    print("Данные загружены!\n")
except Exception as e:
    print(f"Автоматическая загрузка не удалась: {e}")
    print("Используем синтетические данные для демонстрации работы алгоритма\n")


# Загрузка данных
def load_data():
    all_data = []

    # Попробуем разные пути
    possible_paths = [
        'dataset/',
        'dataset/Activity recognition using wearable physiological measurements/',
        './'
    ]

    files_found = False
    for base_path in possible_paths:
        for i in range(101, 109):
            file_path = f'{base_path}subject{i}.dat'
            if os.path.exists(file_path):
                files_found = True
                df = pd.read_csv(file_path, sep='\s+', header=None)
                all_data.append(df)
                print(f"Загружен {file_path}")

    if not files_found:
        print("Реальные данные не найдены. Создаем синтетический датасет...")
        # Создаем более реалистичные данные
        np.random.seed(42)
        for activity in range(1, 8):
            # 18 признаков: физиологические данные
            n_samples = 1000
            X_activity = np.random.randn(n_samples, 18) * activity + activity * 2
            y_activity = np.full(n_samples, activity)
            df = pd.DataFrame(np.column_stack([X_activity, y_activity]))
            all_data.append(df)

    data = pd.concat(all_data, ignore_index=True)
    X = data.iloc[:, :-1].values
    y = data.iloc[:, -1].values.astype(int)

    return X, y


X, y = load_data()

# Масштабирование
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print(f"\nРазмер данных: {X.shape}")
print(f"Количество образцов: {len(y)}")
print(f"Количество признаков: {X.shape[1]}")
print(f"Классы активностей: {np.unique(y)}")
print(f"Распределение классов:")
for cls in np.unique(y):
    print(f"  Класс {cls}: {np.sum(y == cls)} образцов")

# ============== ЗАДАНИЕ 1 ==============
print("\n" + "=" * 70)
print("ЗАДАНИЕ 1: Классификация тремя методами с подбором параметров")
print("=" * 70)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.3, random_state=42, stratify=y
)

# 1) k-ближайших соседей
print("\n1) K-NEAREST NEIGHBORS (KNN)")
print("-" * 70)
param_grid_knn = {'n_neighbors': [3, 5, 7, 9, 11, 15]}
knn = KNeighborsClassifier()
grid_knn = GridSearchCV(knn, param_grid_knn, cv=5, scoring='accuracy', n_jobs=-1)
grid_knn.fit(X_train, y_train)

print(f"Лучшие параметры: {grid_knn.best_params_}")
print(f"Точность на кросс-валидации: {grid_knn.best_score_:.4f}")
y_pred_knn = grid_knn.predict(X_test)
acc_knn = accuracy_score(y_test, y_pred_knn)
print(f"Точность на тестовой выборке: {acc_knn:.4f}")

# 2) RandomForest
print("\n2) RANDOM FOREST")
print("-" * 70)
param_grid_rf = {
    'n_estimators': [50, 100, 200],
    'max_depth': [10, 20, None],
    'min_samples_split': [2, 5]
}
rf = RandomForestClassifier(random_state=42)
grid_rf = GridSearchCV(rf, param_grid_rf, cv=5, scoring='accuracy', n_jobs=-1)
grid_rf.fit(X_train, y_train)

print(f"Лучшие параметры: {grid_rf.best_params_}")
print(f"Точность на кросс-валидации: {grid_rf.best_score_:.4f}")
y_pred_rf = grid_rf.predict(X_test)
acc_rf = accuracy_score(y_test, y_pred_rf)
print(f"Точность на тестовой выборке: {acc_rf:.4f}")

# 3) SVM с RBF ядром
print("\n3) SVM С НЕЛИНЕЙНЫМ ЯДРОМ (RBF)")
print("-" * 70)
param_grid_svm = {
    'C': [0.1, 1, 10, 100],
    'gamma': ['scale', 'auto', 0.001, 0.01]
}
svm = SVC(kernel='rbf', random_state=42)
grid_svm = GridSearchCV(svm, param_grid_svm, cv=5, scoring='accuracy', n_jobs=-1)
grid_svm.fit(X_train, y_train)

print(f"Лучшие параметры: {grid_svm.best_params_}")
print(f"Точность на кросс-валидации: {grid_svm.best_score_:.4f}")
y_pred_svm = grid_svm.predict(X_test)
acc_svm = accuracy_score(y_test, y_pred_svm)
print(f"Точность на тестовой выборке: {acc_svm:.4f}")

# Анализ результатов задания 1
print("\n" + "=" * 70)
print("СРАВНЕНИЕ МЕТОДОВ (ЗАДАНИЕ 1)")
print("=" * 70)
results_1 = {
    'KNN': acc_knn,
    'RandomForest': acc_rf,
    'SVM': acc_svm
}
for model, acc in sorted(results_1.items(), key=lambda x: x[1], reverse=True):
    print(f"{model:15s}: {acc:.4f}")

best_model_1 = max(results_1, key=results_1.get)
print(f"\n>>> Лучший метод: {best_model_1} с точностью {results_1[best_model_1]:.4f}")

# ============== ЗАДАНИЕ 2 ==============
print("\n\n" + "=" * 70)
print("ЗАДАНИЕ 2: Очистка данных")
print("=" * 70)

# Разделение 50/50
X_train_full, X_test_full, y_train_full, y_test_full = train_test_split(
    X_scaled, y, test_size=0.5, random_state=42, stratify=y
)

print(f"\nОбучающая выборка: {X_train_full.shape[0]} образцов")
print(f"Контрольная выборка: {X_test_full.shape[0]} образцов")


# Функции очистки
def remove_noise(X, y, contamination=0.1):
    """Удаление шумовых объектов"""
    iso = IsolationForest(contamination=contamination, random_state=42)
    predictions = iso.fit_predict(X)
    mask = predictions == 1
    print(f"  Удалено шумовых объектов: {np.sum(~mask)}/{len(y)}")
    return X[mask], y[mask]


def remove_features(X, y, k=12):
    """Отбор информативных признаков"""
    selector = SelectKBest(f_classif, k=k)
    X_new = selector.fit_transform(X, y)
    print(f"  Отобрано признаков: {k}/{X.shape[1]}")
    return X_new, selector


def train_and_evaluate(X_train, y_train, X_test, y_test, title=""):
    """Обучение всех моделей и оценка"""
    results = {}

    knn = KNeighborsClassifier(**grid_knn.best_params_)
    knn.fit(X_train, y_train)
    results['KNN'] = accuracy_score(y_test, knn.predict(X_test))

    rf = RandomForestClassifier(**grid_rf.best_params_, random_state=42)
    rf.fit(X_train, y_train)
    results['RandomForest'] = accuracy_score(y_test, rf.predict(X_test))

    svm = SVC(**grid_svm.best_params_, random_state=42)
    svm.fit(X_train, y_train)
    results['SVM'] = accuracy_score(y_test, svm.predict(X_test))

    return results


# 1) Неочищенные данные
print("\n1) НЕОЧИЩЕННЫЕ ДАННЫЕ")
print("-" * 70)
results_raw = train_and_evaluate(X_train_full, y_train_full, X_test_full, y_test_full)
for model, acc in results_raw.items():
    print(f"{model:15s}: {acc:.4f}")

# 2) Сначала объекты, потом признаки
print("\n2) ОЧИСТКА: Объекты → Признаки")
print("-" * 70)
X_tr_no_noise, y_tr_no_noise = remove_noise(X_train_full, y_train_full)
X_tr_clean1, selector1 = remove_features(X_tr_no_noise, y_tr_no_noise)
X_te_clean1 = selector1.transform(X_test_full)
results_obj_feat = train_and_evaluate(X_tr_clean1, y_tr_no_noise, X_te_clean1, y_test_full)
for model, acc in results_obj_feat.items():
    print(f"{model:15s}: {acc:.4f}")

# 3) Сначала признаки, потом объекты
print("\n3) ОЧИСТКА: Признаки → Объекты")
print("-" * 70)
X_tr_few_feat, selector2 = remove_features(X_train_full, y_train_full)
X_tr_clean2, y_tr_clean2 = remove_noise(X_tr_few_feat, y_train_full)
X_te_clean2 = selector2.transform(X_test_full)
results_feat_obj = train_and_evaluate(X_tr_clean2, y_tr_clean2, X_te_clean2, y_test_full)
for model, acc in results_feat_obj.items():
    print(f"{model:15s}: {acc:.4f}")

# Итоговые выводы
print("\n" + "=" * 70)
print("ИТОГОВЫЕ ВЫВОДЫ (ЗАДАНИЕ 2)")
print("=" * 70)

best_raw = max(results_raw, key=results_raw.get)
print(f"\n1) Лучший классификатор на неочищенных данных:")
print(f"   >>> {best_raw}: {results_raw[best_raw]:.4f}")

avg_obj_feat = np.mean(list(results_obj_feat.values()))
avg_feat_obj = np.mean(list(results_feat_obj.values()))
avg_raw = np.mean(list(results_raw.values()))

print(f"\n2) Лучшая последовательность очистки:")
print(f"   Неочищенные данные:      {avg_raw:.4f} (средняя)")
print(f"   Объекты → Признаки:      {avg_obj_feat:.4f} (средняя)")
print(f"   Признаки → Объекты:      {avg_feat_obj:.4f} (средняя)")

if avg_obj_feat > avg_feat_obj:
    print(f"   >>> Лучше: Сначала удалить объекты, потом признаки")
else:
    print(f"   >>> Лучше: Сначала удалить признаки, потом объекты")

all_clean = {**{f"{k}_obj_feat": v for k, v in results_obj_feat.items()},
             **{f"{k}_feat_obj": v for k, v in results_feat_obj.items()}}
best_clean_key = max(all_clean, key=all_clean.get)
best_clean_model = best_clean_key.rsplit('_', 2)[0]
best_clean_acc = all_clean[best_clean_key]

print(f"\n3) Лучший классификатор на очищенных данных:")
print(f"   >>> {best_clean_model}: {best_clean_acc:.4f}")

print("\n" + "=" * 70)