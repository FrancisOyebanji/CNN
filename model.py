{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "toc_visible": true,
      "include_colab_link": true
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
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/FrancisOyebanji/CNN/blob/main/model.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Au_DDE2oRXpa"
      },
      "outputs": [],
      "source": [
        "#This program calculates  Simple Interest\n",
        "def SI_Calculator ():\n",
        "    name = input('What is your name: ')\n",
        "    age = input(\"How old are you: \")\n",
        "    occupation = input(\"What is your occupation: \")\n",
        "    \n",
        "    operation = input(\"what would you like to calculate?\" \"enter 1 for SI, 2 for Principal, 3 for rate or 4 for time\")\n",
        "    \n",
        "    if operation == \"1\":\n",
        "        p = float(input(\"enter the principal: \"))\n",
        "        r = float (input(\"enter the rate: \"))\n",
        "        t = float (input(\"enter the time: \"))\n",
        "        print (\"Dear {}\".format(name), \"Your Simple Interest is:\") \n",
        "        print ((p*r*t)/100.0)\n",
        "        \n",
        "    elif operation == \"2\":\n",
        "        SI = float(input(\"what is the simple interest: \"))\n",
        "        r = float (input(\"enter the rate: \"))\n",
        "        t = float (input(\"enter the time: \"))\n",
        "        print (\"Dear {}\".format(name), \"Your Principal is:\")\n",
        "        print ((100*SI)/r*t)\n",
        "    \n",
        "    elif operation == \"3\":\n",
        "        SI = float(input(\"what is the simple interest: \"))\n",
        "        t = float (input(\"enter the time: \"))\n",
        "        p = float(input(\"enter the principal: \"))\n",
        "        print (\"Dear {}\".format(name), \"Your Rate is:\")\n",
        "        print ((100*SI)/p*t)\n",
        "    \n",
        "    elif operation == \"4\":\n",
        "        SI = float(input(\"what is the simple interest: \"))\n",
        "        p = float(input(\"enter the principal: \"))\n",
        "        r = float (input(\"enter the rate: \"))\n",
        "        print (\"Dear {}\".format(name), \"Your Time is:\")\n",
        "        print ((100*SI)/p*r)\n",
        "    else:\n",
        "        print(\"You supplied a wrong answer\")                    \n",
        "\n"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# New Section"
      ],
      "metadata": {
        "id": "FK9HjUXEBWT7"
      }
    }
  ]
}