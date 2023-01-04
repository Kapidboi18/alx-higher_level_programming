#!/usr/bin/python3
#Author Clinton Siloko
"""This module multiplies two matrices
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matricies using numpy
    """
    m_a = np.matrix(m_a)
    m_b = np.matrix(m_b)
    return np.matmul(m_a, m_b)
