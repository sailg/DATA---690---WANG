{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## Assignment 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import math"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## Required operations"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 4\n",
      " 5\n",
      " 6\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Minimum of integers: 4\n",
      "Maximum of integers: 6\n",
      "Range of integers: 4 - 6\n",
      "Mean of integers: 5.0\n",
      "Varience of integers: 0.6666666666666666\n",
      "Standard deviation of integers: 0.816496580927726\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    int_list=[]\n",
    "    for i in range(1,11):\n",
    "        inte=int(input())\n",
    "        int_list.append(inte)\n",
    "    print(\"Minimum of integers:\",min(int_list))\n",
    "    print(\"Maximum of integers:\",max(int_list))\n",
    "    print(\"Range of integers:\",min(int_list),\"-\",max(int_list))\n",
    "    print(\"Mean of integers:\",(sum(int_list)/10))\n",
    "    print(\"Varience of integers:\",sum((i - (sum(int_list)/10)) ** 2 for i in int_list) / len(int_list))\n",
    "    print(\"Standard deviation of integers:\",(sum((i - (sum(int_list)/10)) ** 2 for i in int_list) / len(int_list))**0.5)\n",
    "        \n",
    "except:\n",
    "    print(\"Please enter integers only\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
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
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
