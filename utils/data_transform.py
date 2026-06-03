"""
UP 2050 — Data Transform Utilities
Loaders for all static data files (JSON/CSV). No runtime API calls.
"""

import json
import os
import pandas as pd

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')


def load_projections():
    """Load economic projections from data/projections.json.
    
    Returns:
        dict: Full projections data with 'metrics' and 'supplementary' keys.
    """
    path = os.path.join(DATA_DIR, 'projections.json')
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_demographics():
    """Load population pyramid data from data/demographics.json.
    
    Returns:
        dict: Demographics data with 'age_groups' list and metadata.
    """
    path = os.path.join(DATA_DIR, 'demographics.json')
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_infrastructure():
    """Load GeoJSON infrastructure data from data/infrastructure.json.
    
    Returns:
        dict: GeoJSON FeatureCollection with expressways, airports, cities.
    """
    path = os.path.join(DATA_DIR, 'infrastructure.json')
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_source_attribution():
    """Load source attribution table from data/source_attribution.csv.
    
    Returns:
        pd.DataFrame: Source attribution with metric, value, source columns.
    """
    path = os.path.join(DATA_DIR, 'source_attribution.csv')
    return pd.read_csv(path)


def get_metric_cards():
    """Extract the 4 primary metric cards for the data pulse section.
    
    Returns:
        list[dict]: List of metric dicts with label, baseline, projected, unit, etc.
    """
    data = load_projections()
    return data['metrics']


def get_age_groups_df():
    """Convert demographics age groups to a pandas DataFrame for easy plotting.
    
    Returns:
        pd.DataFrame: Age groups with male/female columns for 2024 and 2050.
    """
    data = load_demographics()
    return pd.DataFrame(data['age_groups'])
