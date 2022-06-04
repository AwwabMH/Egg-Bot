import random

contractors_all = ["Ezkef LTD", "Zero Group", "The Egg Association", "AIA LLC", "The French Mercenary Guild", "The Standard Egg Company", "The International Monetary Fund", "The Spanish Inquisition", "The Holy Crusaders", "The Powell Group", "CrackHead Industries"]
jobs_all = ["Knight ⚔️", "Farmer 👨‍🌾", "Alchemist ⚗️", "Medical Officer 😷", "Financier 💵", "Manager 🤵", "Educator 👨‍🏫", "Trainer 🥊", "Scout ⚜️"]

av_conts = random.choices(contractors_all, k = 3)
av_jobs = random.choices(jobs_all, k = 3)