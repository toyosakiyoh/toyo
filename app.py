#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 20:15:54 2024

@author: yotoyosaki
"""

import streamlit as st

input_num = st.number_input('Input a number', value=0)

result = input_num ** 2
st.write('Result: ', result)
