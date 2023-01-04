#!/usr/bin/python3
"""Define lazy_matrix_mul class"""
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """Core of class"""
    return (np.matmul(m_a, m_b))
