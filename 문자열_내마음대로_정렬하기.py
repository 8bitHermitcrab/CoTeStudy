{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled2.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPCbXh/ms3jKHP1vs4w+wAe"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "source": [
        "def solution(strings, n):\n",
        "    dic={}\n",
        "    for i in sorted(strings):\n",
        "        dic[i]=i[n]\n",
        "    answer=sorted(dic, key=lambda x: dic[x])\n",
        "    return answer"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YqnyO1_Drf4y",
        "outputId": "5fcaf45f-8559-4581-f74b-a5d5ef71baba"
      },
      "execution_count": 47,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[0, 2, 4, 6]"
            ]
          },
          "metadata": {},
          "execution_count": 47
        }
      ]
    }
  ]
}