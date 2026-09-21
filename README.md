# 💧 Sistema de Conscientização de Consumo de Água

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Linux](https://img.shields.io/badge/Debian-A81D33?style=for-the-badge&logo=debian&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)

## 📌 Objetivo do Sistema
Programa desenvolvido para a campanha de conscientização ambiental da companhia de saneamento local. O sistema classifica o perfil de consumo de água de imóveis (*comercial*, *casa* ou *apartamento*) com base no volume mensal ($m^3$) e exibe alertas educativos ao usuário.

---

## 📋 Regras de Negócio
- **Comercial:** Exibe aviso sobre tarifa comercial e plano corporativo.
- **Apartamento (< 10 $m^3$):** Alerta de *Consumo Econômico*.
- **Apartamento ou Casa ($\le$ 25 $m^3$):** Alerta de *Consumo Moderado* (padrão residencial).
- **Consumo Acima do Padrão Residencial:** Alerta de *Consumo Excessivo* orientando a verificação de vazamentos.

---

## 🚀 Como Executar no Debian Linux

1. Certifique-se de que o **Python 3** está instalado:
   ```bash
   python3 --version
