{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "29fd03bc-6b9c-4751-8f28-faf0205dbb2d",
   "metadata": {},
   "outputs": [],
   "source": [
    "#imports\n",
    "\n",
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "#Making the streamlit\n",
    "\n",
    "st.title(\"BMI Calculator\")\n",
    "weight = st.number_input(\"Enter your weight in lbs:\", value = 0.0)\n",
    "height = st.number_input(\"Enter your height in inches:\", value = 0.0)\n",
    "\n",
    "if st.button(\"Calculate BMI:\"):\n",
    "    bmi_weight = weight * 703\n",
    "    BMI = (bmi_weight // height) // height\n",
    "\n",
    "    st.write(f\"Your BMI is {BMI:.1f}\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
